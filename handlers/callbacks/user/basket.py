from bot.bot import dp
from aiogram.types import CallbackQuery
from keyboard.user.inline.home_navigate import home_navigate_user


@dp.callback_query_handler(text="basket")
async def basket(callback: CallbackQuery):

    await callback.message.edit_text(text="🛒")
    await callback.bot.send_message(
        chat_id=callback.from_user.id,
        text="⚡ Корзина Товаров ⚡",
        parse_mode="HTML",
        reply_markup=home_navigate_user
    )

    # Очистка всех предыдущих сообщений бота
    try:
        for message_id in range(callback.message.message_id - 1, 0, -1):
            try:
                await callback.bot.delete_message(
                    chat_id=callback.from_user.id,
                    message_id=message_id
                )
            except Exception:
                pass
    except Exception as e:
        print(f"Ошибка при очистке сообщений: {e}")
