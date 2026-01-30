from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from jwt.exceptions import DecodeError
from dotenv import load_dotenv
from flask_cors import CORS
import os
from datetime import timedelta

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    app.config['jwt_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=260)
    CORS(app)
    
    db.init_app(app)
    jwt = JWTManager(app)
    
    with app.app_context():
        from .modules.clientes.routes import users_bp
        app.register_blueprint(users_bp, url_prefix='/clients')
        from .modules.transacciones.routes import transaction_bp
        app.register_blueprint(transaction_bp, url_prefix='/transactions')
        from .modules.productos.routes import product_bp
        app.register_blueprint(product_bp, url_prefix='/products')
        from .modules.carrito.routes import cart_bp
        app.register_blueprint(cart_bp,url_prefix='/cart')
        
        
        
    #db.create_all()

    
    @jwt.invalid_token_loader
    def invalid_token_callback():
        return jsonify({
            "msg" : "Signature verication falied."
            
        }),401
        
    @jwt.unauthorized_loader
    def missing_token_callback():
        return jsonify({
            "msg" : "Request does not contain an access token."
        }),401

    return app
