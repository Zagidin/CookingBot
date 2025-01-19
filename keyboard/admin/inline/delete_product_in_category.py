from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def delete_product_id_generate(product_id):
    product_delete = InlineKeyboardMarkup(row_width=True)
    product_delete.add(
        InlineKeyboardButton(
            text="❌ Удалить ❌",
            callback_data=f"delete_product_in_category:{product_id}",
        )
    )

    return product_delete
