from django.urls import path
from ..views.background_task import background_task

urlpatterns = [
    path('/get-scheduled-tasks', background_task.get_scheduled_tasks, name='get_scheduled_tasks'),
]
