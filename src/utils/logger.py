import logging
import os
from datetime import datetime

def setup_logging():
    """Configura el logging para la aplicación"""
    
    # Crear directorio de logs si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configurar formato del log
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(f'logs/diskyoval_{datetime.now().strftime("%Y%m%d")}.log'),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def log_error(error, context=""):
    """Función helper para loggear errores"""
    logger = setup_logging()
    logger.error(f"Error in {context}: {str(error)}", exc_info=True)

def log_info(message, context=""):
    """Función helper para loggear información"""
    logger = setup_logging()
    logger.info(f"Info in {context}: {message}")

def log_warning(message, context=""):
    """Función helper para loggear warnings"""
    logger = setup_logging()
    logger.warning(f"Warning in {context}: {message}")