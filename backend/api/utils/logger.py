
"""
Coded by ChatGPT
Date 2025-04-27
Description: Logger

"""

import logging
import os
from django.http import JsonResponse
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)

def error_response(message, status=400, log=None):
    if log:
        logger.error(f"[{status}] {log}")
    return JsonResponse({"error": message}, status=status)


class Logger:
    def __init__(self, log_dir="logs", log_filename = "app.log"):
        self.log_dir = log_dir
        self.log_filename = log_filename
        self.log_path = os.path.join(self.log_dir, self.log_filename)

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    
    def _write_log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(formatted_message)

    def info(self, message):
        self._write_log("INFO", message)

    def warning(self, message):
        self._write_log("WARNING", message)

    def error(self, message):
        self._write_log("ERROR", message)

    def debug(self, message):
        self._write_log("DEBUG", message)