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
    - meal: The meal to which the food item should be added (e.g., 'breakfast', 'lunch', 'dinner')

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

        # Parse the food item and meal from the request payload
        food_item_data = request.data.get('food_item')
        meal = request.data.get('meal')

        # Validate and add the food item to the appropriate meal (e.g., breakfast)
        if meal and meal in ['breakfast', 'lunch', 'dinner']:
            # Create a new food item and add it to the specified meal
            new_food_item = Food(**food_item_data)
            daily_log_instance[meal].append(new_food_item)

            # Update the nutritional values based on the added food item
            daily_log_instance.caloric_intake += new_food_item.nutrients.get("ENERC_KCAL", 0)
            daily_log_instance.protein_intake += new_food_item.nutrients.get("PROCNT", 0)
            daily_log_instance.carb_intake += new_food_item.nutrients.get("CHOCDF", 0)
            daily_log_instance.fat_intake += new_food_item.nutrients.get("FAT", 0)

            # Update the remaining values
            daily_log_instance.caloric_remain = max(0, user.caloric_intake_goal - daily_log_instance.caloric_intake)
            daily_log_instance.protein_remain = max(0, user.daily_protein_goal - daily_log_instance.protein_intake)
            daily_log_instance.carb_remain = max(0, user.daily_carb_goal - daily_log_instance.carb_intake)
            daily_log_instance.fat_remain = max(0, user.daily_fat_goal - daily_log_instance.fat_intake)

            user.save()
            return Response(model_to_dict(user))
        else:
            return Response({'error': 'Invalid or missing meal information in the request'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)