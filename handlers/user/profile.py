from bot.bot import dp
from base.models import User
from aiogram.types import Message
from base.base import SessionLocal


@dp.message_handler(commands=["profile", "профиль"])
async def user_profile(msg: Message):

    session = SessionLocal()

    user_data = session.query(User.user_name, User.user_phone, User.user_tg_id).all()

    for user in user_data:
        user_tg_id = user[2]

        try:
            tg_user = await dp.bot.get_chat(user_tg_id)
            username = tg_user.username if tg_user.username else "Не указан"
        except:
            username = "Не найден"

        await msg.answer(
            text=f"⚡ Профиль ⚡\n\n"
                 f" 👤 Имя: <a href='https://t.me/{username}'>{user[0]}</a>\n"
                 f" 📱 Телефон: {user[1]}\n"
                 f" 💬 Telegram: @{username}",
            parse_mode="HTML"
        )