from flask import jsonify
from .models import Transaction
from ..carrito.controller import Cart, ProductCart 
from src import db


def process_payment(id_cart):
    cart = Cart.query.get(id_cart)
    if cart.status != 'active':
        raise ValueError("Cart is not active")
    
    transaction = Transaction(cart=cart)
    db.session.add(transaction)
    
    cart.status = 'pending'
    db.session.commit()
    
    #definimos logica de procesamiento de pago , por ahora lo dejo en exitoso como una simulacion 
    payment_successful = True
    
    if payment_successful:
        transaction.status = 'completed'
        cart.status = 'completed'
        for item in cart.products:
            item.product.stock -= item.reserved_quantity 
            item.reserved_quantity = 0 
        db.session.commit()
        return {'message': 'payment succesful', 'transaction_id':transaction.id_transaction}, 200
    else:
        transaction.status = 'failed'
        cart.status = 'active'
        for item in cart.products:
            item.product.stock += item.reserved_quantity
            item.reserved_quantity = 0
        db.session.commit()
        return {'message':'payment failed'}, 400
    

def get_all_transaction():
    transactions = Transaction.query.all()
    return [transaction.to_dict() for transaction in transactions]

def get_transaction_by_id(transaction_id):
    transaction = Transaction.query.filter_by(id_transaction=transaction_id).first()
    if transaction:
        return transaction.to_dict()
    else:
        return {"message": "Transaction not found"}, 404


def create_transaction(cart_id):
    trasaction = Transaction(id_cart=cart_id, )
    db.session.add(trasaction)
    db.session.commit()
    return  trasaction

