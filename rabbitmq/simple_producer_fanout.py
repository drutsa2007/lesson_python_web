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

channel.queue_declare(queue='myQueueFanout1')
channel.queue_declare(queue='myQueueFanout2')
channel.queue_declare(queue='myQueueFanout3')

channel.exchange_declare(exchange='myExchangeFanout', exchange_type="fanout")
channel.queue_bind(exchange='myExchangeFanout', queue='myQueueFanout1')
channel.queue_bind(exchange='myExchangeFanout', queue='myQueueFanout2')
channel.queue_bind(exchange='myExchangeFanout', queue='myQueueFanout3')

text = "message for fanout".encode()
channel.basic_publish(exchange="myExchangeFanout", routing_key='', body=text)
print(text.decode()+" send")

channel.close()
connection.close()
