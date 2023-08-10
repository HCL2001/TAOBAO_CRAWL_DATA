from sqlalchemy import Column, Integer, String, Text ,DateTime
from sqlalchemy.ext.declarative import declarative_base

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
    n_id = Column(Integer)
    name = Column(String(1020))
    product_url = Column(String(5000))
    main_imgs = Column(Text)
    product_props = Column(Text)
    sku_props = Column(Text)
    skus = Column(Text)
