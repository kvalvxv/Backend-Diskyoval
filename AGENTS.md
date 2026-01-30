# Backend-Diskyoval - Agent Guidelines

## Overview
This is a Flask-based e-commerce backend API using SQLAlchemy ORM with MySQL database. The codebase follows a modular structure with separate controllers, models, and routes for each business domain.

## Development Commands

### Running the Application
```bash
# Method 1: Use startup scripts
./start.bat          # Windows
./start.sh           # Linux/Mac

# Method 2: Manual activation
source venv/Scripts/activate  # Windows
python run.py

# Alternative development server
python src/app.py
```

### Database Management
```bash
# Initialize Flask-Migrate (if not already done)
flask db init

# Create new migration
flask db migrate -m "description of changes"

# Apply migrations to database
flask db upgrade

# Downgrade to previous migration
flask db downgrade
```

### Environment Setup
```bash
# Create virtual environment (if needed)
python -m venv venv

# Install dependencies
source venv/Scripts/activate  # Windows
pip install -r requirements.txt

# Alternative activation (Unix/Linux)
source venv/bin/activate
```

### Testing
Currently no formal test framework is configured. When implementing tests:
```bash
# Run all tests (when pytest is added)
pytest

# Run specific test file
pytest test/test_specific.py

# Run with coverage
pytest --cov=src
```

## Code Style & Conventions

### Project Structure
```
src/
├── __init__.py          # Flask app factory and database initialization
├── config.py           # Configuration class with environment variables
├── app.py              # Alternative app entry point
└── modules/            # Business domain modules
    ├── productos/      # Products management
    ├── clientes/       # User/client management
    ├── carrito/        # Shopping cart functionality
    ├── transacciones/  # Transaction handling
    └── contacto/       # Contact management
```

### Module Structure
Each module follows this pattern:
```
module_name/
├── __init__.py
├── models.py          # SQLAlchemy model definitions
├── controller.py      # Business logic functions
└── routes.py          # Flask route definitions
```

### Import Conventions
```python
# Standard library imports first
import os
from datetime import datetime

# Third-party imports
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Local imports
from src import db
from .models import ModelName
from .controller import function_name
```

### Database Models
- Use descriptive table names with `__tablename__`
- Primary keys follow pattern `id_modelname` (e.g., `id_product`, `id_client`)
- Use `db.Column` with appropriate types and constraints
- Include `nullable=False` for required fields
- Define relationships using `relationship()` with proper `back_populates`
- Always include a `to_dict()` method for JSON serialization

Example:
```python
class Product(db.Model):
    __tablename__ = 'products'
    
    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    product_carts = relationship('ProductCart', back_populates='product')
    
    def to_dict(self):
        return {
            'id_product': self.id_product,
            'name': self.name,
            'price': self.price
        }
```

### Controller Functions
- Keep controllers separate from routes
- Functions should accept parameters, not request objects
- Return model objects or None for failures
- Handle database commits and rollbacks appropriately
- Use descriptive function names

Example:
```python
def get_product_by_id(product_id):
    return Product.query.filter_by(id_product=product_id).first()

def create_product(data):
    try:
        new_product = Product(
            name=data['name'],
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product
    except Exception as e:
        db.session.rollback()
        raise e
```

### Route Definitions
- Use Flask Blueprints with meaningful names
- Include proper HTTP methods and route prefixes
- Handle JSON responses consistently
- Use appropriate HTTP status codes
- Implement proper error handling with try/catch blocks

Example:
```python
product_bp = Blueprint('products', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def get_all_products_route():
    try:
        products = get_all_products()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

### Error Handling
- Use try/catch blocks in routes for database operations
- Return consistent error response format: `{'error': str(e)}`
- Use appropriate HTTP status codes (400, 401, 404, 500)
- Implement database rollback on failed operations
- Log errors using `print()` statements (upgrade to logging in production)

### Naming Conventions
- **Files**: lowercase with underscores (snake_case)
- **Classes**: PascalCase (CamelCase) - e.g., `Product`, `User`
- **Functions/Variables**: snake_case - e.g., `get_product_by_id`, `user_data`
- **Constants**: UPPER_CASE - e.g., `SECRET_KEY`, `DATABASE_URI`
- **Database columns**: snake_case - e.g., `id_product`, `creation_date`

### Authentication & Security
- Use Flask-JWT-Extended for authentication
- Protect sensitive routes with `@jwt_required()` decorator
- Store passwords as hashes using `werkzeug.security.generate_password_hash`
- Use environment variables for sensitive configuration
- Implement proper JWT token validation callbacks

### Environment Configuration
- Use `.env` file for environment variables
- Configuration loaded in `src/config.py` using `python-dotenv`
- Required environment variables:
  - `SECRET_KEY`
  - `JWT_SECRET_KEY`
  - `MYSQL_USER`
  - `MYSQL_PASSWORD`
  - `MYSQL_HOST`
  - `MYSQL_DB`
  - `PORT` (defaults to 4001)

### JSON Response Standards
- Use `jsonify()` for all API responses
- Include appropriate HTTP status codes
- For successful operations: return data with 200 status
- For creation: return 201 status
- For errors: return `{'error': str(e)}` with appropriate error code

### Code Quality Notes
- Avoid debug `print()` statements in production code
- Use consistent indentation (4 spaces)
- Add docstrings to complex functions
- Keep functions focused on single responsibilities
- Validate input data before processing

## Common Patterns

### Creating New Module
1. Create module directory under `src/modules/`
2. Add `__init__.py` file
3. Create `models.py` with SQLAlchemy models
4. Create `controller.py` with business logic
5. Create `routes.py` with Flask routes
6. Register blueprint in `src/__init__.py`

### Adding New Endpoint
1. Add controller function in appropriate `controller.py`
2. Add route with Blueprint in `routes.py`
3. Include proper error handling
4. Return consistent JSON responses

### Database Schema Changes
1. Modify models in `models.py`
2. Generate migration: `flask db migrate -m "description"`
3. Review generated migration file
4. Apply migration: `flask db upgrade`

This codebase prioritizes simplicity and clarity over complex abstractions, making it maintainable and easy to understand for new developers.