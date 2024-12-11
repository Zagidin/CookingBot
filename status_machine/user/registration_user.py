from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
    user_name = State()
    user_phone = State()
