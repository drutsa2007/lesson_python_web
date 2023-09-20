from mongo import mongo

mafia = mongo['mafia']
users = mafia['users']

# создание документа
users.insert_many([{"user": "Sergey2", "password": "qwerty123456"}])
result = users.insert_many([
    {"user": "Maxim2", "email": "123456qwerty"},
    {"user": "Aleksey2", "pincode": "123456qwerty"}
]).inserted_ids
print(result)
print(type(result))
for i in result:
    print(i, type(i))

