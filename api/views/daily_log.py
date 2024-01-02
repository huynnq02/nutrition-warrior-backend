# api/views/daily_log.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from ..models.user import User
from ..models.daily_log import DailyLog
from ..models.food import Food

@api_view(['POST'])
def add_food_to_daily_log(request, user_id, date):
    """
    Add a food item to the user's daily log for a specific date.

    Parameters:
    - user_id: User ID
    - date: Date in the format 'YYYY-MM-DD'
    
    Request Payload:
    - food_item: JSON object representing the food item to be added

    Returns:
    Response: The updated user object with the added food item.
    """
    try:
        user = get_object_or_404(User, id=user_id)
        # Find the DailyLog for the specified date or create a new one
        daily_log_instance = next((log for log in user.daily_logs if log.date.date() == date), None)
        if daily_log_instance is None:
            daily_log_instance = DailyLog(date=date)
            user.daily_logs.append(daily_log_instance)

        # Parse the food item from the request payload
        food_item = request.data.get('food_item')

        # Validate and add the food item to the appropriate meal (e.g., breakfast)
        if 'meal' in food_item and food_item['meal'] in ['breakfast', 'lunch', 'dinner']:
            meal = food_item['meal']
            daily_log_instance[meal].append(Food(**food_item))
            user.save()
            return Response(model_to_dict(user))
        else:
            return Response({'error': 'Invalid or missing meal information in the food item'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
