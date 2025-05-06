from ..models.gestacion import Gestacion
from .. import db

def get_all_gestaciones():
    return Gestacion.query.all()

def create_gestacion(data):
    new_gestacion = Gestacion(
        descripcion = data['descripcion'],
        inicio_de_gestacion = data['inicio_de_gestacion'],
        paciente_id = data['paciente_id']
    )
    db.session.add(new_gestacion)
    db.session.commit()
    return new_gestacion