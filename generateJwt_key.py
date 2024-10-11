import os
import binascii

# Generar una secret key aleatoria de 24 bytes
secret_key = binascii.hexlify(os.urandom(24)).decode()
print(secret_key)

