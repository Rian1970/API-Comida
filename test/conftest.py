import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src.models.cliente import Cliente

# Base de datos de prueba en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """ Crea una base de datos en memoria para pruebas. """
    Base.metadata.create_all(bind=engine)  # Crea las tablas
    db = TestingSessionLocal()
    yield db  # Devuelve la sesión de la BD para la prueba
    db.rollback()  # Limpia la BD después de la prueba
    db.close()
    Base.metadata.drop_all(bind=engine)  # Borra todas las tablas después de cada test
