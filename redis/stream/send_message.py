import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

redis_client.xadd("mystream3", {"fruit": "pineapple"})

redis_client.close()
