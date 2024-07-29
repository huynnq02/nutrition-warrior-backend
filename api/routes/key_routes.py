from django.urls import path
from ..views import key
urlpatterns = [
path('/', key.get_key, name='get_key'),
]
