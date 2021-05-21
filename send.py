import pika
import requests
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='user_fetch')

response = requests.get("https://jsonplaceholder.typicode.com/users")

user_list = response.json()

for user in user_list: 
    channel.basic_publish(exchange='', routing_key='user_fetch', body=json.dumps(user))

print(" [x] Sent 'Users Fetched!'")
connection.close()