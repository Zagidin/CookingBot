from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


reg_user = ReplyKeyboardMarkup(resize_keyboard=True)
reg_user.add(
    KeyboardButton(
        text="Пройти Регистрацию 📝"
    )
)
