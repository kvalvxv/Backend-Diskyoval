import gunicorn
from src import create_app
import os

# Configuration
port = os.getenv('PORT', '4001')
workers = int(os.getenv('WEB_CONCURRENCY', '2'))
host = os.getenv('HOST', '0.0.0.0')
bind_env = f'{host}:{port}'

# Create Flask app
app = create_app('production')

# Gunicorn configuration
options = {
    'bind': bind_env,
    'workers': workers,
    'worker_class': 'sync',
    'worker_connections': 1000,
    'timeout': 30,
    'keepalive': 2,
    'max_requests': 1000,
    'max_requests_jitter': 50,
    'preload_app': True,
    'accesslog': '-',
    'errorlog': '-',
    'loglevel': os.getenv('LOG_LEVEL', 'info'),
}

if __name__ == '__main__':
    gunicorn.run(app, **options)