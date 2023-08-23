import configparser
import pika

config = configparser.ConfigParser()
config.read("config.ini")
user, pwd, host, port = config["RabbitMQ"]["user"], config["RabbitMQ"]["password"], \
                        config["RabbitMQ"]["host"], int(config["RabbitMQ"]["port"])

credentials = pika.PlainCredentials(user, pwd)
parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='myQueueHeaders1')
channel.queue_declare(queue='myQueueHeaders2')

channel.exchange_declare(exchange='myExchangeHeaders', exchange_type="headers")
channel.queue_bind(exchange='myExchangeHeaders', queue='myQueueHeaders1', routing_key="",
                   arguments={'x-match': 'all', 'key1': 1, 'key2': 2})
channel.queue_bind(exchange='myExchangeHeaders', queue='myQueueHeaders2', routing_key="",
                   arguments={'x-match': 'any', 'key1': 1, 'key2': 2})


text = "message for headers"
channel.basic_publish(
    exchange="myExchangeHeaders",
    routing_key="",
    body=text.encode(),
    properties=pika.BasicProperties(
        headers={'key1': 1, 'key2': 2}
    )
)
channel.basic_publish(
    exchange="myExchangeHeaders",
    routing_key="",
    body=text.encode(),
    properties=pika.BasicProperties(
        headers={'key1': 1, 'key2': 3}
    )
)
channel.basic_publish(
    exchange="myExchangeHeaders",
    routing_key="",
    body=text.encode(),
    properties=pika.BasicProperties(
        headers={'key1': 2, 'key2': 2}
    )
)
channel.basic_publish(
    exchange="myExchangeHeaders",
    routing_key="",
    body=text.encode(),
    properties=pika.BasicProperties(
        headers={'key1': 4, 'key2': 5}
    )
)
print(text + " send")

channel.close()
connection.close()
