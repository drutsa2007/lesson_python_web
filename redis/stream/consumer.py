import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# количество записей в потоке
print(redis_client.xlen("mystream3"))

# получаем ID стрима
print(redis_client.xinfo_stream("mystream3"))

# создать слушателя в группе
c = redis_client.xreadgroup("mygroup1", "JACK", {"mystream3": "0"}, 5)
print(c)

print(redis_client.xinfo_consumers("mystream3", "mygroup1"))

# прочитать все сообщения стрима. количество первые 10 записей
c = redis_client.xread({"mystream3": b'0-0'}, 10)
# показать все
# c = redis_client.xread({"mystream3": 0}, 10)
# показать только свежие
# c = redis_client.xread({"mystream3": '$'}, 10)
print(c)

# удалить сообщение по ID
# redis_client.xdel("mystream3", 1695815106653)

redis_client.close()
