from datetime import datetime
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

incr_value = 100000
redis_client.set("incr_key", "0")

start = datetime.now()

pipe = redis_client.pipeline()
for _ in range(incr_value):
    pipe.incr("incr_key")
pipe.get("incr_key")
res_with_pipeline = pipe.execute()[-1]

time_with_pipeline = (datetime.now() - start).total_seconds()
print("Time taken: ", time_with_pipeline)  # result 3 second

redis_client.close()
