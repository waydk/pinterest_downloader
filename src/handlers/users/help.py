from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def show_info(message: types.Message):
    await message.answer('📍 In order to start using the bot: \n'
                         '📍 Copy the link to the pin: <a href="https://www.pinterest.com/">Pinterest</a>\n'
                         '📍 /pin_dow - Start downloading video or photo\n'
                         '📍 Any questions: <a href="https://t.me/waydk">Telegram</a>', disable_web_page_preview=True)
