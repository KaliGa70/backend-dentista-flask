from .. import db

class Pacientes(db.Model):
    __tablename__ = 'pacientes'
    idPacientes = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(45), nullable=False)
    Telefono = db.Column(db.Integer, nullable=False)
    Alergias = db.Column(db.JSON, nullable=False)
    Fecha_De_Nacimiento = db.Column(db.Date, nullable=False)
