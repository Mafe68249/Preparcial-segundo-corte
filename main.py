from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from database import create_tables, get_session
from models import Moto, Usuario

app = FastAPI()

# CREAR TABLAS MANUALMENTE
create_tables()


# RUTA PRINCIPAL
@app.get("/")
def inicio():
    return {"mensaje": "API de motos funcionando correctamente"}


# =========================
# CRUD USUARIOS
# =========================

@app.post("/usuarios/")
def crear_usuario(
    usuario: Usuario,
    session: Session = Depends(get_session)
):

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario


@app.get("/usuarios/")
def ver_usuarios(
    session: Session = Depends(get_session)
):

    usuarios = session.exec(select(Usuario)).all()

    return usuarios


@app.get("/usuarios/{id}")
def ver_usuario(
    id: int,
    session: Session = Depends(get_session)
):

    usuario = session.get(Usuario, id)

    if not usuario:
        return {"mensaje": "Usuario no encontrado"}

    return usuario


# =========================
# CRUD MOTOS
# =========================

@app.post("/motos/")
def crear_moto(
    moto: Moto,
    session: Session = Depends(get_session)
):

    session.add(moto)
    session.commit()
    session.refresh(moto)

    return moto


@app.get("/motos/")
def ver_motos(
    session: Session = Depends(get_session)
):

    motos = session.exec(select(Moto)).all()

    return motos


@app.get("/motos/{id}")
def ver_moto(
    id: int,
    session: Session = Depends(get_session)
):

    moto = session.get(Moto, id)

    if not moto:
        return {"mensaje": "Moto no encontrada"}

    return moto


@app.put("/motos/{id}")
def actualizar_moto(
    id: int,
    datos: Moto,
    session: Session = Depends(get_session)
):

    moto = session.get(Moto, id)

    if not moto:
        return {"mensaje": "Moto no encontrada"}

    moto.modelo = datos.modelo
    moto.marca = datos.marca
    moto.cilindraje = datos.cilindraje
    moto.color = datos.color
    moto.precio = datos.precio
    moto.usuario_id = datos.usuario_id

    session.add(moto)
    session.commit()
    session.refresh(moto)

    return moto


@app.delete("/motos/{id}")
def eliminar_moto(
    id: int,
    session: Session = Depends(get_session)
):

    moto = session.get(Moto, id)

    if not moto:
        return {"mensaje": "Moto no encontrada"}

    session.delete(moto)
    session.commit()

    return {"mensaje": "Moto eliminada correctamente"}