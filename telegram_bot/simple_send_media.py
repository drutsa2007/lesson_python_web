import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types.input_file import FSInputFile
from token_tg import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
file1 = FSInputFile("files/fff.jpg")
file2 = FSInputFile("files/fff.mp3")
file3 = FSInputFile("files/fff.mp4")
file4 = FSInputFile("files/fff.pdf")


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Машина состояний приветствует вас. Наберите команду /photo.")


@dp.message(Command("photo"))
async def cmd_food(message):
    await message.answer_photo(photo=file1)
    await message.answer_video(video=file3)
    await message.answer_audio(audio=file2)
    await message.answer_document(document=file4)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   asyncio.run(main())

