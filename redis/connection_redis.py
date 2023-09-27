import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

# Что-=то делаем

redis_client.close()
