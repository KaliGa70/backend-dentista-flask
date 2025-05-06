from .. import db

class Gestacion(db.Model):
    __tablename__ = 'gestacion'
    gestacion_id = db.Column('ID_Gestacion',db.Integer, primary_key=True)
    descripcion = db.Column('Descripcion', db.String(45), nullable=False)
    inicio_de_gestacion = db.Column('Inicio_De_Gestacion', db.Date, nullable=False)
    paciente_id = db.Column('Pacientes_idPacientes', db.Integer, 
                            db.ForeignKey('pacientes.idPacientes'), nullable=False)
    
    pacientes = db.relationship('Pacientes', backref='gestacion')