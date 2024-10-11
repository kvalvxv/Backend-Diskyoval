from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from datetime import datetime
from sqlalchemy.orm import relationship
from src import db 

class Cart(db.Model):
    __tablename__= 'cart'
    
    id_cart = Column(Integer, primary_key=True, autoincrement=True)
    id_client = Column(Integer, ForeignKey('clients.id_client'))
    creation_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default='active')
    
    
    #Relaciones de la base de datos 
    
    owner = relationship('User', back_populates='carts')
    products = relationship('ProductCart', back_populates='cart')
    transaction = relationship('Transaction', uselist=False, back_populates='cart')
    
    
class ProductCart(db.Model):
    __tablename__ = 'product_cart'
    
    id_product_cart = Column(Integer, primary_key=True, autoincrement=True)
    id_cart = Column(Integer, ForeignKey('cart.id_cart'))
    id_product = Column(Integer, ForeignKey('products.id_product'))
    quantity =Column(Integer)
    reserved_quantity = Column(Integer, default=0)
    

#Relaciones de la base de datos 
    product = relationship('Product', back_populates='product_carts')
    cart = relationship('Cart', back_populates='products')