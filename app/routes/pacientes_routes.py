from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..services.pacientes_services import get_all_pacientes, create_paciente

pacientes_bp = Blueprint('pacientes', __name__, url_prefix='/pacientes')

@pacientes_bp.route('/obtener', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_names():
    pacientes = get_all_pacientes()
    return jsonify([{'idPacientes': n.idPacientes, 'Nombre': n.Nombre, 'Telefono': n.Telefono, 'Alergias': n.Alergias, 'Fecha_De_Nacimiento': n.Fecha_De_Nacimiento} for n in pacientes])

@pacientes_bp.route('/create', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_name():
    data = request.get_json()
    new_paciente = create_paciente(data)
    return jsonify({'message': 'Paciente created successfully', 'name_id': new_paciente.idPacientes}), 201