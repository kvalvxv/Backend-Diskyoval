from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .controller import create_user, authenticate_user

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
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
    return result

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    id_client = data.get('id_client')
    print("ID CLIENT",id_client)
    password = data.get('password')

    if not (email and password):
        return jsonify({'message': 'Correo or contraseña is missing'}), 400

    result = authenticate_user({
        'email': email,
        'password': password,
        'id_client': id_client
        
    })
    

    if result[1] == 200:  
        response_data = result[0].get_json()  
        id_client = response_data.get('id_client') 
        print(f"ID Cliente obtenido: {id_client}") 
        access_token = create_access_token(identity={'email': email, 'id_client': id_client})
        return jsonify({'access_token': access_token}), 200
    return result

@users_bp.route('/protected_route', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    print(f"current_user: {current_user}") 
    return jsonify({
        'message': 'Congratulations! You have reached a protected route!',
        'user': current_user,
    }), 200
