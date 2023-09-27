import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# создаем стрим и заносим данные
s = redis_client.xadd("mystream3", {"city": "moscow"})
# напечатать ID стрима
print(s)

# создание группы для чтения стрима
a = redis_client.xinfo_groups("mystream3")
if not a:
    # создать группу
    redis_client.xgroup_create("mystream3", "mygroup1", 0)

# распечатать все группы стрима
print(*a)

redis_client.close()
