from sqlmodel import SQLModel, Field
from typing import Optional


class Usuario(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: str
    edad: int
    ciudad: str



class Moto(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    modelo: str
    marca: str
    cilindraje: int
    color: str
    precio: float
    activo: bool = True

    usuario_id: int


class MotoUpdate(SQLModel):

    modelo: Optional[str] = None
    marca: Optional[str] = None
    cilindraje: Optional[int] = None
    color: Optional[str] = None
    precio: Optional[float] = None
    usuario_id: Optional[int] = None