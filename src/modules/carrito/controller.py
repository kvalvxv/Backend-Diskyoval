from src import db 
from .models import Cart, ProductCart
from ..productos.models import Product
from flask import jsonify



def create_cart(id_client):
    new_cart = Cart(id_client=id_client)
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def get_active_cart(id_client):
    cart =Cart.query.filter_by(id_client=id_client, status="active").first()
    if cart :
        return cart
    else:
        return None

def verify_cart_owner(id_cart, id_client):
    cart = get_active_cart(id_client)
    if cart and cart.id_cart == id_cart:
        return True
    return False


def add_product_to_cart(id_cart, id_product , quantity):
    cart = Cart.query.filter_by(id_cart=id_cart, status = 'active').first()
    if not cart:
        cart = Cart(id_cart=id_cart)
        db.session.add(cart)
        
    product = Product.query.get(id_product)
    if not product:
        raise ValueError("product not found")
    if product.stock < quantity:
        raise ValueError("Not enough stock")
    
    cart_item = ProductCart(cart= cart, product= product, quantity=quantity)
    db.session.add(cart_item)
    
    
    product.stock -= quantity
    cart_item.reserved_quantity = quantity
    
    db.session.commit()
    return cart_item


def update_product_quantity(id_cart, id_product, new_quantity):
    product_cart = ProductCart.query.filter_by(id_cart=id_cart, id_product=id_product).first()
    if product_cart:
        db.session.delete(product_cart)
        db.session.commit()
        return product_cart
    return False

def remove_product_from_cart(id_cart, id_product):
    product_cart = ProductCart.query.filter_by(id_cart=id_cart, id_product=id_product).first()
    if product_cart:
        db.session.delete(product_cart)
        db.session.commit()
        return True
    return False

def cancel_cart(id_cart):
    cart = Cart.query.get(id_cart)
    if cart.status != 'active':
        raise ValueError("Cannot cancel non-active cart")
    
    for item in cart.products:
        item.product.stock += item.reserved_quantity
        item.reserved_quantity = 0 
        
    cart.status = 'cancelled'
    db.session.commit()

def get_products_cart(id_cart):
    return ProductCart.query.filter_by(id_cart=id_cart).all()