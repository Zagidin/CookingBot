from bot.bot import dp
from aiogram.types import (
    Message,
    ContentType,
    ReplyKeyboardRemove
)
from base.models import Admin
from base.base import SessionLocal
from aiogram.dispatcher import FSMContext
from keyboard.user.reply.phone import phone
from keyboard.admin.inline.log_in_passwd import passwd_start
from keyboard.admin.inline.navigate_admin_home import home_nav_admin
from status_machine.admin.registration_admin import RegistrationAdmin


@dp.message_handler(commands=["admin", "админ"])
async def admin_start_registration(msg: Message):

    session = SessionLocal()

    admin = session.query(Admin).all()

    if not admin:
        await msg.answer(
            text=f"👋 @{msg.from_user.username}\n"
                 f"\nДля Входа в Административную часть, Вам необходимо Зарегистрироваться ✍"
        )
        await msg.answer(text="Введите Ваше имя 🚩")

        await RegistrationAdmin.admin_name.set()
    else:
        admin = [admin_tg_id[0] for admin_tg_id in session.query(Admin.admin_tg_id).all()]
        if msg.from_user.id in admin:
            await msg.answer("👋", reply_markup=ReplyKeyboardRemove())
            await msg.answer(
                text="Панель Администратора\n\nДоступные Функции 🧰",
                reply_markup=home_nav_admin
            )
        else:
            await msg.answer("❌")
            await msg.answer(
                text="У Вас нет прав к Доступу Админ панели! ❌\n\n"
                     "Попробуйте Войти ПАРОЛЕМ - <i>Выдаётся Администратором</i>",
                parse_mode='HTML',
                reply_markup=passwd_start
            )


@dp.message_handler(state=RegistrationAdmin.admin_name)
async def reg_admin_name(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data["admin_name"] = msg.text

    await msg.answer(
        text="Теперь поделитесь Вашим номером телефона 📱",
        reply_markup=phone
    )

    await RegistrationAdmin.admin_phone.set()


@dp.message_handler(state=RegistrationAdmin.admin_phone, content_types=ContentType.CONTACT)
async def reg_admin_phone_and_id(msg: Message, state: FSMContext):
    session = SessionLocal()

    async with state.proxy() as data:
        data["admin_phone"] = msg.contact.phone_number

    async with state.proxy() as data:
        data["admin_tg_id"] = msg.from_user.id

    await state.finish()

    admin = Admin(
        admin_name=data['admin_name'],
        admin_phone=str(data['admin_phone']),
        admin_tg_id=data['admin_tg_id'],
    )
    session.add(admin)
    session.commit()

    await msg.answer("✅")
    await msg.answer(
        text="Вы успешно зарегистрировались в роли Администратора!\n\n"
             "Доступные Функции 🧰",
        reply_markup=home_nav_admin
    )

    # Очистка сообщений
    try:
        for i in range(msg.message_id, 0, -1):
            await dp.bot.delete_message(msg.from_user.id, i)
    except: ...
