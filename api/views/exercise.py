from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import os

rapid_api_key = os.getenv('X-RapidAPI-Key')
rapid_api_host = os.getenv('X-RapidAPI-Host')

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