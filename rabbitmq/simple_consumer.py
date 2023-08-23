import configparser
import traceback
import sys
import pika

config = configparser.ConfigParser()
config.read("config.ini")
user, pwd, host, port = config["RabbitMQ"]["user"], config["RabbitMQ"]["password"], \
                        config["RabbitMQ"]["host"], int(config["RabbitMQ"]["port"])

credentials = pika.PlainCredentials(user, pwd)
parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

myQueue = 'myQueue'

channel.queue_declare(queue=myQueue)
print("Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(body.decode())


while True:
    channel.basic_consume(myQueue, callback, auto_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        channel.stop_consuming()
        traceback.print_exc(file=sys.stdout)
