from .. import db

class Recomendaciones(db.Model):
    __tablename__ = 'recomendaciones'
    recomendacion_id = db.Column('idRecomendacion', db.Integer, primary_key=True)
    recomendacion = db.Column('Recomendacion', db.String(45), nullable=False)
    consultas_id = db.Column('Consultas_idConsultas', db.Integer, db.ForeignKey('consultas.idConsultas'), nullable=False)
    consultas = db.relationship('Consultas', backref='recomendaciones')