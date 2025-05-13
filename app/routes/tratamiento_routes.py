from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..services.tratamiento_services import get_all_tratamientos, create_tratamiento

tratamientos_bp = Blueprint('tratamiento', __name__, url_prefix='/tratamiento')

@tratamientos_bp.route('/obtener', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_tratamientos():
    tratamientos = get_all_tratamientos()
    return jsonify([
        {
            'id_tratamiento': t.id_tratamiento,
            'tratamiento'  : t.tratamiento,
            'paciente_id'  : t.paciente_id
        } for t in tratamientos
    ])

@tratamientos_bp.route('/create', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_tratamiento():
    data = request.get_json()
    nuevo = create_tratamiento(data)
    return (
        jsonify({'message': 'Tratamiento creado', 'id_tratamiento': nuevo.id_tratamiento}),
        201,
    )
