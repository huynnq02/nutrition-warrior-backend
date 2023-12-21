
from django.urls import path, include
from .auth_routes import urlpatterns as auth_urls  
from .food_routes import urlpatterns as food_urls  

urlpatterns = [
    path('/auth', include(auth_urls)),
    path('/food', include(food_urls)),

]