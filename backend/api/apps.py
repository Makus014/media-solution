from django.apps import AppConfig
import time
import threading
import os

from datetime import datetime, timedelta

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


    """
    run task every hour to update news
    """
    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':
            return

        from .utils.summarizer import on_analyzing_news

        def run_task():
            while True:
                now = datetime.now()
                next_run = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
                wait_seconds = (next_run - now).total_seconds()

                print(f"[Scheduler] Next run at: {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(wait_seconds)

                on_analyzing_news()
                print("[Scheduler] Ran task at:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        thread = threading.Thread(target=run_task, daemon=True)
        thread.start()