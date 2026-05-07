# database.py
import os
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# URL de conexión de Neon
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear conexión con PostgreSQL Neon
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Crear tablas automáticamente
def create_tables():
    SQLModel.metadata.create_all(engine)

# Crear sesiones para operaciones CRUD
def get_session():
    with Session(engine) as session:
        yield session