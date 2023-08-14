import asyncio
from aiogram import Bot, Dispatcher, Router
from token_tg import API_TOKEN
import router1
import router2

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

main_router = Router()


async def main():
    # Подключаем 2 роутера
    dp.include_routers(router1.router, router2.router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   asyncio.run(main())
