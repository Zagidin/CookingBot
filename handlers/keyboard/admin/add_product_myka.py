import os
from bot.bot import dp
from base.base import SessionLocal
from base.models import Category, Product
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboard.admin.inline.navigate_admin_home import home_nav_admin
from status_machine.admin.add_new_product_flour import AddNewProductFlour


@dp.message_handler(text="Мучное 🍞")
async def add_new_product_myk_category(msg: Message):
    await msg.answer(
        text="⚡ Добавление нового товара ⚡\n\nКатегория <b>Мука</b> 🍞"
             "\n\nВведите название продукта ✍",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove()
    )

    await AddNewProductFlour.name.set()


@dp.message_handler(state=AddNewProductFlour.name)
async def name_product(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['name_product_flour'] = msg.text

    await msg.answer(
        text="Теперь введите Описание Этого товара\n"
             "\n 🤖 Дайте краткое описание об этом товаре\n"
             "\nНапример: "
             "\n***** Производитель *****"
             "\n***** Дата изготовления *****"
             "\n***** Срок хранения *****"
             "\nСостав и другое"
    )

    await AddNewProductFlour.description.set()


@dp.message_handler(state=AddNewProductFlour.description)
async def description_product(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['description_product_flour'] = msg.text

    await msg.answer(
        text="Введите теперь цену товара 💰\n\nНапример -> 10.00 "
    )

    await AddNewProductFlour.price.set()


@dp.message_handler(state=AddNewProductFlour.price)
async def price_product(msg: Message, state: FSMContext):

    async with state.proxy() as data:
        data['price_product_flour'] = msg.text

    await msg.answer(
        text="Теперь отправьте Фото товара 📸"
    )

    await AddNewProductFlour.url_photo.set()


@dp.message_handler(state=AddNewProductFlour.url_photo, content_types=['photo'])
async def url_photo_product_flour(msg: Message, state: FSMContext):

    session = SessionLocal()

    category = session.query(Category).filter_by(name='Мука').first()

    if not category:
        category = Category(
            name="Мука"
        )
        session.add(category)
        session.commit()

    img_flour_save_url = 'img/img_product/flour'
    os.makedirs(img_flour_save_url, exist_ok=True)

    photo_flour_url = f"{img_flour_save_url}/{msg.photo[-1].file_id}.png"
    await msg.photo[-1].download(destination_file=photo_flour_url)

    async with state.proxy() as data:
        data['url_photo_product_flour'] = photo_flour_url

    await state.finish()

    new_product = Product(
        name=data['name_product_flour'],
        description=data['description_product_flour'],
        price=data['price_product_flour'],
        photo=data['url_photo_product_flour'],
        category_id=category.id
    )
    session.add(new_product)
    session.commit()
    session.close()

    await msg.answer(
        text="⚡ Добавлен Новый товар ⚡\n"
             "\nУспешно Добавлено ✅\n"
             "Товар с Категорией -> Мука 🍞",
        reply_markup=home_nav_admin
    )

    # Очистка сообщений
    try:
        for i in range(msg.message_id, 0, -1):
            await dp.bot.delete_message(msg.from_user.id, i)
    except: ...