from openai import OpenAI
client = OpenAI()
import json
import re

model_type = "gpt-4.1"
# model_type = "o3"
# model_type = "gpt-4o"
token_limit = 0

given_prompt = """
Create an interesting random trendy detailed article that you found across the internet.
The article must include an exact and realistic date of creation ranging 2020-2025 based on your research on that certain article.
Then rate how trending the article is right now based on your knowledge.
Respond in **valid JSON format** using the structure below:
"""
given_jsonformat = """{
    "title": "...",
    "content": {
    "introduction": "..."
    "body": "..."
    "conclusion": "..."
    },
    "keywords": ["..."],
    "date_creation": "...",
    "analyzed_by": "...",
    "trend_score": {
    "score": 0-100,
    "explanation": "..."
    }"""

given_system_role = "You are a professional news analyst AI."

"""
this is a given prompt  
@param:
    * prompt - user's input for manual response (default set to provided prompt "given_prompt")
"""
def get_GPT_response(prompt: str = given_prompt):
    print("processing GPT response")
    content = f"""
    {prompt}

    {given_jsonformat}
    """
    res = __fetch_response_completion(content)

    return res



"""
@description: private func, does the response completion. Generates a json format text done by model type.
@param:
    * prompt - user's input for manual response
"""
def __fetch_response_completion(prompt):
    response = client.chat.completions.create(
        model=model_type,
        messages=[
            {"role": "system", "content": given_system_role},
            {"role": "user", "content": prompt}
        ]
    )
    content = response.choices[0].message.content.strip()
    # cleaned = re.sub(r"^```json|```$", "", content, flags=re.MULTILINE).strip()

    print(content)
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return None

    img_title = data.get('title')
    if img_title:
        img_url = __fetch_unsplash_image(img_title)
    else:
        img_url = None
    
    data["image_url"] = img_url
    print("finish processing GPT response. Returning data")
    return data

import requests


#better to hide this
UNSPLASH_ACCESS_KEY = 'SqXgtUu_lWNHZcBxljIHIQZkJnqazkKWf3QdFtJVb5M'


"""
fetch image from unsplash API.
param: get query = title of gpt response for better image url search
"""
def __fetch_unsplash_image(query):
    print("processing image from unsplash")
    url = 'https://api.unsplash.com/search/photos'
    params = {
        'query': query,
        'client_id': UNSPLASH_ACCESS_KEY,
        'per_page': 1,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results')
        if results:
            print("finish processing image")
            return results[0]['urls']['regular']
        else:
            return None
    else:
        return None
