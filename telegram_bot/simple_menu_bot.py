import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.filters.command import Command

from token_tg import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


# Создаем функцию создания команд
async def set_main_menu(bot):
    main_menu = [
        BotCommand(command='/start', description='Начало работы с ботом'),
        BotCommand(command='/help', description='Помощь')]
    await bot.set_my_commands(main_menu)


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Выбирай команды в меню.")


@dp.message(Command(commands=['help']))
async def send_welcome(message: types.Message):
    await message.reply("Какая помощь нужна?")


@dp.message()
async def echo(message: types.Message):
    await message.answer("Вы написали: " + message.text)


async def main():
    # Устанавливаем собственное меню через startup
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   asyncio.run(main())
