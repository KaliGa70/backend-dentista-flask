# app/services/auth_service.py

from flask_jwt_extended import create_access_token
from ..models.users import User
from .. import db

class AuthService:
    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        if User.query.filter_by(username=username).first():
            raise ValueError("El nombre de usuario ya existe.")
        if User.query.filter_by(email=email).first():
            raise ValueError("El correo electrónico ya está registrado.")
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate(username: str, password: str) -> User | None:
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def generate_token(user: User) -> str:
        return create_access_token(identity=str(user.id))

    @staticmethod
    def get_user_by_id(user_id: int) -> User | None:
        """
        Recupera el usuario de la base de datos dado su ID,
        o devuelve None si no existe.
        """
        return User.query.get(user_id)
