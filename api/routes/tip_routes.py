from django.urls import path
from ..views import tip
urlpatterns = [
path('/', tip.add_tips, name='add_tips'),
]
