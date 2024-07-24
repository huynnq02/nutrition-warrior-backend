from django.urls import path
from ..views import progress
urlpatterns = [
path('/analyze/<str:user_id>', progress.user_progress, name='user_progress'),
]
