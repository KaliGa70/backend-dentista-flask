from flask import Blueprint, jsonify, request
from ..services.fechas_services import get_all_fechas, create_fecha
from flask_jwt_extended import jwt_required

fechas_bp = Blueprint('fechas', __name__, url_prefix='/fecha')

@fechas_bp.route('/obtener', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_fechas():
    fechas = get_all_fechas()
    return jsonify([
        {
            'fecha_id': f.fecha_id,
            'fecha'  : f.fecha,
            'consultas_id'  : f.consultas_id
        } for f in fechas
    ])

@fechas_bp.route('/create', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_fecha():
    data = request.get_json()
    new_fecha = create_fecha(data)
    return (
        jsonify({'message': 'fecha creada', 'new_fecha': new_fecha.fecha_id}),
        201,
    )
