from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from ..models.user import User  # Import your User model

@api_view(['POST'])
def calculate_expenditure_method_1(request):
    """
    Calculate TDEE using Method 1.

    Required POST parameters:
    - height: The height of the user.
    - weight: The weight of the user.
    - gender: The gender of the user.
    - activity_level: The activity level of the user (Less Active, Not Sure, More Active).

    Returns:
    Response: The HTTP response with the calculated TDEE.
    """
    try:
        height = request.data.get('height')
        weight = request.data.get('weight')
        gender = request.data.get('gender')
        activity_level = request.data.get('activity_level')

        if activity_level == "Less Active":
            tdee = weight*14
        elif activity_level == "Not Sure":
            tdee = weight*16
        elif activity_level == "More Active":
            tdee = weight*18

        return Response({'tdee': tdee}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def calculate_average(logs, field):
    return sum(getattr(log, field) for log in logs) / len(logs)

KG_TO_LBS = 2.20462262
@api_view(['POST'])
def calculate_expenditure_method_2(request, id):
    
    try:
        user = User.objects.get(id=id)
        weekly_logs = user.weekly_logs
        if len(weekly_logs) < 2:
            return Response({'success': False, 'message': 'Insufficient data for calculation'}, status=status.HTTP_400_BAD_REQUEST)
        # week1 = weekly_logs[0]
        # week2 = weekly_logs[1]
        sorted_weekly_logs = sorted(weekly_logs, key=lambda x: x.week_number, reverse=True)
        week1 = sorted_weekly_logs[1]
        week2 = sorted_weekly_logs[0]

        week1_weight = calculate_average(week1.days, 'weight')
        week2_weight = calculate_average(week2.days, 'weight')
        week1_calories = calculate_average(week1.days, 'caloric_intake')
        week2_calories = calculate_average(week2.days, 'caloric_intake')
        average_colories = (week1_calories+ week2_calories)/2
        weight_change = (week2_weight - week1_weight) * KG_TO_LBS

        if weight_change == 0:
            tdee_min = tdee_max = average_colories
        elif 0.5 <= weight_change <= 1:
            tdee_min = average_colories + 200
            tdee_max = average_colories + 500
        elif -1 <= weight_change <= -0.5:
            tdee_max = average_colories - 200
            tdee_min = average_colories - 500
        else:
            return Response({'success': False, 'message': 'Invalid weight change'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'tdee_min': tdee_min, 'tdee_max': tdee_max}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def calculate_macros(request, id):
    """
    Calculate macros based on user input.

    Required POST parameters:
    - weight: The weight of the user.
    - goal: The user's fitness goal (Lose Fat, Maintain, Gain Muscle).
    - overweight: A boolean indicating whether the user is overweight.
    - deficit_surplus_percentage: The caloric deficit/surplus percentage.
    - daily_protein_ker_kg: The user's daily protein intake per kilogram.

    Returns:
    Response: The HTTP response with the calculated macros.
    """
    try:
        goal = request.data.get('goal')
        height = request.data.get('height')
        weight = request.data.get('weight')
        overweight = request.data.get('overweight')
        daily_protein_ker_kg = request.data.get('daily_protein_ker_kg')
        tdee = request.data.get('tdee')
        if goal == "Lose Fat":
            deficit_percentage = request.data.get('deficit_percentage')
            caloric_intake = tdee*(1-deficit_percentage/100)
        elif goal == "Gain Muscle":
            surplus_percentage = request.data.get('surplus_percentage')
            caloric_intake = tdee*(1+surplus_percentage/100)
        elif goal == "Maintain":
            caloric_intake = tdee

        if overweight == "Yes":
            daily_protein = height
        elif overweight == "No":
            daily_protein = daily_protein_ker_kg*weight

        daily_fat_percentage = request.data.get('daily_fat_percentage')
        daily_fat = caloric_intake*daily_fat_percentage/100/9
        daily_carb = (caloric_intake - (daily_protein * 4 + daily_fat * 9) )/4

        return Response({
            'goal' : goal,
            'caloric_intake_goal': caloric_intake,
            'daily_protein_goal': daily_protein,
            'daily_fat_goal': daily_fat,
            'daily_carb_goal': daily_carb
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

