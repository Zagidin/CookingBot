from keyboard.admin.inline.navigate_admin_home import home_nav_admin
from keyboard.admin.inline.log_in_passwd import passwd_start
from status_machine.admin.log_in_password import ValidPasswd
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from aiogram.types import (
    CallbackQuery,
    Message
)
from bot.bot import dp
from os import getenv


load_dotenv()


@dp.callback_query_handler(text="log_in_password")
async def log_in_admin_panel_passwd(callback: CallbackQuery):
    await callback.answer(
        text="Введите Пароль, который Выдал Администратор"
    )
    await callback.bot.send_message(callback.from_user.id, text="Введите пароль 🚩")

    await ValidPasswd.password.set()


@dp.message_handler(state=ValidPasswd.password)
async def valid_password(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['admin_password_usr'] = msg.text

    await state.finish()

    if data['admin_password_usr'] == getenv("ADMIN_PASSWORD"):
        await msg.answer("✅")
        await msg.answer(
            text="Вы успешно вошли в роли Администратора!\n\n"
                 "Доступные Функции 🧰",
            reply_markup=home_nav_admin
        )
    else:
        await msg.answer("❌")
        await msg.answer(text="<b>Не верный пароль</b>", parse_mode="HTML")
        await msg.answer(
            text="У Вас нет прав к Доступу Админ панели! ❌\n\n"
                 "Попробуйте Войти ПАРОЛЕМ - <i>Выдаётся Администратором</i>\n\n"
                 "Если возникнут проблемы со входом, пожалуйста обратитесь к Администратору за паролем 🗝🔓",
            parse_mode='HTML',
            reply_markup=passwd_start
        )
