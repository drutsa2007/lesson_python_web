import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from token_tg import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(Command('buttons'))
async def send_welcome(message):
    # Создаем 2 кнопки
    button_1 = KeyboardButton(text='Кнопка 1')
    button_2 = KeyboardButton(text='Кнопка 2')
    button_3 = KeyboardButton(text='Отправить телефон', request_contact=True)
    # Создаем объект клавиатуры
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2], [button_3]], resize_keyboard=True)
    await message.answer('Выберите кнопку', reply_markup=keyboard)


# Если придет текст с кнопки 1
@dp.message(F.text == 'Кнопка 1')
async def process_button1(message):
    await message.answer(text='Вы нажали кнопку 1', reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == 'Кнопка 2')
async def process_button2(message):
    await message.answer(text='Вы нажали кнопку 2', reply_markup=ReplyKeyboardRemove())


@dp.message(F.user_shared)
async def process_button3(message):
    await message.answer(text='Вы отправили телефон', reply_markup=ReplyKeyboardRemove())


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Набери команду /buttons.")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   asyncio.run(main())

