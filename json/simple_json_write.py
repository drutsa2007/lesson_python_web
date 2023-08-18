import json


d = {"a": [1, "3", {"r1": 25, "r2": 44}, True, None], "zoo": "Simple Text", "user": 3}
print(json.dumps(d))  # сохраняем как есть
print(json.dumps(d, sort_keys=True))  # сортировка по ключам
print(json.dumps(d, separators=(',', ':')))  # компактное кодирование
with open('record.json', 'w') as f:
    f.write(json.dumps(d, indent=2))  # красивый вывод

