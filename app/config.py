class Config:
    # Configuración manual de la base de datos
    DB_USER = 'root'
    DB_PASSWORD = 'A$2001M$10D$25'
    DB_HOST = 'localhost'
    DB_NAME = 'pacientes'

    # Construir la URI de la base de datos
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False