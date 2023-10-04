# pip install aiohttp
# pip install fake_useragent

from bs4 import BeautifulSoup as BS
import aiohttp
import asyncio
from fake_useragent import UserAgent
import time

url = "https://nsk.rbc.ru/"
h = {"User-Agent": UserAgent().random}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=h) as response:
            content = await aiohttp.StreamReader.read(response.content)
            soup = BS(content, "html.parser")
            news = soup.find_all("span", {"class": "main__feed__title"})
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
            with open("data2.csv", "w", encoding="utf-8") as f:
                f.write(t)


if __name__ == "__main__":
    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    end_time = time.time()
    execution_time = end_time - start_time
    print("Затраченное время", execution_time, "секунд")
    # Затраченное время 0.6002020835876465 секунд

