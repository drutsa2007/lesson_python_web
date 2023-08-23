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

channel.queue_declare(queue='myQueueDirect')

channel.exchange_declare(exchange='myExchangeDirect', exchange_type="direct")
channel.queue_bind(exchange='myExchangeDirect', queue='myQueueDirect')

text = "message for direct".encode()
channel.basic_publish(exchange="myExchangeDirect", routing_key='myQueueDirect', body=text)
print(text.decode()+" send")

channel.close()
connection.close()
