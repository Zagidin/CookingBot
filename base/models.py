from os import getenv
from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    create_engine
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

engine = create_engine(getenv("DATABASE_URL"))

Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    admin_name = Column(String, nullable=False)
    admin_phone = Column(String, nullable=False)
    admin_tg_id = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    user_phone = Column(String, nullable=True)
    user_tg_id = Column(String, nullable=False)

    baskets = relationship("Basket", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    photo = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    category = relationship("Category", back_populates="products")
    baskets = relationship("Basket", back_populates="product")


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", back_populates="category")


class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, default=1)

    user = relationship("User", back_populates="baskets")
    product = relationship("Product", back_populates="baskets")


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    delivery_type = Column(String, nullable=False)
    address = Column(String, nullable=True, default="Самовывоз")
    delivery_time = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="Готовится")  # 'Готовится', 'Готов', 'Едет к вам'

    user = relationship("User", back_populates="orders")