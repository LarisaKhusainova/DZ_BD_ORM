import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base=declarative_base() # создание базового класса

class Publisher(Base):
    __tablename__="publisher"

    id=sq.Column(sq.Integer, primary_key=True)
    name=sq.Column(sq.String(length=40))

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40))
    id_publisher=sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher= relationship(Publisher,backref='book')

class Shop(Base):
    __tablename__="shop"

    id=sq.Column(sq.Integer, primary_key=True)
    name=sq.Column(sq.String(length=40))

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.Integer)
    id_book=sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    book= relationship(Book,backref='stock')
    shop = relationship(Shop, backref='stock')

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale=sq.Column(sq.Date)
    count=sq.Column(sq.Integer)
    id_stock=sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)

    stock= relationship(Stock,backref='sale')


def create_tables(engine):
    Base.metadata.create_all(engine)



