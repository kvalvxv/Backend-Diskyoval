from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
import os
from datetime import timedelta, datetime

load_dotenv()

db = SQLAlchemy()

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Load configuration
    if config_name:
        app.config.from_object(f'src.config.{config_name.title()}Config')
    else:
        app.config.from_object('src.config.Config')
    
    # Override JWT expiration from config
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=app.config.get('JWT_ACCESS_TOKEN_EXPIRES', 260))
    
    # Configure CORS for production
    CORS(app, 
         origins=app.config.get('CORS_ORIGINS', ['*']),
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
         allow_headers=['Content-Type', 'Authorization'])
    
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
        app.register_blueprint(cart_bp, url_prefix='/cart')
        
        # Health check endpoint for deployment platforms
        @app.route('/health')
        def health_check():
            return jsonify({
                'status': 'healthy',
                'timestamp': datetime.utcnow().isoformat(),
                'version': '1.0.0'
            }), 200
        
        @app.route('/')
        def root():
            return jsonify({
                'message': 'Backend-Diskyoval API is running',
                'version': '1.0.0',
                'endpoints': {
                    'health': '/health',
                    'auth': '/clients',
                    'products': '/products',
                    'cart': '/cart',
                    'transactions': '/transactions'
                }
            }), 200
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            "msg": "Signature verification failed.",
            "error": str(error)
        }), 401
        
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            "msg": "Request does not contain an access token.",
            "error": str(error)
        }), 401

    return app