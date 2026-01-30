def validate_user_data(data):
    """Valida los datos de entrada para crear/actualizar usuarios"""
    errors = []
    
    # Validaciones básicas
    if not data.get('name') or len(data.get('name', '').strip()) < 2:
        errors.append('Name must be at least 2 characters long')
    
    if not data.get('lastname') or len(data.get('lastname', '').strip()) < 2:
        errors.append('Lastname must be at least 2 characters long')
    
    if not data.get('email'):
        errors.append('Email is required')
    elif '@' not in data.get('email', ''):
        errors.append('Invalid email format')
    
    if not data.get('password') or len(data.get('password', '')) < 6:
        errors.append('Password must be at least 6 characters long')
    
    if not data.get('phone') or len(data.get('phone', '').strip()) < 8:
        errors.append('Phone must be at least 8 characters long')
    
    if not data.get('user_type'):
        errors.append('User type is required')
    elif data.get('user_type') not in ['cliente', 'admin']:
        errors.append('User type must be either "cliente" or "admin"')
    
    return errors

def validate_product_data(data):
    """Valida los datos de entrada para crear/actualizar productos"""
    errors = []
    
    if not data.get('name') or len(data.get('name', '').strip()) < 2:
        errors.append('Product name must be at least 2 characters long')
    
    if not data.get('description') or len(data.get('description', '').strip()) < 10:
        errors.append('Product description must be at least 10 characters long')
    
    if data.get('price') is None:
        errors.append('Price is required')
    elif not isinstance(data.get('price'), (int, float)) or data.get('price') <= 0:
        errors.append('Price must be a positive number')
    
    if data.get('stock') is None:
        errors.append('Stock is required')
    elif not isinstance(data.get('stock'), int) or data.get('stock') < 0:
        errors.append('Stock must be a non-negative integer')
    
    return errors

def validate_login_data(data):
    """Valida los datos de entrada para login"""
    errors = []
    
    if not data.get('email'):
        errors.append('Email is required')
    
    if not data.get('password'):
        errors.append('Password is required')
    
    return errors