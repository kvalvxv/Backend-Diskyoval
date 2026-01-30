from werkzeug.security import generate_password_hash

def generar_hash(password_plano):
    hash_bcrypt = generate_password_hash(password_plano)
    print(f"Contraseña: {password_plano}")
    print(f"Hash Bcrypt: {hash_bcrypt}")

# Ejemplo de uso
generar_hash("admin")
