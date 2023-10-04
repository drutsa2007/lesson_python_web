from bs4 import BeautifulSoup as BS
import requests
from fake_useragent import UserAgent
import time

URL = "https://nsk.rbc.ru/"
start_time = time.time()

# получаем сайт с передачей случайного user-agent
r = requests.get(URL, headers={"user-agent": UserAgent().random})
# получаем весь текст-код сайта
text = r.text

# создаем парсера
soup = BS(text, "html.parser")
# ищем все элементы по исследованному тегу и классу
news = soup.find_all("span", class_="main__feed__title")
d = []
for n in news:
    # получаем ссылку на новость
    link = n.parent.parent['href']
    # получаем заголовок новости
    header = n.text
    d.append((header, link))

# делаем текст
t = ''
for i in d:
    t += i[0] + ';' + i[1] + '\n'
# заносим текст в файл
with open("data1.csv", "w", encoding="utf-8") as f:
    f.write(t)

end_time = time.time()
execution_time = end_time - start_time
print("Затраченное время", execution_time, "секунд")
# Затраченное время 0.5203876495361328 секунд