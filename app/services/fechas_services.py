from ..models.fechas import Fechas
from .. import db

def get_all_fechas():
    return Fechas.query.all()

def create_fecha(data):
    new_fecha = Fechas(
        fecha = data['fecha'],
        consultas_id = data['consultas_id']
    )
    db.session.add(new_fecha)
    db.session.commit()
    return new_fecha