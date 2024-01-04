from django.urls import path
from ..views import background_task

urlpatterns = [
    path('/get-scheduled-tasks', background_task.get_scheduled_tasks, name='get_scheduled_tasks'),
]
