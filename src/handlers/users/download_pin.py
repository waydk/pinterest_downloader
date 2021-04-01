import aiogram
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from pyquery import PyQuery

from loader import dp
from src.states.pinterest import Pinterest


async def get_download_url(link):
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})
    request_content = str(post_request.content, 'utf-8')
    download_url = PyQuery(request_content)('table.table-condensed')('tbody')('td')('a').attr('href')
    return download_url


@dp.message_handler(Command("pin_dow"))
async def bot_start(message: types.Message):
    await message.answer("Welcome 👋!\n\nEnter your link to the pin 📹 or 📷!\n\n"
                         "To finish sending links for videos or photos, you can write stop 🛑\n"
                         "Enjoy your use! 😃")
    await Pinterest.get_link.set()


@dp.message_handler(state=Pinterest.get_link)
async def get_url(message: types.Message, state: FSMContext):
    user_link = message.text
    if user_link == "stop":
        await state.finish()
        await message.answer("I hope I helped you! Good luck! 😃")
    else:
        try:
            video = await get_download_url(user_link)
            await message.answer_video(video, caption="Thank you for using this bot  🤠")
        except aiogram.utils.exceptions.BadRequest:
            await message.answer("Ooh, looks like you got the wrong link  😅")
