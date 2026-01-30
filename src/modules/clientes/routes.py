from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .controller import create_user, authenticate_user,get_all_users



users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get('name')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')
        user_type = data.get('user_type', 'cliente')

        if not (name and lastname and email and password and phone and user_type):
            return jsonify({'message': 'All fields are required'}), 400

        result = create_user({
            'name': name,
            'lastname': lastname,
            'email': email,
            'password': password,
            'phone': phone,
            'user_type': user_type
        })
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not (email and password):
            return jsonify({'message': 'Correo or contraseña is missing'}), 400

        result = authenticate_user({
            'email': email,
            'password': password
        })
        
        if result.get("message") == "Authentication successful":
            id_client = result.get('id_client')
            user_type = result.get('user_type')
            access_token = create_access_token(identity={'email': email, 'id_client': id_client, 'user_type': user_type })
            return jsonify({'access_token': access_token, 'user_type': user_type}), 200
        else:
            return jsonify(result), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    try:
        search = request.args.get('search', None)
        users = get_all_users(search)
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/protected_route', methods=['GET'])
@jwt_required()
def protected():
    try:
        current_user = get_jwt_identity()
        return jsonify({
            'message': 'Congratulations! You have reached a protected route!',
            'user': current_user,
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
