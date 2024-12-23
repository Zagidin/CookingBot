from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


basket = InlineKeyboardMarkup(row_width=True)
btn1 = InlineKeyboardButton(
    text="Добавить в корзину 🛒",
    callback_data="add_basket_product"
)
basket.add(btn1)