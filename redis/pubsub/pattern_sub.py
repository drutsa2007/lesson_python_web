import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# создаем объект pubsub
p = redis_client.pubsub()

# подписываемся на канал(ы) по шаблону
p.psubscribe('*_chat')

# получение сообщений из подписок
for message in p.listen():
    print(message['data'])

# отписаться от канала
# p.punsubscribe('*_chat')

redis_client.close()