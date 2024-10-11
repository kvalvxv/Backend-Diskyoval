from flask import Blueprint, jsonify, request
from .controller import process_payment, get_all_transaction,get_transaction_by_id,create_transaction

transaction_bp = Blueprint('transaction_bp', __name__)


@transaction_bp.route('/process_payment/<int:id_cart>', methods=['POST'])
def process_payment_route(id_cart):
    try:
        result, status_code = process_payment(id_cart)
        return jsonify(result), status_code
    except ValueError as e :
        return jsonify({"error": str(e)}), 400
    except Exception as e :
        return jsonify({"error": str(e)}), 500

@transaction_bp.route('/', methods=['GET'])
def get_transactions():
    try:
        transactions = get_all_transaction()
        return jsonify(transactions), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@transaction_bp.route('/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    result = get_transaction_by_id(transaction_id)
    if isinstance(result, tuple):
        response, status_code = result
        return jsonify(response), status_code
    return jsonify(result), 200

@transaction_bp.route('/new_transaction', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        cart_id = data['id_cart']
        total = data['total']
        new_transaction = create_transaction(cart_id, total)
        return jsonify(new_transaction.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500