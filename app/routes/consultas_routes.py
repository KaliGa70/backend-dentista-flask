from flask import Blueprint, jsonify, request
from ..services.consultas_services import get_all_consultas, create_consulta
from flask_jwt_extended import jwt_required

consultas_bp = Blueprint('consultas', __name__, url_prefix='/consulta')

@consultas_bp.route('/obtener', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_consultas():
    consultas = get_all_consultas()
    return jsonify([
        {
            'consulta_id': d.consulta_id,
            'motivo'  : d.motivo,
            'paciente_id'  : d.paciente_id
        } for d in consultas
    ])

@consultas_bp.route('/create', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_consulta():
    data = request.get_json()
    new_consulta = create_consulta(data)
    return (
        jsonify({'message': 'consulta creada', 'new_consulta': new_consulta.consulta_id}),
        201,
    )
