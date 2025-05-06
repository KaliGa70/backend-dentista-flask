from flask import Blueprint, jsonify, request
from ..services.gestacion_services import get_all_gestaciones, create_gestacion
gestaciones_bp = Blueprint('gestacion', __name__)

@gestaciones_bp.route('/gestacion', methods=['GET'])
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

@gestaciones_bp.route('/gestacion', methods=['POST'])
def add_gestacion():
    data = request.get_json()
    new_gestacion = create_gestacion(data)
    return (
        jsonify({'message': 'Gestacion creado', 'new_gestacion': new_gestacion.gestacion_id}),
        201,
    )
