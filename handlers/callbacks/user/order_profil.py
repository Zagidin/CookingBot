from bot.bot import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="order")
async def user_order(callback: CallbackQuery):
    await callback.message.answer(text="В РАЗРАБОТКЕ!")
