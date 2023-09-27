import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# вставка или создание через словарь
redis_client.hset("hash_one", mapping={"1": "qwe", "2": "sdfg"})
# вставка или создание через ключ и значение
redis_client.hset("hash_one", "3", "aaaaaaa")
print(redis_client.hget("hash_one", "3"))

# удаление ключа(ключей) в hash
redis_client.hdel("hash_one", "1")
print(redis_client.hget("hash_one", "1"))

redis_client.close()
