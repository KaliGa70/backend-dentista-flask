from ..models.tratamiento import Tratamiento
from .. import db

def get_all_tratamientos():
    return Tratamiento.query.all()

def create_tratamiento(data):
    nuevo = Tratamiento(
        tratamiento = data['tratamiento'],
        paciente_id = data['paciente_id'],
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo
