
from aiogram.dispatcher.filters.state import StatesGroup, State


class Pinterest(StatesGroup):
    get_link = State()
