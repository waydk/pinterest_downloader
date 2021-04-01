from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def start(message: types.Message):
    await message.answer(f"Hello 👋, {message.from_user.full_name}!\n\n"
                         f"I'm Pinterest Downloader Bot 🤖\n"
                         f"So in Pinterest you can't download videos\n"
                         f"I'll help you with that\n\n"
                         f"You can also download photos!\n"
                         f"To get started: /pin_dow 📍")




