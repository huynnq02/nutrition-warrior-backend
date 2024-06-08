# api/routes/auth_routes.py
from django.urls import path
from ..views import food

urlpatterns = [
    path('/search/<str:food_name>', food.search_food, name='search_food'),
    path('/random',food.random_food_for_today, name='random_food_for_today')
    # path('/<str:id>/', food.update_user, name='update_user'),
]
