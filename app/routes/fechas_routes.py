from flask import Blueprint, jsonify, request
from ..services.fechas_services import get_all_fechas, create_fecha
fechas_bp = Blueprint('fechas', __name__)

@fechas_bp.route('/fecha', methods=['GET'])
def get_fechas():
    fechas = get_all_fechas()
    return jsonify([
        {
            'fecha_id': f.fecha_id,
            'fecha'  : f.fecha,
            'consultas_id'  : f.consultas_id
        } for f in fechas
    ])

@fechas_bp.route('/fecha', methods=['POST'])
def add_fecha():
    data = request.get_json()
    new_fecha = create_fecha(data)
    return (
        jsonify({'message': 'fecha creada', 'new_fecha': new_fecha.fecha_id}),
        201,
    )
