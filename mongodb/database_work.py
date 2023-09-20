from mongo import mongo

# Создание БД через словарь
db1 = mongo['myDB1']

# создание коллекции
myCol1 = db1['myCollection1']
# принудительное создание коллекции
myCol3 = db1.create_collection("myCollection3")

# создание документа
myCol1.insert_one({"user": "Sergey"})
myCol1.insert_one({"user": "Michail"})

# количество документов в коллекции
count_docs = myCol1.count_documents({})
print(count_docs)

# переименование коллекции
db1['myCollection1'].rename("myNewCollection1")

myCols = db1.list_collection_names()
# ничего не выведет, если нет документов в коллекции
print(myCols)

mydbs = mongo.list_database_names()
# выведет только 3 предустановленные БД,
# потому что нет документов в созданных db1 и db2.
print(mydbs)
mongo.drop_database("myDB1")


