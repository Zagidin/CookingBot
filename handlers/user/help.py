from bot.bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['help', 'помощь'])
async def help_bot(msg: Message):

    # bot_logo_photo = open("img/main_home_help_info_bot.png")

    await msg.answer(
        text="Телеграм Бот - Онлайн Пекарня -< ZAGA >-\n\n"
                "⚡ Функционал Бота ⚡\n\t"
                "‣ Заказ и Просмотр товаров Пекарни 🔎"
                "\n\n⚡ Команды ⚡\n"
                "/nav\n/навигация - Главное 🏠\n\n"
                "/profile\n/профиль - Профиль 👤\n\n"
                "/support\n/поддержка - Поддержка 🛠"
    )
