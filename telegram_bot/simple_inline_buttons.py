import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from token_tg import API_TOKEN

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(Command('buttons'))
async def send_welcome(message):
    # Создаем 2 кнопки
    button_1 = InlineKeyboardButton(text='Кнопка 1', callback_data='button1')
    button_2 = InlineKeyboardButton(text='Кнопка 2', callback_data='button2')
    button_3 = InlineKeyboardButton(text='Открыть фейсбук', url='https://facebook.com')
    # button_4 = InlineKeyboardButton(text='Открыть пользователя', url='tg://user?user_id=1322265845')
    button_4 = InlineKeyboardButton(text='Открыть пользователя', url='tg://openmessage?user_id=1322265845')

    # Создаем объект инлайн-клавиатуры
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1, button_2], [button_3], [button_4]])
    await message.answer('Выберите кнопку', reply_markup=keyboard)
    # await message.answer('Выберите кнопку', , parse_mode="HTML")
    # await message.answer('Выберите кнопку', , parse_mode=None)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery с data 'button1'
@dp.callback_query(F.data == 'button1')
async def process_button_1_press(callback):
    await callback.message.answer(
        text='Была нажата кнопка 1',
        reply_markup=callback.message.reply_markup)
    # для редактирование сообщения с которого была нажата кнопка используйте:
    # await callback.message.edit_text(....)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery с data 'button2'
@dp.callback_query(F.data == 'button2')
async def process_button_2_press(callback):
    await callback.message.answer(text='Была нажата кнопка 2', show_alert=True)


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Набери команду /buttons.")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
