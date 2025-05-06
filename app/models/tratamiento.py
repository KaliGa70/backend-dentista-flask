from .. import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'

    id_tratamiento = db.Column('idTratamiento', db.Integer, primary_key=True)
    tratamiento    = db.Column('Tratamiento',  db.String(45), nullable=False)
    paciente_id    = db.Column('Pacientes_idPacientes', db.Integer,
                               db.ForeignKey('pacientes.idPacientes'), nullable=False)

    paciente = db.relationship('Pacientes', backref='tratamientos')
