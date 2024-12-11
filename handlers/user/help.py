from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['help', 'помощь'])
async def help_bot(msg: Message):
    await msg.answer(
        text='Help Bot 👏'
    )
