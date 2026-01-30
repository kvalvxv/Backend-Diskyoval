from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from src import db
from src.utils.validators import validate_user_data, validate_login_data
from flask import jsonify

def create_user(data):
    errors = validate_user_data(data)
    if errors:
        return {"error": "Validation failed", "details": errors}
    
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
        return {"message": "User created successfully", "id_client": new_user.id_client}
    except Exception as e:
        db.session.rollback()
        raise e

def authenticate_user(data):
    errors = validate_login_data(data)
    if errors:
        return {"error": "Validation failed", "details": errors}
    
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        return {"message": "Authentication successful", "id_client": user.id_client, "user_type": user.user_type}
    else:
        return {"message": "Invalid credentials"}


def get_all_users(search=None):
    try:
        if search:
            users = User.query.filter(User.name.ilike(f"%{search}%")).all()
        else:
            users = User.query.all()

        user_list = []
        for user in users:
            user_list.append({
                'id_client': user.id_client,
                'name': user.name,
                'lastname': user.lastname,
                'email': user.email,
                'phone': user.phone,
                'user_type': user.user_type
            })

        return user_list
    except Exception as e:
        raise e
