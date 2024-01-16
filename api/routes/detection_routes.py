from django.urls import path
from ..views import detection

urlpatterns = [
    path('/detect/', detection.detect_objects, name='detect_objects'),
]
