from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.tip import Tip

@api_view(['GET'])
def health_check(request):
    return Response("Service OK", status=status.HTTP_200_OK)