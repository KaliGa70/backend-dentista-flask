from .. import db

class Fechas(db.Model):
    __tablename__ = 'fechas'
    fecha_id = db.Column('idFecha', db.Integer, primary_key=True)
    fecha = db.Column('Fecha', db.Date, nullable=False)
    consultas_id = db.Column('Consultas_idConsultas', db.Integer, db.ForeignKey('consultas.idConsultas'), nullable=False)
    consultas = db.relationship('Consultas', backref='fechas')