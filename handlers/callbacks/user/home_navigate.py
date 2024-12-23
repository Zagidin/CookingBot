from bot.bot import dp
from aiogram.types import CallbackQuery
from keyboard.user.inline.start_navigation import navigate


@dp.callback_query_handler(text="home_navigate_user")
async def home_user_navigate(callback: CallbackQuery):
    await callback.bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text="⚡ <b>Навигация</b> ⚡",
        parse_mode="HTML",
        reply_markup=navigate
    )