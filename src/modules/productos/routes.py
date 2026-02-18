from flask import Blueprint, request, jsonify
from .controller import get_product_by_id, get_all_products, create_product, update_product, delete_product
from werkzeug.utils import secure_filename

product_bp = Blueprint('products', __name__, url_prefix='/products')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@product_bp.route('/', methods=['GET'])
def get_all_products_route():
    try:
        products = get_all_products()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({'msg':'product not found'}), 404


@product_bp.route('/new_product', methods=['POST'])
def create_product_route():
    try:
        if request.content_type and 'multipart/form-data' in request.content_type:
            name = request.form.get('name')
            description = request.form.get('description')
            price = request.form.get('price')
            stock = request.form.get('stock')
            image = request.files.get('image')
            
            if not all([name, description, price, stock]):
                return jsonify({'error': 'Missing required fields'}), 400
            
            product_data = {
                'name': name,
                'description': description,
                'price': float(price),
                'stock': int(stock)
            }
            
            image_file = image if image and allowed_file(image.filename) else None
            result = create_product(product_data, image_file)
        else:
            data = request.get_json()
            result = create_product(data)
        
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    try:
        if request.content_type and 'multipart/form-data' in request.content_type:
            data = {
                'name': request.form.get('name'),
                'description': request.form.get('description'),
                'price': request.form.get('price'),
                'stock': request.form.get('stock')
            }
            data = {k: v for k, v in data.items() if v is not None}
            
            if data.get('price'):
                data['price'] = float(data['price'])
            if data.get('stock'):
                data['stock'] = int(data['stock'])
            
            image = request.files.get('image')
            new_image = image if image and allowed_file(image.filename) else None
            
            product = update_product(product_id, data, new_image)
        else:
            data = request.get_json()
            product = update_product(product_id, data)
        
        if product:
            return jsonify(product.to_dict()), 200
        return jsonify({'msg':'product not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    try:
        product = delete_product(product_id)
        if product:
            return jsonify({
                'msg': f'{product.name} with ID {product.id_product} deleted successfully'
            }), 200
        return jsonify({'msg':'product not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500