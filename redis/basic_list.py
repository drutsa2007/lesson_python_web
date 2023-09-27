import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# добавить элемент в начало, если нет то создаст
redis_client.lpush("list_one", "value1")
# добавить элемент в конец, если нет то создаст
redis_client.rpush("list_one", "value1")
# добавить только в существующий
redis_client.lpushx("list_one", "value1")
# добавить в существующий в конец
redis_client.rpushx("list_one", "value1")

# получить список значений в срезе
d = redis_client.lrange("list_one", 0, 3)

# получить элемент по индексу
redis_client.lindex("list_one", 2)
# длина списка по ключу
redis_client.llen("list_one")
# удалить и вернуть первый
a1 = redis_client.lpop("list_one")
# удалить и вернуть последний
a2 = redis_client.rpop("list_one")

redis_client.close()
