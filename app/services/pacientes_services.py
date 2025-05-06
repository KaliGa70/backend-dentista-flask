from ..models.pacientes import Pacientes
from .. import db

def get_all_pacientes():
    return Pacientes.query.all()

def create_paciente(data):
    new_paciente = Pacientes(
        Nombre = data['Nombre'],
        Telefono = data['Telefono'],
        Fecha_De_Nacimiento = data['Fecha_De_Nacimiento'],
        Alergias = data['Alergias']
    )
    db.session.add(new_paciente)
    db.session.commit()
    return new_paciente