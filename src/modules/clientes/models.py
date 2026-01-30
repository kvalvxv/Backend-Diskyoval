from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from src import db 
 

class User(db.Model):
    __tablename__='clients'
    id_client = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(255), nullable=False)
    
    carts = relationship('Cart', back_populates='owner')

    def to_dict(self):
        return {
            'id_client': self.id_client,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone,
            'user_type': self.user_type
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)