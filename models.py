# models.py

from sqlmodel import SQLModel, Field
from typing import Optional


# TABLA USUARIOS
class Usuario(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: str
    edad: int
    ciudad: str


# TABLA MOTOS
class Moto(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    modelo: str
    marca: str
    cilindraje: int
    color: str
    precio: float

    # Relación simple con usuario
    usuario_id: int