import google.generativeai as genai
from .api_key_manager import get_random_api_key

def gemini_analyze(logs):
    api_key = get_random_api_key()
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    data = {
        'logs': logs
    }
    
    prompt = """
    As a professional personal trainer, analyze the following my logs and provide insights and advice. 
    Structure your response exactly as follows:

    Analysis:
    • [Key observation 1]
    • [Key observation 2]
    ...
    • [Key observation ...]

    Advice:
    1. [Specific advice point 1]
    2. [Specific advice point 2]
    ...
    .... [Specific advice point ...]


    Ensure each section is clearly separated and formatted as shown above and should be easy for looking. Here are the user logs:
    """ + str(data)

    response = model.generate_content(prompt)
    print("🚀 ~ response:", response)
    
    return response.text
