from bot.bot import dp
from base.base import SessionLocal
from aiogram.types import CallbackQuery
from base.models import Product, Basket, User


@dp.callback_query_handler(lambda c: c.data.startswith("add_basket_product:"))
async def user_basket(callback: CallbackQuery):

    session = SessionLocal()

    try:
        product_id = int(callback.data.split(":")[1])

        product = session.query(Product).filter(Product.id == product_id).one_or_none()

        user = (
            session.query(User.id, User.user_tg_id)
            .filter(User.user_tg_id == callback.from_user.id)
            .one_or_none()
        )

        if product:
            existing_basket_item = (
                session.query(Basket)
                .filter(Basket.user_id == user.id, Basket.product_id == product.id)
                .one_or_none()
            )

            if existing_basket_item:
                await callback.message.answer("🚩 Этот товар есть в корзине 🛒")
                session.close()
            else:
                new_product_in_basket = Basket(
                    user_id=user.id, product_id=product.id, quantity=1
                )
                session.add(new_product_in_basket)
                session.commit()
                session.close()

                await callback.message.answer("✅ Товар добавлен в корзину 🛒")
    except:
        await callback.message.answer("Ошибка при добавления товара в Корзину 🚩")

    await callback.message.delete()
