from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.utils.logger import error_response
from api.utils.responder import get_GPT_response

from api.utils.savedb import save_news_to_db
from api.utils.summarizer import on_analyzing_news
import json


"""
@Depracated:

Analyze trending News in media.
Used this for testing purpose.

Front end could use this by calling API /analyze it's in "get" so it doesn't need to configure anything,
just call this api and it will automatically update the database
"""
@csrf_exempt
def analyze_news(request):
    if request.method != 'GET':
        return error_response('GET method required', status=405)
    
    result = on_analyzing_news()
    if result == 0:
        return JsonResponse({"message": "SUCCESS", "status": result})
    else:
        return JsonResponse({"message": "FAILED", "status": result}, status = 400)
