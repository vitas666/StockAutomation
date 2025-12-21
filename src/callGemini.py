import google.generativeai as genai
import os
from config import gemini_key

api_key = os.environ["GEMINI_API_KEY"]= gemini_key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('models/gemini-2.5-pro')

def AIResponse(input) -> str:
    try:
        response = model.generate_content(input)
        return response.text
    except:
        return('model name might be wrong.')

