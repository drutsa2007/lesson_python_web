from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
import time
import re

URL = "https://www.onlinetrade.ru/catalogue/noutbuki-c9/"
# start_time = time.time()

# headers = {
#         'X-Requested-With': 'XMLHttpRequest',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
#     }
# url = 'https://www.dns-shop.ru/catalog/recipe/9ef9de6e3da00b3d/igrovye/?utm_source=www.dns-shop.ru'
# session = requests.session()
# session.headers.update(headers)
#
# rs = session.get(url)
# data = rs.text
# print(data)

o = Options()
o.add_experimental_option("detach", True)
# print(UserAgent().random)
# o.add_argument('User-Agent='+UserAgent().random)
# o.add_argument('Accept=*/*')
# o.add_argument('Accept-Language=ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
# o.add_argument('Referer='+URL)
# o.add_argument('Content-Type=text/plain;charset=UTF-8')
# o.add_argument('Origin='+URL)
# o.add_argument('Connection=keep-alive')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  #, options=o)
# driver.maximize_window()
driver.get(URL)
# ставим задержку, чтобы прогрузилась страница
time.sleep(2)
text = driver.page_source
# print(text)

# создаем парсера
soup = BS(text, "html.parser")
# ищем все элементы по исследованному тегу и классу
items = soup.find_all("div", class_="indexGoods__item")
d = []
for n in items:
    # получаем заголовок новости
    name = n.find("a", class_="indexGoods__item__name")
    price = n.find("span", itemprop="price")
    price_edit = price.text.replace(" ", "")
    d.append((name.text, int(price_edit[:-1])))

for i in d:
    print(i)

# # делаем текст
# t = ''
# for i in d:
#     t += i[0] + ';' + i[1] + '\n'
# # заносим текст в файл
# with open("data3.csv", "w", encoding="utf-8") as f:
#     f.write(t)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Затраченное время", execution_time, "секунд")
# Затраченное время 0.5203876495361328 секунд