from .. import db

class Direccion(db.Model):
    __tablename__ = 'direccion'
    direccion_id = db.Column('idDireccion', db.Integer, primary_key=True)
    calle = db.Column('Calle', db.String(45), nullable=False)
    numero = db.Column('Numero', db.Integer, nullable=False)
    codigo_postal = db.Column('Codigo_Postal', db.Integer, nullable=False)
    paciente_id = db.Column('Pacientes_idPacientes', db.Integer, db.ForeignKey('pacientes.idPacientes'), nullable=False)
    pacientes = db.relationship('Pacientes', backref='direccion')