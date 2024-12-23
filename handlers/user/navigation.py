from bot.bot import dp
from aiogram.types import Message
from keyboard.user.inline.start_navigation import navigate


@dp.message_handler(commands=["nav", "навигация"])
async def main_navigate(msg: Message):

    await msg.answer(
        text="⚡ <b>Навигация</b> ⚡",
        parse_mode="HTML",
        reply_markup=navigate
    )

    # Очистка сообщений
    try:
        for i in range(msg.message_id, 0, -1):
            await dp.bot.delete_message(msg.from_user.id, i)
    except:
        ...