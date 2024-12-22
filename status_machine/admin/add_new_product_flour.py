from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewProductFlour(StatesGroup):
    name = State()
    description = State()
    price = State()
    url_photo = State()
