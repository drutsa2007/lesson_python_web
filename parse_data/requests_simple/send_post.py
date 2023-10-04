import requests

url = 'url'  # url куда отправляем
data = {"data1": "какие-то данные", "data2": "какие-то другие данные"}
# Передаем данные
message2 = requests.post(url, data=data)
# если сайт принимает json, то так и пишем
message1 = requests.post(url, json=data)
# проверка ушло или нет
print(message1.text)


# отправка файла
with open('файл картинки', 'rb') as f:
    r = requests.post(url, {'files': f})
    print(r)  # результат
# или так: files = {'file': open('report.xls', 'rb')}

# логинимся на сайте
data = {"объект в формате ключ: значение"}
session = requests.Session()
s = session.post(url, data=data)



# или так
from requests.auth import HTTPBasicAuth
# указываем параметры аутентификации
auth = HTTPBasicAuth('fake@example.com', 'password')
body = {"dd": "dd"}
resp = requests.post(url=url, data=body, auth=auth)
print(resp.status_code)
content = resp.json()
print(content['body'])

# отправка куки
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
