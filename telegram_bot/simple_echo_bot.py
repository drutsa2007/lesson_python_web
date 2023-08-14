# импортируем асинхронность, так скажем
import asyncio
# Импортируем нужные методы и классы из библиотеки
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
# Забираем API_TOKEN
from token_tg import API_TOKEN

# создаем объект bot
bot = Bot(token=API_TOKEN)
# создаем отслеживатель, который принимает все апдейты и обрабатывает их.
dp = Dispatcher()


# оборачиваем в декоратор, который отслеживает команду /start
@dp.message(Command('start'))
# создаем функцию (название любое), которая будет обрабатывать эту команду
async def cmd_start(message: types.Message):
    # отправляем сообщение в виде Reply
    await message.reply("Привет! Я Эхо-бот!\nОтправь мне любое сообщение")


# оборачиваем в декоратор, который будет выполнятся на любой текст
@dp.message()
async def echo(message: types.Message):
    # что-то пишем в ответ
    await message.answer("Вы написали: " + message.text)
    # пишем ответ, на последнюю фразу
    await message.reply("Вы написали: " + message.text)


# главная функция запуска бота
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   # запускаем в режиме асинхронности
   asyncio.run(main())
