from ..models.recomendaciones import Recomendaciones
from .. import db

def get_all_recomendaciones():
    return Recomendaciones.query.all()

def create_recomendacion(data):
    new_recomendacion = Recomendaciones(
        recomendacion = data['recomendacion'],
        consultas_id = data['consultas_id']
    )
    db.session.add(new_recomendacion)
    db.session.commit()
    return new_recomendacion