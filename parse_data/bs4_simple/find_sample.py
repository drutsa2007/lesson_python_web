import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://pythonworld.ru/samouchitel-python')
text = r.text

soup = bs(text, "html.parser")

# вложенный поиск
print(soup.find("head").find("title"))