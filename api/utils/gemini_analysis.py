import google.generativeai as genai
from .api_key_manager import get_random_api_key

def gemini_analyze(logs):
    api_key = get_random_api_key()
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    data = {
        'logs': logs
    }
    prompt="You are the professional PT, please analyze the following user logs and provide insights and advice, please response with readable and concise format: " + str(data)
    response = model.generate_content(prompt)
    print("🚀 ~ response:", response)
    
    
    return response.text
