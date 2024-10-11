from flask import Blueprint, request, jsonify
from src import db 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .controller import create_cart,get_active_cart,verify_cart_owner, add_product_to_cart, update_product_quantity, remove_product_from_cart, get_products_cart, Product

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')


@cart_bp.route('/', methods=['POST'])
@jwt_required()
def create_cart_route():
    current_user = get_jwt_identity()
    id_client = current_user.get("id_client")
    
    if id_client is None :
        return jsonify({"message": "User not found"}), 404
    
    cart = create_cart(id_client)
    return jsonify({
        'id_cart': cart.id_cart,
        'id_client': cart.id_client,
        'creation_date': cart.creation_date
    }), 201
    
    
@cart_bp.route('/active', methods=['GET'])
@jwt_required()
def  get_active_cart_route():
    current_user = get_jwt_identity()
    id_client = current_user.get("id_client")
    
    if id_client is None :
        return jsonify({"message": "User not found"}), 404
    
    cart = get_active_cart(id_client)
    return cart

    
@cart_bp.route('/<int:id_cart>/products', methods=['POST'])
@jwt_required()
def add_product_route(id_cart):
    current_user = get_jwt_identity()
    id_client = current_user.get("id_client")
    
    if id_client is None :
        return jsonify({"message": "User not found"}), 404
    
    if not verify_cart_owner(id_cart, id_client):
        return jsonify({'msg': 'You are not the owner of this cart'}), 401
    
    data = request.get_json()
    id_product = data.get('id_product')
    quantity = data.get('quantity')
    
    try:
        product_cart = add_product_to_cart(id_cart, id_product, quantity)
        return jsonify({
            'id_product': product_cart.id_product,
            'id_product_cart': product_cart.id_product_cart,
            'id_cart': product_cart.id_cart,
            'quantity': product_cart.quantity
            
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}),400
  

@cart_bp.route('/<int:id_cart>/products/<int:id_product>', methods=['PUT'])
@jwt_required()
def update_product_route(id_cart, id_product):
    current_user = get_jwt_identity()
    id_client = current_user.get("id_client")
    
    if id_client is None :
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    new_quantity = data.get('quantity')
    product_cart = update_product_quantity(id_cart, id_product, new_quantity)
    if product_cart:
        return jsonify({
            'id_product_cart': product_cart.id_product_cart,
            'id_cart': product_cart.id_cart,
            'id_product': product_cart.id_product,
            'quantity': product_cart.quantity
        }),200
    return jsonify({'error':'Product not found in cart'}), 404


@cart_bp.route('/<int:id_cart>/products', methods=['DELETE'])
@jwt_required()
def remove_product_route(id_cart, id_product):
    current_user = get_jwt_identity()
    id_client = current_user.get("id_client")
    
    if id_client is None :
        return jsonify({"message": "User not found"}), 404
    
    success = remove_product_from_cart(id_cart, id_product)
    if success:
        return jsonify({'message':'Product removed from cart'}), 200
    return jsonify({'error':'Product not found in cart'}), 404


@cart_bp.route('/<int:id_cart>/products', methods=['GET'])
@jwt_required()
def get_products_route(id_cart):
    current_user = get_jwt_identity()
    id_client = current_user.get("id_client")
    
    if id_client is None :
        return jsonify({"message": "User not found"}), 404
    
    products = get_products_cart(id_cart)
    return jsonify([{
        'id_product_cart': product.id_product_cart,
        'id_cart': product.id_cart,
        'id_product': product.id_product,
        'quantity': product.quantity
    }for product in products]), 200
