from flask import Blueprint, request, jsonify
from classes.models import User
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import check_password_hash
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__)

# Registro de usuarios
@auth_bp.route('/register', methods=['POST'])
# def register():
#     db= get_db()
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')

#     if not username or not email or not password:
#         return jsonify({'message': 'Faltan campos'}), 400

#     # Hash de la contraseña
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#     # Crear el nuevo usuario
#     new_user = User(username=username, email=email, password_hash=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'message': 'Usuario registrado exitosamente'}), 201

# Inicio de sesión (login) y generación de JWT
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Verificar si el usuario existe
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        # Crear token JWT
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

# Ruta protegida como ejemplo
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Obtener la identidad del usuario actual desde el token
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(logged_in_as=user.username), 200