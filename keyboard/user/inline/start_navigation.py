from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


navigate = InlineKeyboardMarkup(row_width=True)

btn1 = InlineKeyboardButton(
    text="Просмореть Меню 🔎",
    callback_data="look_menu"
)

btn2 = InlineKeyboardButton(
    text="Корзина 🛒",
    callback_data="basket"
)

btn3 = InlineKeyboardButton(
    text="История Заказов 📋",
    callback_data="order_history"
)

btn4 = InlineKeyboardButton(
    text="Статус Заказа ⌛",
    callback_data="order_state"
)

navigate.add(btn1)
navigate.row(btn3, btn4)
navigate.add(btn2)
