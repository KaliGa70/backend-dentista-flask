from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Inicializar SQLAlchemy
db = SQLAlchemy()

def create_app():
    """
    Factory function para crear y configurar la aplicación Flask.
    """
    # Crear la instancia de Flask
    app = Flask(__name__)

    # Configurar la aplicación desde la clase Config
    app.config.from_object(Config)

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar blueprints (rutas)
    register_blueprints(app)

    return app

def register_blueprints(app):
    """
    Registrar todos los blueprints (rutas) de la aplicación.
    """
    from .routes.pacientes_routes import pacientes_bp
    from .routes.tratamiento_routes import tratamientos_bp
    from .routes.gestacion_routes import gestaciones_bp
    from .routes.direccion_routes import direcciones_bp
    from .routes.consultas_routes import consultas_bp
    from .routes.fechas_routes import fechas_bp
    from .routes.recomendaciones_routes import recomendaciones_bp


    app.register_blueprint(pacientes_bp)
    app.register_blueprint(tratamientos_bp)
    app.register_blueprint(gestaciones_bp)
    app.register_blueprint(direcciones_bp)
    app.register_blueprint(consultas_bp)
    app.register_blueprint(fechas_bp)
    app.register_blueprint(recomendaciones_bp)

