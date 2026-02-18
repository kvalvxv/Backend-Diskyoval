from .models import Product
from src import db
from src.utils.cloudinary_config import upload_image, delete_image

def get_product_by_id(product_id):
    return Product.query.filter_by(id_product=product_id).first()

def get_all_products():
    products = Product.query.all()
    return [product.to_dict() for product in products]

def create_product(product_data, image_file=None):
    try:
        image_result = None
        if image_file:
            image_result = upload_image(image_file)
            if not image_result.get('success'):
                raise Exception(image_result.get('error'))
        
        new_product = Product(
            name=product_data['name'],
            price=product_data['price'],
            stock=product_data['stock'],
            description=product_data['description'],
            image_url=image_result['url'] if image_result else None,
            image_public_id=image_result['public_id'] if image_result else None
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict()
    except Exception as e:
        db.session.rollback()
        raise e

def update_product(product_id, data, new_image=None):
    product = get_product_by_id(product_id)
    if product:
        old_public_id = product.image_public_id
        
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        
        if new_image:
            if old_public_id:
                delete_image(old_public_id)
            
            image_result = upload_image(new_image)
            if image_result.get('success'):
                product.image_url = image_result['url']
                product.image_public_id = image_result['public_id']
        
        db.session.commit()
        return product
    return None

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        if product.image_public_id:
            delete_image(product.image_public_id)
        
        db.session.delete(product)
        db.session.commit()
        return product
    return None