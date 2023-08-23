import configparser
from typing import Dict
import pika

config = configparser.ConfigParser()
config.read("config.ini")


def create() -> Dict:
    credentials = pika.PlainCredentials(
        config["RabbitMQ"]["user"],  # пользователь
        config["RabbitMQ"]["password"]  # пароль
    )
    parameters = pika.ConnectionParameters(
        host=config["RabbitMQ"]["host"],  # сервер
        port=int(config["RabbitMQ"]["port"]),  # порт (по умолчанию 5672)
        credentials=credentials  # аутентификация
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return {"channel": channel, "connection": connection}
