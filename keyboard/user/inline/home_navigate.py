from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


home_navigate_user = InlineKeyboardMarkup(row_width=True)
btn1 = InlineKeyboardButton(
    text="На Главную",
    callback_data="home_navigate_user"
)
btn2 = InlineKeyboardButton(
    text="⚡ Меню ⚡",
    callback_data="look_menu"
)
home_navigate_user.row(btn1, btn2)