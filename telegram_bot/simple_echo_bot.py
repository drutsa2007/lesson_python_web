# Импортируем нужные методы и классы из библиотеки
from aiogram import Bot, Dispatcher, executor, types

# создаем константу с API токеном, который нам выдал BotFather
API_TOKEN = '6511515039:AAHuHApjggtPMWSPXwgdsu83hzY71GDb10g'

# создаем объект bot
bot = Bot(token=API_TOKEN)
# создаем отслеживатель, который принимает все апдейты и обрабатывает их.
dp = Dispatcher(bot)


# оборачиваем в декоратор, который отслеживает команду /start
@dp.message_handler(commands=['start'])
# создаем функцию (название любое), которая будет обрабатывать эту команду
async def send_welcome(message: types.Message):
    # отправляем сообщение в виде Reply
    await message.reply("Привет! Я Эхо-бот!\nОтправь мне любое сообщение")


# оборачиваем в декоратор, который будет выполнятся на любой текст
@dp.message_handler()
async def echo(message: types.Message):
    # что-то пишем в ответ
    await message.answer("Вы написали: " + message.text)


if __name__ == '__main__':
    # Запускаем чат-бот
    executor.start_polling(dp, skip_updates=True)
