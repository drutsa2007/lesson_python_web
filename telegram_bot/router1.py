from aiogram import Router
from aiogram.filters.command import Command

router = Router()


@router.message(Command('start'))
async def cmd_start(message):
    await message.reply("Это старт")



