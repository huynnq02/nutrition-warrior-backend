# message_queue/apps.py

from django.apps import AppConfig
import threading
from .rabbitmq_queues import receive_create_user

class MessageQueueConfig(AppConfig):
    name = 'message_queue'

    def ready(self):
        threading.Thread(target=receive_create_user).start()
