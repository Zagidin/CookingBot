from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="delete_product")
async def delete_product(callback: CallbackQuery):
    """
        Нужно дорелизовать скрипт, который при удалении продукта
        из пекарни удаляло и в корзине у пользователя.
    """

    await callback.message.answer(
        text="Удаление продукта из Пекарни - В разработке"
    )

    await callback.answer(
        text="⚡ Удаление продукта ⚡"
    )
