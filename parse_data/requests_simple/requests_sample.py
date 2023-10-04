import requests

# url = "http://yandex.ru"
# response = requests.get(url=url)
# # проверяем есть ли url
# try:
#     response.raise_for_status()
# except Exception as e:
#     print('Ошибка при загрузке страницы:\n' + str(e))
#
# # если ответ 200 - выполняем нужное
# if response.status_code == 200:
#     print('Успешно подключились.')
#
# # получаем объект класса Response
# print(response)
# # тип response
# print(type(response))
# # получаем заголовки
# print(response.request.headers)
# # получаем заголовки
# print(response.headers)
# # вывести конкретный заголовок
# print(response.headers['Content-Type'])
# print(response.headers.get('content-type'))  # или так
# # контент как текст (для будущего парсинга)
# print(response.text)  # выведет весь html в виде текста
# # если нужно получить двоичные данные то (возможно для сохранения картинки)
# print(response.content)  # выведет весь html в бинарном коде
# # код HTTP
# print(response.status_code)
# # кодировка сайта
# print(response.encoding)
# # куки
# print(response.cookies)
# # ссылка созданная
# print(response.url)



# # куки
# for i in r.cookies:
#     print(i)
#
# # передача параметров в get
# создаем словарь
# params = dict(cityId="CityCZ_1638")
# # отправляем в get-запрос
# r = requests.get("https://www.mvideo.ru/shops/store-list", params=params)
# # получаем url с параметрами
# print(r.url)
# https://www.mvideo.ru/shops/store-list?cityId=CityCZ_1638

#
# получаем ответ в виде json (если url выдает json)
r1 = requests.get('https://jsonplaceholder.typicode.com/todos/1')
json = r1.json()
print(json)
#
# передача заголовков
headers = {'user-agent': 'brauser/0.0.1'}
r2 = requests.get("https://jsonplaceholder.typicode.com/todos/1", headers=headers)

# запретить редирект
r3 = requests.get("https://jsonplaceholder.typicode.com/todos/1", allow_redirects=False)

# ограничить запрос по времени
r4 = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=0.001)

requests.get('https://api.github.com/user', auth=('username', 'password'))