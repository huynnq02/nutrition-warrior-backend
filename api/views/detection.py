# food_detection/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def detect_food_in_image(request):
    try:
        # Assuming the image is sent as a file in the request
        image = request.FILES['image']

        # Call your YOLO detection function
        detected_food = detect_food(image)

        # Return the detected food as a response
        return Response({'success': True, 'detected_food': detected_food}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
