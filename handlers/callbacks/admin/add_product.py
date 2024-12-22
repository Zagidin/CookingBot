from bot.bot import dp
from aiogram.types import CallbackQuery
from keyboard.admin.reply.category_product import category_product


@dp.callback_query_handler(text="add_new_product")
async def add_new_product(callback: CallbackQuery):

    await callback.answer(
        text="⚡⚡ Добавление нового продукта ⚡⚡"
    )

    await callback.bot.send_message(
        callback.from_user.id,
        text="⚡ Добавление нового товара ⚡\n"
             "\nВыберите категорию товара 👇",
        reply_markup=category_product
    )
