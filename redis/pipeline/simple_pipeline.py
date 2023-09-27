import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

pipe = redis_client.pipeline()
pipe.set("a", "a value")
pipe.set("b", "b value")
pipe.get("a")
pipe.execute()

# Или так:

pipe = redis_client.pipeline()
pipe.set("a1", "a1 value").set("b1", "b1 value").get("a1").execute()

redis_client.close()
