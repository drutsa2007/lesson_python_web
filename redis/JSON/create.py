import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, encoding="UTF-8", decode_responses=True)

# Не работает, требует RedisJSON модуль. rejson не помогает в Windows.

user1 = {
    "user": {
        "name": "Paul John",
        "email": "paul.john@example.com",
        "age": 42,
        "city": "London"
    }
}

json = redis_client.json()
json.set("user", '$', user1)
print(json.get("user"))

redis_client.close()


