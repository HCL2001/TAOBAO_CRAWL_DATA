from sqlalchemy import Column, Integer, String, Text ,DateTime, TIMESTAMP, DECIMAL, ForeignKey, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class SearchProduct(Base):
    __tablename__ = "search_product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String(255))
    name = Column(String(1020))
    price = Column(String(50))
    shopName = Column(String(255))
    link = Column(Text)  # Sử dụng cột TEXT cho các URL dài
    image = Column(String(1020))


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    token = Column(String(10000))

class Detail(Base):
    __tablename__ = "detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    n_id = Column(Double)
    name = Column(String(1020))
    product_url = Column(String(5000))
    main_imgs = Column(Text)
    product_props = Column(Text)
    sku_props = Column(Text)
    skus = Column(Text)

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    created_at = Column(TIMESTAMP, server_default="2023-08-10 00:00:00")
    total_price = Column(DECIMAL(10, 2))
    cart_items = relationship("CartItem", back_populates="cart")

class CartItem(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    n_id = Column(Double)
    name = Column(String(1020))
    price = Column(Integer)
    quantity = Column(Integer)
    total_price = Column(DECIMAL(10, 2))
    cart = relationship("Cart", back_populates="cart_items")
