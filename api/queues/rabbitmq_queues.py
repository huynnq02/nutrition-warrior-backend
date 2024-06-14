import pika
import os
import json
from ..models.user import User
from bson import ObjectId

QUEUE_URL = os.getenv('QUEUE_URL')

def push_update_user(message):
    connection = pika.BlockingConnection(pika.URLParameters(QUEUE_URL))
    channel = connection.channel()

    queue_name = 'update_user_queue'
    channel.queue_declare(queue=queue_name, durable=True)
    print(json.dumps(message))
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body= str(json.dumps(message,default=str)),
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    
    print(f" [x] Sent")
    # Đóng kết nối
    connection.close()

def receive_create_user():
    try:
        connection = pika.BlockingConnection(pika.URLParameters(QUEUE_URL))
        channel = connection.channel()

        queue_name = 'create_user_queue'
        channel.queue_declare(queue=queue_name, durable=True)

        channel.basic_consume(queue=queue_name, on_message_callback=handle_create_user_message, auto_ack=False)

        channel.start_consuming()
        # connection.close()
    except Exception as error:
        print("Can not receive create user",error)

def handle_create_user_message(ch, method, properties, body):
    try:
        message = json.loads(body)
        id = message['id']
        email = message['email']
        phone = message['phone_number']
        name = message['name']
        user = User(id=ObjectId(id), email=email, name=name, phone=phone)
        user.save()
    except Exception as error:
        print("Cannot create user",error) 
    ch.basic_ack(delivery_tag=method.delivery_tag)