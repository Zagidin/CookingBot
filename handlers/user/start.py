from bot.bot import dp
from base.models import User
from aiogram.types import Message
from base.base import SessionLocal
from keyboard.user.reply.registaration import reg_user
from keyboard.user.inline.start_navigation import navigate


@dp.message_handler(commands=["start", "старт"])
async def start_bot(msg: Message):

    session = SessionLocal()

    user_tg_id = msg.from_user.id
    user = session.query(User).filter(User.user_tg_id == str(user_tg_id)).first()

    if not user:
        await msg.answer(
            text=f"👋 Привет, <b>@{msg.from_user.username}</b>\n\n"
            f"🤖 Давайте пройдём небольшую регистрацию,\nдля входа в аккаунт 🗝🔓\n"
            f"\n<i>ЕСЛИ НЕ ПРОЙТИ РЕГИСТРАЦИЮ, ВЫ НЕ СМОЖЕТЕ ПОЛЬЗОВАТЬСЯ БОТОМ</i>",
            parse_mode="HTML",
            reply_markup=reg_user,
        )
        await msg.answer(
            text="Пожалуйста, нажмите на кнопку, которая появилась ниже, "
            "чтобы начать регистрацию 😉"
        )
    else:

        # Очистка сообщений
        try:
            for i in range(msg.message_id, 0, -1):
                await dp.bot.delete_message(msg.from_user.id, i)
        except:
            ...

        await msg.answer(
            text="⚡ <b>Навигация</b> ⚡", parse_mode="HTML", reply_markup=navigate
        )
