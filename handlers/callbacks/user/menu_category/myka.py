from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="myka")
async def menu_category_flour(callback: CallbackQuery):
    await callback.bot.send_message(
        chat_id=callback.from_user.id,
        text="МУЧНОЙ ОТДЕЛ -> В РАЗРАБОТКЕ !"
    )
