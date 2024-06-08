from dotenv import load_dotenv
import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict

load_dotenv()
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
 

@api_view(['GET'])
def search_food(request, food_name):
    """
    Search for food using the Edamam API.

    Parameters:
    - food_name: Food name.

    Returns:
    Response: The HTTP response from the Edamam API.
    """
    try:
        if not food_name:
            return Response({'error': 'Food name parameter is required'}, status=400)

        params = {'app_id': APP_ID, 'app_key': APP_KEY, 'ingr': food_name}
        base_url = 'https://api.edamam.com/api/food-database/v2/parser'
        autocomplete_url = 'https://api.edamam.com/auto-complete'
        response = requests.get(base_url, params=params)
        autocomplete_params = {'app_id': APP_ID, 'app_key': APP_KEY, 'q': food_name}
        autocomplete_response = requests.get(autocomplete_url, params=autocomplete_params)
        if response.status_code == 200:
            if autocomplete_response.status_code == 200:
                print("Auto complete was successful")
                autocomplete_data = autocomplete_response.json()
            else:
                autocomplete_data = {}
            data = response.json()
            if data.get('hints'):
                data['auto_complete'] = autocomplete_data
                return Response(data)
        return Response(None)
    
    except Exception as e:
        # Handle exceptions and return an appropriate response
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def random_food_for_today(request):
    try:
        base_url = 'https://www.themealdb.com/api/json/v1/1/random.php'
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json().get("meals")[0]
            return Response(data)
        return Response(None)
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 