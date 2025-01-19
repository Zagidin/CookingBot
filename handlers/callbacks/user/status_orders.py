from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="order_status")
async def order_state(callback: CallbackQuery):
    await callback.bot.send_message(
        chat_id=callback.from_user.id, text="Статус Готовности Заказа -> В РАЗРАБОТКЕ !"
    )
