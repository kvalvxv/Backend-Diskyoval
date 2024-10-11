from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db
from flask import jsonify

def create_user(data):
    try:
        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            password=hashed_password,
            phone=data['phone'],
            user_type=data['user_type']
        )
        db.session.add(new_user)
        db.session.commit()
        print(f"ID del nuevo usuario: {new_user.id_client}") 
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def authenticate_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user :
        print(f"Usuario encontrado: {user.email}, ID Cliente: {user.id_client}") 
    if user and check_password_hash(user.password, data['password']):
        return jsonify({"message": "Authentication successful", "id_client": user.id_client}),200
       
    else:
        return jsonify({"message": "Invalid credentials"}), 401
