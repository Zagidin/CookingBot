from os import getenv
from bot.bot import dp
from base.models import Admin
from dotenv import load_dotenv
from aiogram.types import Message
from base.base import SessionLocal


load_dotenv()


@dp.message_handler(commands=["support", "поддержка"])
async def bot_admin_support(msg: Message):
    session = SessionLocal()

    admin_data = session.query(
        Admin.admin_name, Admin.admin_phone, Admin.admin_tg_id
    ).all()

    if admin_data:
        for admin in admin_data:
            admin_tg_id = admin[2]

            try:
                tg_user = await dp.bot.get_chat(admin_tg_id)
                username = tg_user.username if tg_user.username else "Не указан"
            except:
                username = "Не найден"

            await msg.answer(
                text=f"⚡ Администратор Пекарни ⚡\n\n"
                f" 🚩 Имя: <a href='https://t.me/{username}'>{admin[0]}</a>\n"
                f" ☎ Телефон: +{admin[1]}\n",
                parse_mode="HTML",
            )
    else:
        await msg.answer(
            text=f"🚩 Администратор не найден 🚩\n\n"
            f"🤖 <i><b>Нет информации об админе, похоже админ не был зарегистрирован</b></i> ❌\n\n"
            f"☎ Номер Горячей Линии: +{getenv('ADMIN_PHONE_SUPPORT')}",
            parse_mode="HTML",
        )
