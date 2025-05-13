from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar rutas
    from app.routes import pacientes_routes
    from app.routes import tratamiento_routes
    from app.routes import gestacion_routes
    from app.routes import direccion_routes
    from app.routes import consultas_routes
    from app.routes import fechas_routes
    from app.routes import recomendaciones_routes
    from app.routes import auth_routes
    app.register_blueprint(pacientes_routes.pacientes_bp)
    app.register_blueprint(tratamiento_routes.tratamientos_bp)
    app.register_blueprint(gestacion_routes.gestaciones_bp)
    app.register_blueprint(direccion_routes.direcciones_bp)
    app.register_blueprint(consultas_routes.consultas_bp)
    app.register_blueprint(fechas_routes.fechas_bp)
    app.register_blueprint(recomendaciones_routes.recomendaciones_bp)
    app.register_blueprint(auth_routes.auth_bp)

    return app