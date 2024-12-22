from bot.bot import dp
from base.base import SessionLocal
from aiogram.types import InputFile
from aiogram.types import CallbackQuery
from base.models import Category, Product


@dp.callback_query_handler(text="tvorog")
async def menu_category_flour(callback: CallbackQuery):

    session = SessionLocal()

    products_tvg = (
        session.query(
            Product.name,
            Product.description,
            Product.price,
            Product.photo
        )
        .join(Category)
        .filter(Category.name == "Творожное")
        .all()
    )

    if not products_tvg:
        await callback.bot.send_message(
            callback.from_user.id,
            "Список Товаров пуст ❌\n\n"
                 "🤖 Владелец пока не добавил ни одного товара 🚩"
        )

        session.close()
    else:
        await callback.bot.send_message(
            chat_id=callback.from_user.id,
            text="⚡ СЛАДКИЙ ОТДЕЛ ⚡"
        )

        await callback.answer("⚡ СЛАДКИЙ ОТДЕЛ ⚡")

        for product in products_tvg:
            open_photo_product_flour = f"{product[3]}"

            try:
                photo_sweet_product = InputFile(open_photo_product_flour)
                await callback.bot.send_photo(
                    callback.from_user.id,
                    photo=photo_sweet_product,
                    caption=f"🥧 Название продукта: {product[0]}\n"
                            f"\nОписание:\n\n"
                            f" {product[1]}\n\n"
                            f" 💰 Цена: {product[2]}"
                )
            except Exception as e:
                await callback.bot.send_message(f"Ошибка отправки фото: {e}")
                await callback.bot.send_message(
                    callback.from_user.id,
                    text=f"Название продукта: {product[0]}\n"
                         f"\nОписание:\n"
                         f"{product[1]}\n\n"
                         f"Цена: {product[2]}\n\n"
                         f"❌ Фото недоступно"
                )