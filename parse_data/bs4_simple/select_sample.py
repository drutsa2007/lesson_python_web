import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://pythonworld.ru/samouchitel-python')
text = r.text

soup = bs(text, "html.parser")

# если 1 тэг на страницу, то можно получить так
print(soup.title.text)
# можно получить так
print(soup.select("head > title")[0].text)
# получить родителя
print(soup.title.parent.name)
# получить тег
print(soup.title.name)

print("---------------------------------------------------------")
# список мета-тегов
meta = soup.select("head > meta")
for m in meta:
    print(m)
    # attrs - выдает словарь всех аттрибутов тега: {"attr": "value", ...}
    for att, val in m.attrs.items():
        print("....", att, val)
    # можно удалить аттрибут
    # del m['id']

print("---------------------------------------------------------")
# поиск по классу
a1 = soup.select("p.strikeout.body")
