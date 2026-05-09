from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session

from database import create_tables, get_session
from models import Moto, Usuario, MotoUpdate

import operations

app = FastAPI()


create_tables()



@app.get("/")
def inicio():

    return {
        "mensaje": "API de motos funcionando correctamente"
    }



@app.post("/usuarios/")
def crear_usuario(
    usuario: Usuario,
    session: Session = Depends(get_session)
):

    return operations.crear_usuario(
        session,
        usuario
    )


@app.get("/usuarios/")
def ver_usuarios(
    session: Session = Depends(get_session)
):

    return operations.obtener_usuarios(session)


@app.get("/usuarios/{id}")
def ver_usuario(
    id: int,
    session: Session = Depends(get_session)
):

    usuario = operations.obtener_usuario_por_id(
        session,
        id
    )

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario



@app.post("/motos/")
def crear_moto(
    moto: Moto,
    session: Session = Depends(get_session)
):

    return operations.crear_moto(
        session,
        moto
    )


@app.get("/motos/")
def ver_motos(
    session: Session = Depends(get_session)
):

    return operations.obtener_motos(session)


@app.get("/motos/{id}")
def ver_moto(
    id: int,
    session: Session = Depends(get_session)
):

    moto = operations.obtener_moto_por_id(
        session,
        id
    )

    if not moto:
        raise HTTPException(
            status_code=404,
            detail="Moto no encontrada"
        )

    return moto



@app.patch("/motos/{id}")
def modificar_parcial_moto(
    id: int,
    datos: MotoUpdate,
    session: Session = Depends(get_session)
):

    moto = operations.obtener_moto_por_id(
        session,
        id
    )

    if not moto:
        raise HTTPException(
            status_code=404,
            detail="Moto no encontrada"
        )

    datos_actualizados = datos.dict(
        exclude_unset=True
    )

    return operations.actualizar_moto(
        session,
        moto,
        datos_actualizados
    )



@app.delete("/motos/{id}")
def eliminar_moto(
    id: int,
    session: Session = Depends(get_session)
):

    moto = operations.obtener_moto_por_id(
        session,
        id
    )

    if not moto:
        raise HTTPException(
            status_code=404,
            detail="Moto no encontrada"
        )

    return operations.eliminar_moto(
        session,
        moto
    )