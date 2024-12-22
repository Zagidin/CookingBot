from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


category_product = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Мучное 🍞")
btn2 = KeyboardButton(text="Сладкое 🥐")
btn3 = KeyboardButton(text="Творожное 🥧")
category_product.row(btn1, btn2)
category_product.add(btn3)
