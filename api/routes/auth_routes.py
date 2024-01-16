# api/routes/auth_routes.py
from django.urls import path
from ..views import auth

urlpatterns = [
    path('/reset-password', auth.reset_password, name='reset_password'),
    path('/auth-otp', auth.auth_otp, name='auth_otp'),
    path('/change-password',auth.change_password, name='change_password'),
    path('/', auth.create_user, name='create_user'),
    path('/login', auth.login_user, name='login_user'),
    path('/update/<str:id>', auth.update_user, name='update_user'),
   
]
    