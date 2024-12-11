from aiogram.dispatcher.filters.state import StatesGroup, State


class ValidPasswd(StatesGroup):
    password = State()
