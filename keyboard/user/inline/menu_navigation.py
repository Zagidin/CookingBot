from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


manu_nav = InlineKeyboardMarkup(row_width=True)

btn1 = InlineKeyboardButton(text="Мучное 🍞", callback_data="myka")

btn2 = InlineKeyboardButton(text="Сладкое 🥐", callback_data="sladkoe")

btn3 = InlineKeyboardButton(text="Творожное 🥧", callback_data="tvorog")

manu_nav.add(btn1)
manu_nav.add(btn2)
manu_nav.add(btn3)
