from api.models.db import DatabaseConnector
from datetime import datetime

"""
Save database
"""
def save_news_to_db(
        title: str,
        content: list,
        keywords: list,
        date_creation: str,
        image_url: str,
        analyzed_by: str,

        trend_explanation: str,
        trend_score: int
    ) -> DatabaseConnector:
    date_obj = datetime.strptime(date_creation, "%Y-%m-%d").date()

    return DatabaseConnector.objects.create(
        title=title,
        content=content,
        keywords=keywords,
        date_creation=date_obj,
        image_url=image_url,
        analyzed_by=analyzed_by,

        trend_explanation=trend_explanation,
        trend_score=trend_score
    )

