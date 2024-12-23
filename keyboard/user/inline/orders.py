from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


order = InlineKeyboardMarkup(row_width=True)
btn1 = InlineKeyboardButton(
    text="⚡ Заказы ⚡",
    callback_data="order"
)
order.add(btn1)