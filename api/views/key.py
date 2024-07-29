from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.key import Key
from random import choice

@api_view(['GET'])
def get_key(request):
    try: 
        keys = Key.objects.all()
        print(keys)
        if not keys:
            raise ValueError("No API keys found in the database.")
        key = choice(keys).key
        print(key)
        return Response({'success': True, 'key': key}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
