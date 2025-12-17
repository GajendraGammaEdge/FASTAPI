# app/rabbitmq/publisher.py
import pika
import json
import os
import time

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "admin")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "password123")
QUEUE = "chat_queue"

def get_rabbitmq_connection():
    retries = 10
    for i in range(retries):
        try:
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
            parameters = pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                credentials=credentials
            )

            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE, durable=True)
            return connection, channel

        except pika.exceptions.AMQPConnectionError:
            print("Waiting for RabbitMQ...")
            time.sleep(3)

    raise Exception("RabbitMQ not available")

def publish_message(sender_id: int, receiver_id: int, message: str):
    connection, channel = get_rabbitmq_connection()
    payload = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "message": message
    }

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE,
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )

    connection.close()
