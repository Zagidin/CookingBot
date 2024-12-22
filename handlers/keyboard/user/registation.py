from status_machine.user.registration_user import Registration
from keyboard.user.inline.start_navigation import navigate
from keyboard.user.reply.phone import phone
from aiogram.dispatcher import FSMContext
from base.base import SessionLocal
from base.models import User
from bot.bot import dp
from aiogram.types import (
    ReplyKeyboardRemove,
    ContentType,
    Message
)


@dp.message_handler(text="Пройти Регистрацию 📝")
async def registration_user(msg: Message):
    await msg.answer(
        text="Введите Ваше имя ✍",
        reply_markup=ReplyKeyboardRemove()
    )

    await Registration.user_name.set()


@dp.message_handler(state=Registration.user_name)
async def reg_user_name(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['user_name'] = msg.text

    await msg.answer(
        text="Теперь поделитесь номеро телефона нажав на кнопку ниже ☎",
        reply_markup=phone
    )

    await Registration.user_phone.set()


@dp.message_handler(state=Registration.user_phone, content_types=ContentType.CONTACT)
async def reg_user_phone_and_id(msg: Message, state: FSMContext):
    """ 🚩 Номер телефона пользователя и USER_ID """

    session = SessionLocal()

    async with state.proxy() as data:
        data['user_phone'] = msg.contact.phone_number

    async with state.proxy() as data:
        data['user_tg_id'] = msg.from_user.id

    await state.finish()

    await msg.answer("📝")
    await msg.answer(
        text=f"{data['user_name']}, Вы успешно зарегистрировались! ✅",
        reply_markup=ReplyKeyboardRemove()
    )

    await msg.answer(
        text="Добро пожаловать в Пекарню -< ZAGA >- 🙌\n"
             "\n⚡ Навигация ⚡",
        reply_markup=navigate
    )

    # Очистка сообщений
    try:
        for i in range(msg.message_id, 0, -1):
            await dp.bot.delete_message(msg.from_user.id, i)
    except: ...

    user = User(
        user_name=data['user_name'],
        user_phone=str(data['user_phone']),
        user_tg_id=str(data['user_tg_id'])
    )
    session.add(user)
    session.commit()
    session.close()
