from .. import db

class Consultas(db.Model):
    __tablename__ = 'consultas'
    consulta_id = db.Column('idConsultas', db.Integer, primary_key=True)
    motivo = db.Column('Motivo',db.String(45), nullable=False)
    paciente_id = db.Column('Pacientes_idPacientes', db.Integer, db.ForeignKey('pacientes.idPacientes'), nullable=False)
    pacientes = db.relationship('Pacientes', backref='consultas')