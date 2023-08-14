import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from token_tg import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


# если грубо, то таблица с полями
class Anketa(StatesGroup):
    familia = State()
    imya = State()
    vozrast = State()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Машина состояний приветствует вас. Наберите команду /anketa.")


@dp.message(Command("anketa"))
async def cmd_food(message, state: FSMContext):
    await message.answer(text="Как твоя фамилия?")
    # Запускаем сохранение фамилии
    await state.set_state(Anketa.familia)


@dp.message(Anketa.familia)
async def cmd_food(message, state: FSMContext):
    # сохраняем фамилию
    await state.update_data(familia=message.text.title())
    await message.answer(text="Как твоё имя?")
    # Запускаем сохранение имени
    await state.set_state(Anketa.imya)


@dp.message(Anketa.imya)
async def cmd_food(message, state: FSMContext):
    # сохраняем имя
    await state.update_data(imya=message.text.title())
    await message.answer(text="Сколько тебе лет?")
    # Запускаем сохранение возраста
    await state.set_state(Anketa.vozrast)


@dp.message(Anketa.vozrast)
async def cmd_food(message, state: FSMContext):
    await state.update_data(vozrast=message.text)
    await message.answer(text="Спасибо за информацию")
    # сохраняем все в файл
    with open("anketa.txt", 'w') as f:
        f.write(str(await state.get_data()))  # сохранит в словарь


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   asyncio.run(main())

