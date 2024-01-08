
from django.urls import path, include
from .auth_routes import urlpatterns as auth_urls  
from .food_routes import urlpatterns as food_urls  
from .daily_log_routes import urlpatterns as daily_log_urls
# from .background_task_routes import urlpatterns as background_task_urls

urlpatterns = [
    path('/auth', include(auth_urls)),
    path('/food', include(food_urls)),
    path('/daily-log', include(daily_log_urls)),
    # path('/background-task', include(background_task_urls)),
  
]