# api/routes/auth_routes.py
from django.urls import path
from ..views import auth

urlpatterns = [
    path('/', auth.create_user, name='create_user'),
    path('/login', auth.login_user, name='login_user'),
    path('/<str:id>', auth.update_user, name='update_user'),
]
