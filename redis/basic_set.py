import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# добавляем в множество, если нет такого создаем
redis_client.sadd("set_one", "321")

# количество элементов во множестве
print(redis_client.scard("set_one"))

# есть ли значение во множестве
print(redis_client.sismember("set_one", "333"))\

# получить все элементы множества
print(redis_client.smembers("set_one"))

# перенести элементы в другое множество с удалением из первого
redis_client.smove("set_one", "set_two", "123")
print(redis_client.smembers("set_two"))
print(redis_client.smembers("set_one"))

# получить случайные элементы (кол-во указывается) из множества с удалением
s = redis_client.spop("set_two", 5)

# получить случайные елементы без удаления
s1 = redis_client.srandmember("set_one", 5)

# удалить элементы из множества
redis_client.srem("set_two", "123", "321")

redis_client.close()
