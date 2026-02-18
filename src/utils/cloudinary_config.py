import os
import cloudinary
from cloudinary import api, uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv

load_dotenv()

# Check if Cloudinary is configured
CLOUDINARY_CONFIGURED = all([
    os.getenv('CLOUDINARY_CLOUD_NAME'),
    os.getenv('CLOUDINARY_API_KEY'),
    os.getenv('CLOUDINARY_API_SECRET')
])

if CLOUDINARY_CONFIGURED:
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET'),
        secure=True
    )


def upload_image(file, folder='diskyoval/products'):
    """
    Sube una imagen a Cloudinary y retorna la URL y public_id
    """
    if not CLOUDINARY_CONFIGURED:
        return {
            'success': False,
            'error': 'Cloudinary not configured. Please set CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, and CLOUDINARY_API_SECRET environment variables.'
        }
    
    try:
        result = uploader.upload(
            file,
            folder=folder,
            transformation=[
                {'width': 800, 'height': 800, 'crop': 'limit'},
                {'quality': 'auto'},
                {'fetch_format': 'auto'}
            ]
        )
        return {
            'success': True,
            'url': result['secure_url'],
            'public_id': result['public_id'],
            'format': result['format'],
            'width': result['width'],
            'height': result['height']
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def delete_image(public_id):
    """
    Elimina una imagen de Cloudinary
    """
    if not CLOUDINARY_CONFIGURED:
        return {
            'success': False,
            'error': 'Cloudinary not configured'
        }
    
    if not public_id:
        return {'success': True}
    
    try:
        result = uploader.destroy(public_id)
        return {
            'success': True,
            'result': result
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def get_image_url(public_id, transformations=None):
    """
    Genera una URL optimizada para una imagen existente
    """
    if not public_id:
        return None
    
    if not CLOUDINARY_CONFIGURED:
        return None
    
    try:
        options = {}
        if transformations:
            options['transformation'] = transformations
        
        url, options = cloudinary_url(public_id, **options)
        return url
    except Exception:
        return None