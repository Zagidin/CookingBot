from bot.bot import dp
from base.base import SessionLocal
from aiogram.types import InputFile
from aiogram.types import CallbackQuery
from base.models import Category, Product
from keyboard.admin.inline.navigate_admin_home import home_nav_admin
from keyboard.admin.inline.delete_product_in_category import delete_product_id_generate


@dp.callback_query_handler(text="delete_category_product_sweet")
async def delete_product_flour(callback: CallbackQuery):
    # Очистка сообщений
    try:
        for i in range(callback.message.message_id, 0, -1):
            await dp.bot.delete_message(callback.message.from_user.id, i)
    except:
        ...

    session = SessionLocal()

    products_sweet = (
        session.query(
            Product.id,
            Product.name,
            Product.description,
            Product.price,
            Product.photo
        )
        .join(Category)
        .filter(Category.name == "Сладкое")
        .all()
    )

    if not products_sweet:

        await callback.bot.delete_message(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id
        )

        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            text="Список Товаров пуст ❌"
        )

        session.close()
    else:

        await callback.bot.delete_message(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id
        )

        await callback.bot.send_message(
            callback.from_user.id,
            text="⚡ СЛАДКИЙ ОТДЕЛ ⚡"
        )

        await callback.answer(text="⚡ СЛАДКИЙ ОТДЕЛ ⚡")

        for product in products_sweet:
            open_photo_product_flour = f"{product[4]}"

            try:
                photo_sweet_product = InputFile(open_photo_product_flour)
                await callback.bot.send_photo(
                    callback.from_user.id,
                    photo=photo_sweet_product,
                    caption=f"🥐 Название продукта: {product[1]}\n"
                            f"\nОписание:\n\n"
                            f" {product[2]}\n\n"
                            f" 💰 Цена: {product[3]}",
                    reply_markup=delete_product_id_generate(product[0])
                )
            except:
                await callback.bot.send_message(
                    callback.from_user.id,
                    text=f"Название продукта: {product[0]}\n"
                         f"\nОписание:\n"
                         f"{product[1]}\n\n"
                         f"Цена: {product[2]}\n\n"
                         f"❌ Фото недоступно"
                )

        await callback.message.answer(
            text="⚡ Навигация Администратора ⚡",
            reply_markup=home_nav_admin
        )
