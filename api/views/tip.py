from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.tip import Tip

@api_view(['POST'])
def add_tips(request):
    try:
        data = request.data.get('tips')

        if not data or not isinstance(data, list):
            return Response({'success': False, 'message': 'Tips data is required as a list'}, status=status.HTTP_400_BAD_REQUEST)

        for tip_data in data:
            title = tip_data.get('title')
            explanation = tip_data.get('explanation')

            if not title or not explanation:
                return Response({'success': False, 'message': 'Title and explanation are required for each tip'}, status=status.HTTP_400_BAD_REQUEST)

            Tip.objects.create(title=title, explanation=explanation)

        return Response({'success': True, 'message': 'Health tips added successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
