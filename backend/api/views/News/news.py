
from django.http import JsonResponse
from api.models.db import DatabaseConnector
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json

from api.utils.logger import error_response


"""
Description: get current news from database, it reads the current available news/media in the database.
The request method is "GET" because it only provides data without modifying the database. 
"""
def get_current_news(request):
    if request.method != "GET":
        return error_response("Get Method Required for this method", status=405)
    
    news_items = DatabaseConnector.objects.all().order_by('-created_at')
    data = [
        {
            "id": n.id,
            "title": n.title,
            "content": n.content,
            "keywords": n.keywords,
            "analyzed_by": n.analyzed_by,
            "image_url": n.image_url,
            "date_creation": n.date_creation,
            "time_created": n.created_at.isoformat(), 
            "trend_score": n.trend_score,
            "trend_explanation": n.trend_explanation
        }
        for n in news_items
    ]
    return JsonResponse(data, safe=False)





