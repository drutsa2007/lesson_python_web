import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# начало транзакции
p = redis_client.pipeline(transaction=True)
# список команд
p.set(name="key_one1", value="10", ex=5)
p.set(name="key_one2", value="20", ex=15)
p.set(name="key_one3", value="30", ex=25)
p.set(name="key_one4", value="40", ex=35)

# выполнение списка команда
result = p.execute()
print(result)

redis_client.close()


