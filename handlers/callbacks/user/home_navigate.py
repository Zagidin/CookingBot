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

    # Очистка всех предыдущих сообщений бота
    try:
        for message_id in range(callback.message.message_id - 1, 0, -1):
            try:
                await callback.bot.delete_message(
                    chat_id=callback.from_user.id,
                    message_id=message_id
                )
            except Exception:
                pass
    except Exception as e:
        print(f"Ошибка при очистке сообщений: {e}")