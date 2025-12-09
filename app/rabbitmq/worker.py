# app/rabbitmq/worker.py
import pika
import json
from app.service.chat_service import save_chat_message_to_db

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("rabbitmq")
    )
    channel = connection.channel()
    channel.queue_declare(queue='chat_queue')
    return connection, channel

def callback(ch, method, properties, body):
    data = json.loads(body)
    save_chat_message_to_db(data)
    print(f"Received message from {data['sender_id']} to {data['receiver_id']}")

def start_worker():
    connection, channel = get_rabbitmq_connection()
    channel.basic_consume(queue='chat_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()
