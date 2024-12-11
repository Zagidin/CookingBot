from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationAdmin(StatesGroup):
    admin_name = State()
    admin_phone = State()
