from os import remove
from bot.bot import dp
from base.models import Product
from sqlalchemy.orm import Session
from base.base import SessionLocal
from sqlalchemy.exc import NoResultFound
from aiogram.types import CallbackQuery


@dp.callback_query_handler(lambda c: c.data.startswith("delete_product_in_category:"))
async def delete_product(call: CallbackQuery):
    """
        🚩 Чтобы удалялся товар, нужно прописать проверку,
            существует ли этот товар в корзине,
                Если Истина, то удалить товар с Корзины и уже Потом с БД -> Продукта 🚩

        🚩 УДАЛИТЬ СООБЩЕНИЕ В main.py ПОСЛЕ ИСПРАВЛЕНИЯ 🚩
    """

    session: Session = SessionLocal()

    try:
        product_id = int(call.data.split(":")[1])

        product = session.query(Product).filter(
            Product.id == product_id
        ).one_or_none()

        remove(product.photo)

        if product:
            session.delete(product)
            session.commit()
            await call.message.answer("✅")
            await call.message.answer(f"Товар успешно удалён ✅")

        else:
            await call.message.answer(f"Товар с ID {product_id} не найден.")
    except NoResultFound:
        await call.message.answer(f"Товар не найден.")
    except Exception as e:
        await call.message.answer(f"Произошла ошибка: {e}")
        session.rollback()
    finally:
        session.close()

    await call.message.delete()
