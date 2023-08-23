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

channel.queue_declare(queue='myQueue')

text = "message".encode()
channel.basic_publish(exchange="", routing_key='myQueue', body=text, properties=pika.BasicProperties())
print(text.decode()+" send")

channel.close()
connection.close()
