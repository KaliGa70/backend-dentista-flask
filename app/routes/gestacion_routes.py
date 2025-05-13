from flask import Blueprint, jsonify, request
from ..services.gestacion_services import get_all_gestaciones, create_gestacion
from flask_jwt_extended import jwt_required

gestaciones_bp = Blueprint('gestacion', __name__, url_prefix='/gestacion')

@gestaciones_bp.route('/obtener', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_gestaciones():
    gestaciones = get_all_gestaciones()
    return jsonify([
        {
            'gestacion_id': g.gestacion_id,
            'descripcion'  : g.descripcion,
            'inicio_de_gestacion'  : g.inicio_de_gestacion,
            'paciente_id'  : g.paciente_id
        } for g in gestaciones
    ])

@gestaciones_bp.route('/create', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_gestacion():
    data = request.get_json()
    new_gestacion = create_gestacion(data)
    return (
        jsonify({'message': 'Gestacion creado', 'new_gestacion': new_gestacion.gestacion_id}),
        201,
    )
