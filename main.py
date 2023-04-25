import psycopg2
import sqlalchemy, json

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from list_def import create_db, delete_table
from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN='postgresql://postgres:qwer3@localhost:5432/netology_db' # переменная для подключения к БД
engine=sqlalchemy.create_engine(DSN) # создание переменной для движка

create_tables(engine)
Session=sessionmaker(bind=engine) # создание сессии

session=Session()
with open('data.json', 'r') as fd:
    data = json.load(fd)
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
            }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


session.close