from bot.bot import dp
from base.base import SessionLocal
from aiogram.types import InputFile
from aiogram.types import CallbackQuery
from base.models import Category, Product
from keyboard.user.inline.korzina import add_product_basket_generate
from keyboard.user.inline.home_navigate import home_navigate_user



@dp.callback_query_handler(text="sladkoe")
async def menu_category_flour(callback: CallbackQuery):

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
            text="Список Товаров пуст ❌\n\n"
                 "🤖 Владелец пока не добавил ни одного товара 🚩",
            reply_markup=home_navigate_user
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
                            f" 💰 Цена: {product[3]} ₽",
                    reply_markup=add_product_basket_generate(product[0])
                )
            except Exception as e:
                print(f"Ошибка отправки фото: {e}")
                await callback.bot.send_message(
                    callback.from_user.id,
                    text=f"Название продукта: {product[0]}\n"
                         f"\nОписание:\n"
                         f"{product[1]}\n\n"
                         f"Цена: {product[2]}\n\n"
                         f"❌ Фото недоступно"
                )

        await callback.message.answer(text="⚡ Навигация ⚡", reply_markup=home_navigate_user)