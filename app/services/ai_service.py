import google.generativeai as genai
from flask import current_app

def _get_model():
    genai.configure(api_key=current_app.config.get("GEMINI_API_KEY"))
    return genai.GenerativeModel("gemma-3-4b-it")


def _get_model1():
    genai.configure(api_key=current_app.config.get("GEMINI_API_KEY"))
    return genai.GenerativeModel("gemini-3.1-flash-lite-preview")



def crop_advisory(location, soil_type, crop, language):
    model = _get_model()

    prompt = f"""
You are an agricultural expert.

Give crop advice in this format:
Answer:
- Suitable crop
- Reason
- Fertilizer suggestion
- Tips

Give in short , in points ,1-2 small+breif points each , and answer should be in easy language , just like you are explaining a illetrate person

Location: {location}
Soil: {soil_type}
Crop: {crop}
Language: {language}
If the given input is not releted to farming , irrigation , fertilizer , pesticide and all , then give output something like ask question releted only to farming , dont give any answer to other question , becuase this is used in a farmer releted app
"""

    return model.generate_content(prompt).text


def get_ad_chat(msg, lang, image=None, pdf=None):

    lang = "hindi" if lang=="hi" else "english"

    model = _get_model1()

    prompt = f"""
You are an agricultural expert.

Give crop advice in this format:
Answer:
    Give details about whatever the user asked in the user message.

Give in short , in points ,1-2 small+breif points each , and answer should be in easy language , just like you are explaining a illetrate person

user message : {msg}
langague for output : {lang}

ignore any extra details , give proper , breif output , becasue user is most probably farmer.
If the given input is not releted to farming , irrigation , fertilizer , pesticide and all , then give output something like ask question releted only to farming , dont give any answer to other question , becuase this is used in a farmer releted app
"""
    print(lang)
    return model.generate_content(prompt).text


def soil_health(soil_type, ph, language):
    model = _get_model()

    prompt = f"""
Give soil improvement advice.

Format:
Answer:
- Soil condition
- What to add
- Fertilizer tips

Give in short , in points ,1-2 small+breif points each , and answer should be in easy language , just like you are explaining a illetrate person

Soil: {soil_type}
pH: {ph}
Language: {language}
If the given input is not releted to farming , irrigation , fertilizer , pesticide and all , then give output something like ask question releted only to farming , dont give any answer to other question , becuase this is used in a farmer releted app
"""

    return model.generate_content(prompt).text


def weather_advisory(location, language):
    model = _get_model()

    prompt = f"""
Give general weather-based farming advice.

Format:
Answer:
- What farmer should do
- Precautions

Give in short , in points ,1-2 small+breif points each , and answer should be in easy language , just like you are explaining a illetrate person

Location: {location}
Language: {language}
If the given input is not releted to farming , irrigation , fertilizer , pesticide and all , then give output something like ask question releted only to farming , dont give any answer to other question , becuase this is used in a farmer releted app
"""

    return model.generate_content(prompt).text


def pest_detection_info(crop, problem, language):
    model = _get_model()

    prompt = f"""
Farmer has pest issue.

Format:
Answer:
- Possible pest/disease
- Solution
- Pesticide suggestion

Give in short , in points ,1-2 small+breif points each , and answer should be in easy language , just like you are explaining a illetrate person

Crop: {crop}
Problem: {problem}
Language: {language}
If the given input is not releted to farming , irrigation , fertilizer , pesticide and all , then give output something like ask question releted only to farming , dont give any answer to other question , becuase this is used in a farmer releted app
"""

    return model.generate_content(prompt).text


def market_advisory(crop, location, language):
    model = _get_model()

    prompt = f"""
Give market advice.

Format:
Answer:
- Current trend
- When to sell
- Tips

Give in short , in points ,1-2 small+breif points each , and answer should be in easy language , just like you are explaining a illetrate person

Crop: {crop}
Location: {location}
Language: {language}
If the given input is not releted to farming , irrigation , fertilizer , pesticide and all , then give output something like ask question releted only to farming , dont give any answer to other question , becuase this is used in a farmer releted app
"""

    return model.generate_content(prompt).text