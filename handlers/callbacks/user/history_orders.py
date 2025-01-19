from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="order_history")
async def order_history(callback: CallbackQuery):
    await callback.bot.send_message(
        chat_id=callback.from_user.id, text="История Заказов -> В РАЗРАБОКЕ !"
    )
