# Backend-Diskyoval

🛒 **API Backend for E-commerce Platform** - Flask-based REST API with SQLAlchemy ORM

## 📋 Overview

Backend-Diskyoval is a comprehensive e-commerce backend API built with Python Flask, designed to handle products, users, shopping carts, transactions, and contact management. This backend follows clean architecture principles with modular structure and includes robust validation, error handling, and security features.

## 🚀 Features

- **👤 User Management** - Registration, authentication with JWT
- **🛍️ Product Catalog** - CRUD operations for products
- **🛒 Shopping Cart** - Cart management and product reservations
- **💳 Transactions** - Order processing and payment handling
- **📞 Contact Management** - Customer service and support
- **🔐 Security** - JWT authentication, password hashing, input validation
- **📊 Database** - SQLAlchemy ORM with MySQL support
- **🔄 Migrations** - Flask-Migrate for schema management

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, Flask 3.0+
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: JWT (Flask-JWT-Extended)
- **Security**: Werkzeug password hashing
- **Migrations**: Flask-Migrate
- **CORS**: Flask-CORS
- **Validation**: Custom input validators
- **Logging**: Python logging system

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL server
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/kvalvxv/Backend-Diskyoval.git
   cd Backend-Diskyoval
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file in root directory
   touch .env
   ```
   
   Add the following to your `.env` file:
   ```env
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-here
   MYSQL_USER=your-mysql-username
   MYSQL_PASSWORD=your-mysql-password
   MYSQL_HOST=localhost
   MYSQL_DB=your-database-name
   PORT=4001
   ```

5. **Set up database**
   ```bash
   # Initialize migrations (first time only)
   flask db init
   
   # Create migration
   flask db migrate -m "Initial migration"
   
   # Apply migrations
   flask db upgrade
   ```

## 🏃‍♂️ Running the Application

### Method 1: Using startup scripts (Recommended)
```bash
# Windows
./start.bat

# Linux/Mac
./start.sh
```

### Method 2: Manual startup
```bash
# Make sure virtual environment is activated
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Linux/Mac

# Run the application
python run.py
```

The server will start at `http://127.0.0.1:4001`

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:4001
```

### Endpoints

#### 🔐 Authentication
- `POST /clients/register` - User registration
- `POST /clients/login` - User login (returns JWT token)
- `GET /clients/protected_route` - Protected route example

#### 👥 Users
- `GET /clients/users` - Get all users (admin only)
- `GET /clients/users?search=term` - Search users

#### 🛍️ Products
- `GET /products/` - Get all products
- `GET /products/<id>` - Get product by ID
- `POST /products/new_product` - Create new product
- `PUT /products/<id>` - Update product
- `DELETE /products/<id>` - Delete product

#### 🛒 Shopping Cart
- `GET /cart/` - Get user's cart
- `POST /cart/add` - Add item to cart
- `PUT /cart/update/<id>` - Update cart item
- `DELETE /cart/remove/<id>` - Remove item from cart

#### 💳 Transactions
- `GET /transactions/` - Get transaction history
- `POST /transactions/create` - Create new transaction
- `GET /transactions/<id>` - Get transaction details

#### 📞 Contact
- `POST /contact/send` - Send contact message
- `GET /contact/messages` - Get all messages (admin)

### Authentication

Protected endpoints require JWT token in headers:
```bash
Authorization: Bearer <your-jwt-token>
```

## 🏗️ Project Structure

```
Backend-Diskyoval/
├── src/
│   ├── __init__.py          # Flask app factory
│   ├── config.py           # Configuration management
│   ├── app.py             # Alternative entry point
│   └── modules/          # Business logic modules
│       ├── clientes/       # User management
│       ├── productos/     # Product management
│       ├── carrito/       # Shopping cart
│       ├── transacciones/ # Transactions
│       └── contacto/      # Contact management
├── test/                 # Test files
├── migrations/           # Database migrations
├── logs/                # Application logs
├── venv/                # Virtual environment
├── start.bat            # Windows startup script
├── start.sh             # Linux/Mac startup script
├── AGENTS.md            # Developer guidelines
├── .gitignore           # Git ignore file
├── requirements.txt      # Python dependencies
└── run.py              # Main application entry point
```

## 🔧 Development

### Code Style
This project follows the guidelines in [AGENTS.md](AGENTS.md) which includes:
- Import conventions
- Naming patterns
- Database model standards
- Route definitions
- Error handling patterns
- Security practices

### Database Migrations
```bash
# Create new migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade

# Rollback migration
flask db downgrade
```

### Testing
```bash
# Run tests (when implemented)
pytest

# Run with coverage
pytest --cov=src
```

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'flask'**
   ```bash
   # Activate virtual environment
   source venv/Scripts/activate  # Windows
   # or
   source venv/bin/activate      # Linux/Mac
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

2. **Database connection errors**
   - Check your `.env` file configuration
   - Ensure MySQL server is running
   - Verify database credentials and privileges

3. **JWT token errors**
   - Check your JWT_SECRET_KEY in `.env`
   - Ensure token is included in Authorization header

### Logs
Check application logs in `logs/` directory for detailed error information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please follow the coding standards outlined in [AGENTS.md](AGENTS.md).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Repository**: https://github.com/kvalvxv/Backend-Diskyoval
- **Issues**: https://github.com/kvalvxv/Backend-Diskyoval/issues

## 🙏 Acknowledgments

- Flask team for the excellent framework
- SQLAlchemy community for the amazing ORM
- All contributors who helped improve this project

---

**Built with ❤️ for the e-commerce community**