from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


home_nav_admin = InlineKeyboardMarkup(row_width=True)

btn1 = InlineKeyboardButton(
    text="Добавить Новый Товар 📝",
    callback_data="add_new_product"
)

btn2 = InlineKeyboardButton(
    text="Удалить Товар 🗑",
    callback_data="delete_product"
)

btn3 = InlineKeyboardButton(
    text="Посмотреть Заказы 📋",
    callback_data="user_orders"
)

home_nav_admin.add(btn1)
home_nav_admin.row(btn2, btn3)
