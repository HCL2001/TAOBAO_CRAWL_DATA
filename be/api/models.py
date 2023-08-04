from sqlalchemy import Column, Integer, String, Text ,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SearchProduct(Base):
    __tablename__ = "search_product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(1020))
    price = Column(String(50))
    link = Column(Text)  # Sử dụng cột TEXT cho các URL dài
    image = Column(String(1020))

    # def __str__(self):
    #     return f"SearchProduct(id={self.id}, name={self.name}, price={self.price}, image={self.image})"

# class Detail(Base):
#     __tablename__ = "detail"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     price = Column(String)
#     link = Column(String)
#     promotion = Column(String)


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    token = Column(String(10000))

class Detail(Base):
    __tablename__ = "detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(1020))
    price = Column(String(20))
    link = Column(Text)
    promotion = Column(String(50))
    product_name = Column(String(1020))
