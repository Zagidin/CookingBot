from bot.bot import dp
from base.base import SessionLocal
from base.models import Product, Basket
from aiogram.types import CallbackQuery


@dp.callback_query_handler(lambda c: c.data.startswith("add_basket_product:"))
async def user_basket(callback: CallbackQuery):
    """
        Сделать проверку, Если Товар уже был добавлен в корзину,
            то выводить сообщение о том, что товар уже существует в корзине

        Пример использования: файлы добавления продукта, проверка на существовании категории

        🚩 УДАЛИТЬ СООБЩЕНИЕ В main.py ПОСЛЕ ИСПРАВЛЕНИЯ 🚩
    """

    session = SessionLocal()

    try:
        product_id = int(callback.data.split(":")[1])

        product = session.query(Product).filter(
            Product.id == product_id
        ).one_or_none()

        if product:
            new_product_in_basket = Basket(
                user_id=callback.from_user.id,
                product_id=product.id,
                quantity=1
            )
            session.add(new_product_in_basket)
            session.commit()
            session.close()
    except:
        await callback.message.answer("Ошибка при добавления товара в Корзину 🚩")

    await callback.message.delete()
