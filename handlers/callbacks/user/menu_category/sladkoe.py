from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="sladkoe")
async def menu_category_sweet(callback: CallbackQuery):
    await callback.bot.send_message(
        chat_id=callback.from_user.id,
        text="СЛАДКИЙ ОТДЕЛ -> В РАЗРАБОТКЕ !"
    )
