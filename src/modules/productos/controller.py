from .models import Product
from src import db

def get_product_by_id(product_id):
    return Product.query.filter_by(id_product=product_id).first()

def get_all_products():
    products = Product.query.all()
    return [product.to_dict() for product in products]

def create_product(product_list):
    results = []
    try:
        for data in product_list:
            new_product = Product(
                name=data['name'],
                price=data['price'],
                stock=data['stock'],
                description=data['description']
            )
            db.session.add(new_product)
            results.append(new_product.to_dict())
        db.session.commit()
        return results
    except Exception as e:
        db.session.rollback()
        raise e

def update_product(product_id, data):
    product = get_product_by_id(product_id)
    if product:
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price =data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        db.session.commit()
        return product
    return None


def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return product
    return None