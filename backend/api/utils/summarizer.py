import json
from api.utils.responder import get_GPT_response
from api.utils.savedb import save_news_to_db
from django.db import IntegrityError


"""
process analyzing news
return int success if theres no error, else it returns 1 if failed
"""
def on_analyzing_news() -> int:
    
    SUCCESS = 0
    FAILED = 1
    try:
        
        data = get_GPT_response()
        print("processing analyzing news")
        print(data)
        if not data:
            print("Failed to process data")
            return FAILED
        
        title = data.get('title')
        summary = data.get('content', [])
        date_creation = data.get("date_creation")
        keywords = data.get('keywords', [])
        image_url = data.get('image_url')
        analyzed_by = data.get('analyzed_by', 'manual')

        trend_data = data.get('trend_score', {})

        trend_score = trend_data.get('score', 0)

        trend_explanation = trend_data.get('explanation', '')


        if not title or not summary or not date_creation or not keywords:
            print("Failed to summarize data")
            return FAILED
        
        save_news_to_db(title, summary, keywords, date_creation, image_url, analyzed_by, trend_explanation, trend_score)
        return SUCCESS
    except IntegrityError as e:
        print("Database Intergrity ERROR", str(e))
    except Exception as e:
        print("Unexpected Error: ", str(e))
        return FAILED




