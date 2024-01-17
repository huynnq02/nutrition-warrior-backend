
from django.urls import path, include
from .auth_routes import urlpatterns as auth_urls  
from .food_routes import urlpatterns as food_urls  
from .daily_log_routes import urlpatterns as daily_log_urls
from .exercise_routes import urlpatterns as exercise_urls
from .tip_routes import urlpatterns as tip_urls
from .detection_routes import urlpatterns as detection_urls
from .macro_routes import urlpatterns as macro_urls
# from .background_task_routes import urlpatterns as background_task_urls

urlpatterns = [
    path('/auth', include(auth_urls)),
    path('/foods', include(food_urls)),
    path('/daily-logs', include(daily_log_urls)),
    path('/exercises', include(exercise_urls)),
    path('/tips', include(tip_urls)),
    path('/detection', include(detection_urls)),
    path('/', include(macro_urls))
    # path('/background-task', include(background_task_urls)),
  
]