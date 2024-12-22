import os
from bot.bot import dp
from base.base import SessionLocal
from base.models import Category, Product
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboard.admin.inline.navigate_admin_home import home_nav_admin
from status_machine.admin.add_new_product_sweet import AddNewProductSweet


@dp.message_handler(text="Сладкое 🥐")
async def add_new_product_sld_category(msg: Message):
    await msg.answer(
        text="⚡ Добавление нового товара ⚡\n\nКатегория <b>Сладкое</b> 🥐"
             "\n\nВведите название продукта ✍",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

    await AddNewProductSweet.name.set()


@dp.message_handler(state=AddNewProductSweet.name)
async def name_product_sweet(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['name_product_sweet'] = msg.text

    await msg.answer(
        text="Теперь введите Описание Этого товара\n"
             "\n 🤖 Дайте краткое описание об этом товаре\n"
             "\nНапример: "
             "\n***** Производитель *****"
             "\n***** Дата изготовления *****"
             "\n***** Срок хранения *****"
             "\nСостав и другое"
    )

    await AddNewProductSweet.description.set()


@dp.message_handler(state=AddNewProductSweet.description)
async def description_product_sweet(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['description_product_sweet'] = msg.text

    await msg.answer(
        text="Введите теперь цену товара 💰\n\nНапример -> 10.00 "
    )

    await AddNewProductSweet.price.set()


@dp.message_handler(state=AddNewProductSweet.price)
async def price_product_sweet(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['price_product_sweet'] = msg.text

    await msg.answer(
        text="Теперь отправьте Фото товара 📸"
    )

    await AddNewProductSweet.url_photo.set()


@dp.message_handler(state=AddNewProductSweet.url_photo, content_types=['photo'])
async def url_photo_product_sweet(msg: Message, state: FSMContext):

    session = SessionLocal()

    category = session.query(Category.id).filter_by(name='Сладкое').first()

    if not category:
        category = Category(
            name="Сладкое"
        )
        session.add(category)
        session.commit()

    img_sweet_save_url = 'img/img_product/sweet'
    os.makedirs(img_sweet_save_url, exist_ok=True)

    photo_sweet_url = f"{img_sweet_save_url}/{msg.photo[-1].file_id}.png"
    await msg.photo[-1].download(destination_file=photo_sweet_url)

    async with state.proxy() as data:
        data['url_photo_product_sweet'] = photo_sweet_url

    await state.finish()

    new_product = Product(
        name=data['name_product_sweet'],
        description=data['description_product_sweet'],
        price=data['price_product_sweet'],
        photo=data['url_photo_product_sweet'],
        category_id=category.id
    )
    session.add(new_product)
    session.commit()
    session.close()

    await msg.answer(
        text="⚡ Добавлен Новый товар ⚡\n"
             "\nУспешно Добавлено ✅\n"
             "Товар с Категорией -> Сладкое 🥐",
        reply_markup=home_nav_admin
    )

    # Очистка сообщений
    try:
        for i in range(msg.message_id, 0, -1):
            await dp.bot.delete_message(msg.from_user.id, i)
    except: ...