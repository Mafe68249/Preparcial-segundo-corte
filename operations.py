from sqlmodel import select
from models import Moto, Usuario



def crear_usuario(session, usuario):

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario


def obtener_usuarios(session):

    return session.exec(select(Usuario)).all()


def obtener_usuario_por_id(session, id):

    return session.get(Usuario, id)



def crear_moto(session, moto):

    session.add(moto)
    session.commit()
    session.refresh(moto)

    return moto


def obtener_motos(session):

    statement = select(Moto).where(Moto.activo == True)

    return session.exec(statement).all()


def obtener_moto_por_id(session, id):

    return session.get(Moto, id)


def actualizar_moto(session, moto, datos_actualizados):

    for campo, valor in datos_actualizados.items():
        setattr(moto, campo, valor)

    session.add(moto)
    session.commit()
    session.refresh(moto)

    return moto


def eliminar_moto(session, moto):

    moto.activo = False

    session.add(moto)
    session.commit()
    session.refresh(moto)

    return {
        "mensaje": "Moto desactivada correctamente"
    }