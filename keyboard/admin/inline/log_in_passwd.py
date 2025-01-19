from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


passwd_start = InlineKeyboardMarkup()
passwd_start.add(
    InlineKeyboardButton(text="Войти ПАРОЛЕМ 🗝🔓", callback_data="log_in_password")
)
