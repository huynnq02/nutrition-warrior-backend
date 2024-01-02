from django.urls import path
from ..views import daily_log

urlpatterns = [
    path('/add_food/<str:user_id>/<str:date>', daily_log.add_food_to_daily_log, name='add_food_to_daily_log'),
]
