from flask import Blueprint, request, jsonify
from .controller import get_product_by_id, get_all_products, create_product, update_product, delete_product

product_bp = Blueprint('products', __name__, url_prefix='/products')


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
    return jsonify({'msg':'product not found'}), 200

@product_bp.route('/new_product', methods=['POST'])
def create_product_route():
    data = request.get_json()
    result = create_product(data)
    
    return jsonify(result), 200

@product_bp.route('<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    product = update_product(product_id, data)
    if product:
        return jsonify(product.to_dict()), 200
    return {'msg':'product not found'}, 404

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    product = delete_product(product_id)
    if product:
        return jsonify(product.name,product.id_product,"deleted succesfully"), 200
    return {'msg':'product not found'}, 404