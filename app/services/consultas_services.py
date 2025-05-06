from ..models.consultas import Consultas
from .. import db

def get_all_consultas():
    return Consultas.query.all()

def create_consulta(data):
    new_consulta = Consultas(
        motivo = data['motivo'],
        paciente_id = data['paciente_id']
    )
    db.session.add(new_consulta)
    db.session.commit()
    return new_consulta