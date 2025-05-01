import pytest
from models import get_engine, get_session, Student

# Замените эти значения на свои данные для подключения к БД
DB_USER = 'postgres'
DB_PASSWORD = 'India2022'
DB_NAME = 'mydatabase'


@pytest.fixture(scope='module')
def setup_database():
    engine = get_engine(DB_USER, DB_PASSWORD)
    # Создаем таблицы в БД
    Student.__table__.create(bind=engine)

    yield engine  # Возвращаем объект engine для использования в тестах

    # Удаляем таблицы после завершения тестов
    Student.__table__.drop(bind=engine)


@pytest.fixture(scope='function')
def session(setup_database):
    session = get_session(setup_database)

    yield session  # Возвращаем сессию для использования в тестах

    session.rollback()  # Откатываем изменения после каждого теста
    session.close()  # Закрываем сессию


def test_add_student(session):
    new_student = Student(name='John Doe')
    session.add(new_student)
    session.commit()

    assert new_student.id is not None  # Проверяем, что студент был добавлен


def test_update_student(session):
    student = session.query(Student).filter_by(name='John Doe').first()

    student.name = 'Jane Doe'
    session.commit()

    updated_student = session.query(Student).filter_by(id=student.id).first()

    assert updated_student.name == 'Jane Doe'  # Проверяем обновление имени


def test_soft_delete_student(session):
    student = session.query(Student).filter_by(name='Jane Doe').first()

    student.is_deleted = True  # Помечаем студента как удалённого
    session.commit()

    deleted_student = session.query(Student).filter_by(id=student.id).first()

    assert deleted_student.is_deleted is True  # Проверяем мягкое удаление
