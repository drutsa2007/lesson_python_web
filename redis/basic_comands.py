import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Сортированные множества sorted set
# хэш-таблицы hash
# битовые массивы bitmap
# битовое поле bitfield
# структуры hyperlog
# потоки stream
# пространственные данные geospatial
# json


# Тип значения по ключу



# Существование ключа
b1 = redis_client.exists("key_four")

# Удалить ключ
d2 = redis_client.delete("key_two")

# срок жизни ключа
a1 = redis_client.ttl("key_one")  # секунды
a2 = redis_client.pttl("key_one")  # милисекунды

redis_client.close()
