import configparser
import random
import time

import pika

config = configparser.ConfigParser()
config.read("config.ini")
user, pwd, host, port = config["RabbitMQ"]["user"], config["RabbitMQ"]["password"], \
                        config["RabbitMQ"]["host"], int(config["RabbitMQ"]["port"])

credentials = pika.PlainCredentials(user, pwd)
parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='myQueueTopic1')
channel.queue_declare(queue='myQueueTopic2')
channel.queue_declare(queue='myQueueTopic3')

channel.exchange_declare(exchange='myExchangeTopic', exchange_type="topic")
channel.queue_bind(exchange='myExchangeTopic', queue='myQueueTopic1', routing_key='auto.*.*')
channel.queue_bind(exchange='myExchangeTopic', queue='myQueueTopic2', routing_key='*.black.*')
channel.queue_bind(exchange='myExchangeTopic', queue='myQueueTopic3', routing_key='#.sedan')

routings = ["auto", "black", "sedan"]
for i in range(10):
    r = random.choice(routings) + '.' + random.choice(routings) + '.' + random.choice(routings)
    text = "message for topic " + r
    channel.basic_publish(exchange="myExchangeTopic", routing_key=r, body=text.encode())
    print(text + " send")
    time.sleep(1)

channel.close()
connection.close()
