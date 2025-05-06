from ..models.direccion import Direccion
from .. import db

def get_all_direcciones():
    return Direccion.query.all()

def create_direccion(data):
    new_direccion = Direccion(
        calle = data['calle'],
        numero = data['numero'],
        codigo_postal = data['codigo_postal'],
        paciente_id = data['paciente_id']
    )
    db.session.add(new_direccion)
    db.session.commit()
    return new_direccion