from flask import Blueprint, jsonify, request
from ..services.recomendaciones_services import get_all_recomendaciones, create_recomendacion
from flask_jwt_extended import jwt_required

recomendaciones_bp = Blueprint('recomendaciones', __name__, url_prefix='/recomendacion')

@recomendaciones_bp.route('/obtener', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_recomendaciones():
    recomendaciones = get_all_recomendaciones()
    return jsonify([
        {
            'recomendacion_id': r.recomendacion_id,
            'recomendacion'  : r.recomendacion,
            'consultas_id'  : r.consultas_id
        } for r in recomendaciones
    ])

@recomendaciones_bp.route('/create', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_recomendacion():
    data = request.get_json()
    new_recomendacion = create_recomendacion(data)
    return (
        jsonify({'message': 'recomendacion creada', 'new_recomendacion': new_recomendacion.recomendacion_id}),
        201,
    )
