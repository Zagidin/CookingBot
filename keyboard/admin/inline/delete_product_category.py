from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


product_category = InlineKeyboardMarkup(row_width=True)
btn1 = InlineKeyboardButton(
    text="Мучной 🍞", callback_data="delete_category_product_flour"
)
btn2 = InlineKeyboardButton(
    text="Сладкий 🥐", callback_data="delete_category_product_sweet"
)
btn3 = InlineKeyboardButton(
    text="Творожный 🥧", callback_data="delete_category_product_cottage_cheese"
)
product_category.row(btn1, btn2)
product_category.add(btn3)
