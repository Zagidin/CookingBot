import os
from bot.bot import dp
from base.base import SessionLocal
from base.models import Category, Product
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboard.admin.inline.navigate_admin_home import home_nav_admin
from status_machine.admin.add_new_product_tvorog import AddNewProductTvorog


@dp.message_handler(text="Творожное 🥧")
async def add_new_product_tvg_category(msg: Message):
    await msg.answer(
        text="⚡ Добавление нового товара ⚡\n\nКатегория <b>Творожное</b> 🥧"
        "\n\nВведите название продукта ✍",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove(),
    )

    await AddNewProductTvorog.name.set()


@dp.message_handler(state=AddNewProductTvorog.name)
async def name_product_tvg(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data["name_product_tvg"] = msg.text

    await msg.answer(
        text="Теперь введите Описание Этого товара\n"
        "\n 🤖 Дайте краткое описание об этом товаре\n"
        "\nНапример: "
        "\n***** Производитель *****"
        "\n***** Дата изготовления *****"
        "\n***** Срок хранения *****"
        "\nСостав и другое"
    )

    await AddNewProductTvorog.description.set()


@dp.message_handler(state=AddNewProductTvorog.description)
async def description_product_tvg(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data["description_product_tvg"] = msg.text

    await msg.answer(text="Введите теперь цену товара 💰\n\nНапример -> 10.00 ")

    await AddNewProductTvorog.price.set()


@dp.message_handler(state=AddNewProductTvorog.price)
async def price_product_tvg(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data["price_product_tvg"] = msg.text

    await msg.answer(text="Теперь отправьте Фото товара 📸")

    await AddNewProductTvorog.url_photo.set()


@dp.message_handler(state=AddNewProductTvorog.url_photo, content_types=["photo"])
async def url_photo_product_tvg(msg: Message, state: FSMContext):

    session = SessionLocal()

    category = session.query(Category.id).filter_by(name="Творожное").first()

    if not category:
        category = Category(name="Творожное")
        session.add(category)
        session.commit()

    img_tvg_save_url = "img/img_product/cottage_cheese"
    os.makedirs(img_tvg_save_url, exist_ok=True)

    photo_sweet_url = f"{img_tvg_save_url}/{msg.photo[-1].file_id}.png"
    await msg.photo[-1].download(destination_file=photo_sweet_url)

    async with state.proxy() as data:
        data["url_photo_product_tvg"] = photo_sweet_url

    await state.finish()

    new_product = Product(
        name=data["name_product_tvg"],
        description=data["description_product_tvg"],
        price=data["price_product_tvg"],
        photo=data["url_photo_product_tvg"],
        category_id=category.id,
    )
    session.add(new_product)
    session.commit()
    session.close()

    await msg.answer(
        text="⚡ Добавлен Новый товар ⚡\n"
        "\nУспешно Добавлено ✅\n"
        "Товар с Категорией -> Творожное 🥧",
        reply_markup=home_nav_admin,
    )

    # Очистка сообщений
    try:
        for i in range(msg.message_id, 0, -1):
            await dp.bot.delete_message(msg.from_user.id, i)
    except:
        ...
