from bot.bot import dp
from aiogram.types import CallbackQuery
from keyboard.user.inline.start_navigation import navigate


@dp.callback_query_handler(text="home_navigate_user")
async def home_user_navigate(callback: CallbackQuery):

    await callback.bot.delete_message(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id
    )

    await callback.bot.send_message(
        chat_id=callback.from_user.id,
        text="⚡ <b>Навигация</b> ⚡",
        parse_mode="HTML",
        reply_markup=navigate
    )

    # Очистка сообщений
    try:
        for i in range(callback.message.message_id, 0, -1):
            await dp.bot.delete_message(callback.message.from_user.id, i)
    except: ...


    """
        Редактирование либо удаление всех сообщений при нажатии на кнопок меню или на главную
    """