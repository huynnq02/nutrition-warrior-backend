from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..utils.progress_analysis import analyze_progress

@api_view(['GET'])
def user_progress(request, user_id):
    """
    Analyze the progress of the user in terms of weight, nutrition, and macros.

    Parameters:
    - user_id: User ID

    Returns:
    Response: The progress analysis including weight progress, nutritional averages, and advice.
    """
    try:
        user = User.objects.get(id=user_id)
        progress_data = analyze_progress(user)
        return Response({'success': True, 'data': progress_data}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
