from mongo import mongo

mafia = mongo['mafia']
users = mafia['users']

# создание документа
users.insert_one({"user": "Sergey", "passord": "qwerty123456"})
result = users.insert_one({"user": "Maxim", "passord": "123456qwerty"}).inserted_id
print(result)
# _id - уникальный идентификатор, если не уследите за уникальностью, будут проблемы
# лучше не указывать, мое мнение
result2 = users.insert_one({"_id": 1, "user": "Maxim", "passord": "123456qwerty"}).inserted_id
print(result2)

