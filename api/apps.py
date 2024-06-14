from django.apps import AppConfig
import threading
from .queues.rabbitmq_queues import receive_create_user

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        threading.Thread(target=receive_create_user).start()
