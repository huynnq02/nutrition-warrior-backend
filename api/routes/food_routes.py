# api/routes/auth_routes.py
from django.urls import path
from ..views import food

urlpatterns = [
    path('/', food.create_user, name='create_user'),
    path('/', food.login_user, name='login_user'),
    path('/<str:id>/', food.update_user, name='update_user'),
]
