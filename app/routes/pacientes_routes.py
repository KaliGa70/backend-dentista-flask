from flask import Blueprint, jsonify, request
from ..services.pacientes_services import get_all_pacientes, create_paciente

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/pacientes', methods=['GET'])
def get_names():
    pacientes = get_all_pacientes()
    return jsonify([{'idPacientes': n.idPacientes, 'Nombre': n.Nombre, 'Telefono': n.Telefono, 'Alergias': n.Alergias, 'Fecha_De_Nacimiento': n.Fecha_De_Nacimiento} for n in pacientes])

@pacientes_bp.route('/pacientes', methods=['POST'])
def add_name():
    data = request.get_json()
    new_paciente = create_paciente(data)
    return jsonify({'message': 'Paciente created successfully', 'name_id': new_paciente.idPacientes}), 201