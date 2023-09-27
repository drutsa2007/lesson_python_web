import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# создаем объект pubsub
p = redis_client.pubsub()

while True:
    # текст, который хотим отправить
    x = input()
    # обработка выхода на всякий случай (делал для себя и проверки)
    if x == 'stop':
        break
    # публикуем сообщение в каналы
    redis_client.publish('my_channel', x.encode(encoding='utf-8'))
    redis_client.publish('my_chat', x.encode(encoding='utf-8'))

# список каналов
print(redis_client.pubsub_channels())

# количество подписчиков на каналы
print(redis_client.pubsub_numsub())
# количество подписок на уникальные шаблоны
print(redis_client.pubsub_numpat())

redis_client.close()