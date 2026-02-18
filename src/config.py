import os
import cloudinary
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # Database configuration - supports multiple database types
    DATABASE_URL = os.getenv('DATABASE_URL')
    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Legacy MySQL configuration
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_EXPIRE_MINUTES', 260))  # minutes
    
    # Server configuration
    PORT = int(os.getenv('PORT', 4001))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # Environment
    ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Security
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}