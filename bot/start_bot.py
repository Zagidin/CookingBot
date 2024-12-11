from bot.bot import dp
from aiogram import executor


def start_bot():
    print("Бот-Старт: -> ", end='')
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )
    print("Бот-Стоп")
