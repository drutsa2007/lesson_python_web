# Импортируем нужные методы и классы из библиотеки
from aiogram import Bot, Dispatcher, executor, types
# Подключаем тип для команд
from aiogram.types import BotCommand

API_TOKEN = '6511515039:AAHuHApjggtPMWSPXwgdsu83hzY71GDb10g'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Создаем функцию создания команд
async def set_main_menu(dp):
    main_menu = [
        BotCommand(command='/start', description='Начало работы с ботом'),
        BotCommand(command='/help', description='Помощь'),
        BotCommand(command='/show_picture', description='Показать картинку'),
        BotCommand(command='/show_text', description='Показать текст'),
        BotCommand(command='/show_video', description='Показать видео')]
    await dp.bot.set_my_commands(main_menu)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Выбирай команды в меню.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Какая помощь нужна?")


@dp.message_handler(commands=['show_picture'])
async def send_welcome(message: types.Message):
    await message.reply("Показываю картинку")


@dp.message_handler(commands=['show_text'])
async def send_welcome(message: types.Message):
    await message.reply("Показываю текст")


@dp.message_handler(commands=['show_video'])
async def send_welcome(message: types.Message):
    await message.reply("Показываю видео")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Вы написали: " + message.text)


if __name__ == '__main__':
    # Устанавливаем собственное меню через on_startup
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)

