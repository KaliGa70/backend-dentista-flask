from .pacientes_services import get_all_pacientes, create_paciente
from .tratamiento_services import get_all_tratamientos, create_tratamiento
from .gestacion_services import get_all_gestaciones, create_gestacion
from .direccion_services import get_all_direcciones, create_direccion
from .consultas_services import get_all_consultas, create_consulta
from .fechas_services import get_all_fechas, create_fecha
from .recomendaciones_services import get_all_recomendaciones, create_recomendacion
from .auth_services import (
    AuthService
)
# Exportar todos los servicios
__all__ = [
    'get_all_pacientes', 'create_paciente',
    'get_all_tratamientos', 'create_tratamiento',
    'get_all_gestaciones', 'create_gestacion',
    'get_all_direcciones', 'create_direccion',
    'get_all_consultas', 'create_consulta',
    'get_all_fechas', 'create_fecha',
    'get_all_recomendaciones', 'create_recomendacion',
    'register_user', 'authenticate', 'get_user_by_id', 'generate_token'
]

register_user   = AuthService.register_user
authenticate    = AuthService.authenticate
generate_token  = AuthService.generate_token
get_user_by_id  = AuthService.get_user_by_id