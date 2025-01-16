from bot.bot import dp
from aiogram.types import CallbackQuery
from keyboard.user.inline.home_navigate import home_navigate_user


@dp.callback_query_handler(text="basket")
async def basket(callback: CallbackQuery):
    logo_basket = open("img/basket_logo.png", "rb")

    await callback.bot.send_photo(
        chat_id=callback.from_user.id,
        photo=logo_basket,
        caption="⚡ Корзина Товаров ⚡\n\n<i>Вернуться на главную</i> - /<b>nav</b> \n"
                "<i>или пропишите</i> /<b>навигация</b>",
        parse_mode="HTML",
        reply_markup=home_navigate_user
    )
