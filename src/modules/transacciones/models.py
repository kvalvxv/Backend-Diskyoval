from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from src import db 


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id_transaction = db.Column(db.Integer, primary_key=True)
    id_cart = db.Column(db.Integer, db.ForeignKey('cart.id_cart'), nullable=False)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')
    
    
    cart = relationship('Cart', back_populates='transaction')
   
    def to_dict(self):
        return {
            'id_transaction': self.id_transaction,
            'id_cart': self.id_cart,
            'transaction_date': self.transaction_date,
            'status': self.status
            
        }
