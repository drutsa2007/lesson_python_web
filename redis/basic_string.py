import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# создание строкового типа
redis_client.set(name="key_one", value="10")
# создание + время жизни
redis_client.setex("important_key", 100, "important_value")
# получить строку
a = redis_client.get("key_one").decode("utf-8")

# проверить сущестование ключа
is_set = redis_client.exists("key_one")

# ограничиить по времени
redis_client.set(name="key_two", value="10", ex=5)

# добавить к значению
redis_client.append("key_two", value="22")

# Уменьшить значение
redis_client.decr("key_two", amount=3)
# Создает если не существует
redis_client.decrby("key_three", amount=3)
# увеличить значение
redis_client.incr("key_two", amount=5)
redis_client.incrby("key_four", amount=5)

# a = redis_client.getdel("key")  # Удалить после получения

print(redis_client.get("key_three"))

redis_client.close()
