# 📋 Backend-Diskyoval - Installation Requirements

## ⚠️ IMPORTANT: Migration is NOT enough!

The backend requires several setup steps beyond database migration for proper functionality.

## 🔧 Complete Setup Process

### 1. Database Setup (Required)

```bash
# Install MySQL server if not already installed
# Ubuntu/Debian: sudo apt install mysql-server
# macOS: brew install mysql
# Windows: Download from mysql.com

# Create database
mysql -u root -p
CREATE DATABASE diskyoval_db;
CREATE USER 'diskyoval_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON diskyoval_db.* TO 'diskyoval_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 2. Environment Configuration (Required)

Create `.env` file with ALL required variables:

```env
# Database Configuration
MYSQL_HOST=localhost
MYSQL_USER=diskyoval_user
MYSQL_PASSWORD=your_password
MYSQL_DB=diskyoval_db

# Security Keys (REQUIRED - generate these!)
SECRET_KEY=your-random-secret-key-here-min-32-chars
JWT_SECRET_KEY=your-jwt-secret-key-here-min-32-chars

# Server Configuration
PORT=4001
```

### 3. Generate Security Keys (Required)

Run these scripts to generate secure keys:

```bash
# Generate SECRET_KEY
python generateJwt_key.py  # Use one of the generated keys for SECRET_KEY

# Or generate manually (RECOMMENDED)
python -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(32))"
```

### 4. Database Migration (Required)

```bash
# Activate virtual environment first!
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Linux/Mac

# Run migrations
flask db upgrade
```

### 5. Create Admin User (Required for testing)

The backend needs at least one admin user. Use the provided script:

```bash
python generate_passwordsAdmin.py
```

This will create:
- Admin user with hashed password
- Test users if configured

## 🚨 Common Setup Issues

### Issue 1: Missing Security Keys
```
RuntimeError: SECRET_KEY must be set
```
**Solution**: Generate and add SECRET_KEY and JWT_SECRET_KEY to `.env`

### Issue 2: Database Connection Failed
```
sqlalchemy.exc.OperationalError: (2003, "Can't connect to MySQL server")
```
**Solutions**:
- MySQL server is not running
- Wrong credentials in `.env`
- Database doesn't exist
- User doesn't have privileges

### Issue 3: Migration Errors
```
alembic.util.exc.CommandError: Can't locate revision identified by '760194d395da'
```
**Solution**: Database not initialized, run:
```bash
flask db stamp 760194d395da
flask db upgrade
```

## ✅ Verification Checklist

After setup, verify everything works:

### 1. Test Database Connection
```bash
python -c "from src import db; print('✅ Database connection successful')"
```

### 2. Test Server Startup
```bash
python run.py
# Should show: * Running on http://127.0.0.1:4001
```

### 3. Test Registration Endpoint
```bash
curl -X POST http://127.0.0.1:4001/clients/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test",
    "lastname": "User", 
    "email": "test@example.com",
    "password": "password123",
    "phone": "1234567890",
    "user_type": "cliente"
  }'
```

### 4. Test Login
```bash
curl -X POST http://127.0.0.1:4001/clients/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

## 📝 TL;DR (Quick Setup)

```bash
# 1. Clone and setup
git clone https://github.com/kvalvxv/Backend-Diskyoval.git
cd Backend-Diskyoval
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# 2. Generate security keys
python -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(32))"
python -c "import secrets; print('JWT_SECRET_KEY=' + secrets.token_urlsafe(32))"

# 3. Create .env file (replace with your values)
cat > .env << EOF
MYSQL_HOST=localhost
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=diskyoval_db
SECRET_KEY=paste_generated_key_here
JWT_SECRET_KEY=paste_generated_key_here
PORT=4001
EOF

# 4. Setup database and run migrations
# (Create database and user in MySQL first!)
flask db upgrade

# 5. Create admin user
python generate_passwordsAdmin.py

# 6. Run server
python run.py
```

## ⚠️ Security Notes

- **NEVER** commit `.env` file to version control
- **ALWAYS** use different SECRET_KEY and JWT_SECRET_KEY
- **CHANGE** default admin passwords in production
- **USE** HTTPS in production environments

## 🤝 What to Expect After Setup

- ✅ Backend runs on `http://127.0.0.1:4001`
- ✅ Users can register and login
- ✅ Products can be managed via API
- ✅ Shopping cart functionality works
- ✅ JWT authentication protects endpoints
- ✅ Input validation prevents bad data
- ✅ Logging captures errors and events