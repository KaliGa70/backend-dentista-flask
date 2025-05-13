# app/routes/auth_routes.py

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    get_csrf_token
)
from app.services.auth_services import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    try:
        user = AuthService.register_user(
            username=data.get('username', '').strip(),
            email=data.get('email', '').strip(),
            password=data.get('password', '')
        )
    except ValueError as e:
        return jsonify(msg=str(e)), 409

    # Generar tokens
    access_token  = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    # Preparar respuesta con cookies y CSRF tokens
    resp = make_response(jsonify(
        msg='Usuario registrado',
        access_csrf = get_csrf_token(access_token),
        refresh_csrf = get_csrf_token(refresh_token)
    ), 201)

    set_access_cookies(resp,  access_token)   # Cookie HttpOnly en '/'
    set_refresh_cookies(resp, refresh_token)  # Cookie HttpOnly en '/auth/refresh'

    return resp

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    user = AuthService.authenticate(
        username=data.get('username', '').strip(),
        password=data.get('password', '')
    )
    if not user:
        return jsonify(msg='Credenciales inválidas'), 401

    # Generar tokens
    access_token  = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    resp = make_response(jsonify(
        msg='Login exitoso',
        access_csrf = get_csrf_token(access_token),
        refresh_csrf = get_csrf_token(refresh_token)
    ), 200)

    set_access_cookies(resp,  access_token)
    set_refresh_cookies(resp, refresh_token)

    return resp

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True, locations=['cookies'])
def refresh():
    # Solo se envía aquí la cookie de refresh token
    user_id = get_jwt_identity()
    new_access = create_access_token(identity=str(user_id))

    resp = make_response(jsonify(
        access_csrf = get_csrf_token(new_access)
    ), 200)
    set_access_cookies(resp, new_access)
    return resp

@auth_bp.route('/logout', methods=['POST'])
def logout():
    resp = make_response(jsonify(msg='Logout exitoso'), 200)
    unset_jwt_cookies(resp)
    return resp

@auth_bp.route('/me', methods=['GET'])
@jwt_required(locations=['cookies'])
def me():
    user = AuthService.get_user_by_id(get_jwt_identity())
    if not user:
        return jsonify(msg='Usuario no encontrado'), 404

    return jsonify({
        'id':       user.id,
        'username': user.username,
        'email':    user.email,
        'created':  user.created_at.isoformat()
    }), 200
