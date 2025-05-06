from flask import Blueprint, jsonify, request
from ..services.direccion_services import get_all_direcciones, create_direccion
direcciones_bp = Blueprint('direccion', __name__)

@direcciones_bp.route('/direccion', methods=['GET'])
def get_direcciones():
    direcciones = get_all_direcciones()
    return jsonify([
        {
            'direccion_id': d.direccion_id,
            'calle'  : d.calle,
            'numero'  : d.numero,
            'codigo_postal'  : d.codigo_postal,
            'paciente_id'  : d.paciente_id
        } for d in direcciones
    ])

@direcciones_bp.route('/direccion', methods=['POST'])
def add_direccion():
    data = request.get_json()
    new_direccion = create_direccion(data)
    return (
        jsonify({'message': 'Direccion creada', 'new_direccion': new_direccion.direccion_id}),
        201,
    )
