import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

redis_client.setbit("bitmap_one", 2, "0100010")
print(redis_client.getbit("bitmap_one", 2))
print(redis_client.get("bitmap_one"))

redis_client.close()
