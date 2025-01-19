from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_product_basket_generate(product_id):
    basket = InlineKeyboardMarkup(row_width=True)
    btn1 = InlineKeyboardButton(
        text="Добавить в корзину 🛒", callback_data=f"add_basket_product:{product_id}"
    )
    basket.add(btn1)

    return basket
