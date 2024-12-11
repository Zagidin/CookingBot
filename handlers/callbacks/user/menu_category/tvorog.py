from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="tvorog")
async def menu_category_tvg(callback: CallbackQuery):
    await callback.bot.send_message(
        chat_id=callback.from_user.id,
        text="ТВОРОЖНЫЙ ОТДЕЛ -> В РАЗРАБОТКЕ !"
    )
