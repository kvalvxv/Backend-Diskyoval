from src import db
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'products'
    
    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    product_carts = relationship('ProductCart', back_populates='product')
    
    def to_dict(self):
        return {
            'id_product':self.id_product,
            'name':self.name,
            'description':self.description,
            'price':self.price,
            'stock':self.stock,
        }