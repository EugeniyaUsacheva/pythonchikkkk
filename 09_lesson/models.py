from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_deleted = Column(Boolean, default=False)


# Функция для создания подключения к БД
def get_engine(user, password, host='localhost', port=5432, database='mydatabase'):
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')


# Функция для создания сессии
def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
