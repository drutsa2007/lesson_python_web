from datetime import datetime
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

incr_value = 100000
redis_client.set("incr_key", "0")

start = datetime.now()

for _ in range(incr_value):
    redis_client.incr("incr_key")
res_without_pipeline = redis_client.get("incr_key")

time_without_pipeline = (datetime.now() - start).total_seconds()
print("Time taken: ", time_without_pipeline)  # result 21 second

redis_client.close()
