from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..models.daily_log import DailyLog, ExerciseData, ExerciseSet
from ..models.exercise import Exercise
from ..serializers.user import UserSerializer
from datetime import datetime
import requests
import os

rapid_api_key = os.getenv('X-RapidAPI-Key')
rapid_api_host = os.getenv('X-RapidAPI-Host')


@api_view(['POST'])
def add_exercise_to_daily_log(request, user_id):
    """
    Add an exercise to the daily log of a user.

    Parameters:
    - user_id (str): The ID of the user.

    Request data:
    - exercise_data (dict): Exercise details including body_part, equipment, gif_url, name, target, secondary_muscles, and instructions.
    - sets (list): List of sets with reps and duration.

    Returns:
    Response: The HTTP response indicating the success or failure of the operation.
    """
    try:
        user = User.objects.get(id=user_id)
        print(1)
        today = datetime.now().date().isoformat()
        print(today)
        print(2)
        for daily_log in user.daily_logs:
            daily_log_date_str = daily_log.date.date().isoformat()

            print(daily_log_date_str)
            if today == daily_log_date_str:
                print("Equal")

        print(3)
        existing_daily_log = None
        for daily_log in user.daily_logs:
            daily_log_date_str = daily_log.date.date().isoformat()
            if today == daily_log_date_str:
                existing_daily_log = daily_log
                break
        print(3)
        if existing_daily_log:
            daily_log = existing_daily_log
            print("exists")
        else:
            daily_log_data = {
                "date": today,
                "exercise_data": []
            }
            daily_log = DailyLog(**daily_log_data)

            user.daily_logs.append(daily_log)
            user.save()
            print("not")
        exercise_data = request.data.get('exercise_data')
        exercise = Exercise(**exercise_data)

        sets_data = request.data.get('sets')
        sets = [ExerciseSet(reps=set_data.get('reps'), duration=set_data.get('duration')) for set_data in sets_data]
        exercise_data_instance = ExerciseData(exercise=exercise, sets=sets)
        daily_log.exercise_data.append(exercise_data_instance)
        
        user.save()
        serializer = UserSerializer(user)  # Use the serializer to convert the user object
        serialized_user = serializer.data
        return Response({'success': True, 'message': 'Exercise added to daily log successfully', 'data': serialized_user}, status=status.HTTP_201_CREATED)

    except User.DoesNotExist:
        return Response({'success': False, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#TODO: get_exercise_by_id

@api_view(['GET'])
def get_all_exercises(request):
    try:
        limit = request.GET.get('limit', '10')

        url = 'https://exercisedb.p.rapidapi.com/exercises'
        params = {'limit': limit}

        headers = {
            'X-RapidAPI-Key': rapid_api_key,
            'X-RapidAPI-Host': rapid_api_host
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return Response({'success': True, 'data': response.json()}, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response({'success': False, 'message': f'Request error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_exercises_by_name(request, exercise_name):
    try:
        limit = request.GET.get('limit', '10')

        url = f'https://exercisedb.p.rapidapi.com/exercises/name/{exercise_name}'
        params = {'limit': limit}

        headers = {
            'X-RapidAPI-Key': rapid_api_key,
            'X-RapidAPI-Host': rapid_api_host
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return Response({'success': True, 'data': response.json()}, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response({'success': False, 'message': f'Request error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_exercises_by_target(request, target_muscle):
    try:
        limit = request.GET.get('limit', '10')

        url = f'https://exercisedb.p.rapidapi.com/exercises/target/{target_muscle}'
        params = {'limit': limit}

        headers = {
            'X-RapidAPI-Key': rapid_api_key,
            'X-RapidAPI-Host': rapid_api_host
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return Response({'success': True, 'data': response.json()}, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response({'success': False, 'message': f'Request error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_exercises_by_equipment(request, equipment_type):
    try:
        limit = request.GET.get('limit', '20')

        url = f'https://exercisedb.p.rapidapi.com/exercises/equipment/{equipment_type}'
        params = {'limit': limit}

        headers = {
            'X-RapidAPI-Key': rapid_api_key,
            'X-RapidAPI-Host': rapid_api_host
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return Response({'success': True, 'data': response.json()}, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response({'success': False, 'message': f'Request error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_target_list(request):
    try:
        target_list = [
            "abductors", "abs", "adductors", "biceps", "calves",
            "cardiovascular system", "delts", "forearms", "glutes",
            "hamstrings", "lats", "levator scapulae", "pectorals",
            "quads", "serratus anterior", "spine", "traps", "triceps",
            "upper back"
        ]
        return Response({'success': True, 'data': target_list}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_body_part_list(request):
    try:
        body_parts = [
            "back", "cardio", "chest", "lower arms", "lower legs",
            "neck", "shoulders", "upper arms", "upper legs", "waist"
        ]
        return Response({'success': True, 'data': body_parts}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_equipment_list(request):
    try:
        equipment_list = [
            "assisted", "band", "barbell", "body weight", "bosu ball",
            "cable", "dumbbell", "elliptical machine", "ez barbell", "hammer",
            "kettlebell", "leverage machine", "medicine ball", "olympic barbell",
            "resistance band", "roller", "rope", "skierg machine", "sled machine",
            "smith machine", "stability ball", "stationary bike", "stepmill machine",
            "tire", "trap bar", "upper body ergometer", "weighted", "wheel roller"
        ]
        return Response({'success': True, 'data': equipment_list}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_exercises_for_body_part(request, body_part):
    try:

        limit = request.GET.get('limit', '20')

        url = f'https://exercisedb.p.rapidapi.com/exercises/bodyPart/{body_part}'
        params = {'limit': limit}

        headers = {
            'X-RapidAPI-Key': rapid_api_key,
            'X-RapidAPI-Host': rapid_api_host
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return Response({'success': True, 'data': response.json()}, status=status.HTTP_200_OK)

    except requests.exceptions.RequestException as e:
        return Response({'success': False, 'message': f'Request error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)