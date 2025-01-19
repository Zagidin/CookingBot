from bot.bot import dp
from aiogram.types import CallbackQuery
from keyboard.admin.inline.delete_product_category import product_category


@dp.callback_query_handler(text="delete_product")
async def delete_product(callback: CallbackQuery):
    """
    Нужно дорелизовать скрипт, который при удалении продукта
    из пекарни удаляло и в корзине у пользователя.
    """

    await callback.message.answer(
        text="Выберите Категорию продукции 👇", reply_markup=product_category
    )

    await callback.answer(text="⚡ Удаление продукта ⚡")
