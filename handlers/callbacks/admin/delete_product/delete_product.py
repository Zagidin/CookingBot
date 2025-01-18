from os import remove
from bot.bot import dp
from base.base import SessionLocal
from base.models import Product, Basket
from aiogram.types import CallbackQuery
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session


@dp.callback_query_handler(lambda c: c.data.startswith("delete_product_in_category:"))
async def delete_product(call: CallbackQuery):

    session: Session = SessionLocal()

    try:
        id_product = int(call.data.split(":")[1])

        product = session.query(Product).filter(
            Product.id == id_product
        ).one_or_none()

        remove(product.photo)

        if product:
            session.query(Basket).filter(
                Basket.product_id == id_product
            ).delete()

            session.delete(product)
            session.commit()

            await call.message.answer("✅")
            await call.message.answer(f"Товар успешно удалён ✅")

        else:
            await call.message.answer(f"Товар с ID {id_product} не найден.")
    except NoResultFound:
        await call.message.answer(f"Товар не найден.")
    except Exception as e:
        await call.message.answer(f"Произошла ошибка: {e}")
        session.rollback()
    finally:
        session.close()

    await call.message.delete()
