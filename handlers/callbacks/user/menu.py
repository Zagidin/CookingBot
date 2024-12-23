from bot.bot import dp
from aiogram.types import CallbackQuery
from aiogram.types import InputMediaPhoto
from keyboard.user.inline.menu_navigation import manu_nav


@dp.callback_query_handler(text="look_menu")
async def look_menu(callback: CallbackQuery):

    logo_menu = open("img/menu_logo.png", "rb")

    await callback.bot.edit_message_media(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media=logo_menu,
            caption=(
                "⚡ Меню Товаров ⚡\n\n"
                "<i>Вернуться на главную</i> - /<b>nav</b> \n"
                "<i>или пропишите</i> /<b>навигация</b>"
            ),
            parse_mode="HTML"
        ),
        reply_markup=manu_nav
    )