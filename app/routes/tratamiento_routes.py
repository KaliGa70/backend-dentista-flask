from flask import Blueprint, jsonify, request
from ..services.tratamiento_services import get_all_tratamientos, create_tratamiento

tratamientos_bp = Blueprint('tratamiento', __name__)

@tratamientos_bp.route('/tratamiento', methods=['GET'])
def get_tratamientos():
    tratamientos = get_all_tratamientos()
    return jsonify([
        {
            'id_tratamiento': t.id_tratamiento,
            'tratamiento'  : t.tratamiento,
            'paciente_id'  : t.paciente_id
        } for t in tratamientos
    ])

@tratamientos_bp.route('/tratamiento', methods=['POST'])
def add_tratamiento():
    data = request.get_json()
    nuevo = create_tratamiento(data)
    return (
        jsonify({'message': 'Tratamiento creado', 'id_tratamiento': nuevo.id_tratamiento}),
        201,
    )
