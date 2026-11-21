
import hashlib
import os

print("=" * 50)
print("          FILE INTEGRITY MONITOR")
print("=" * 50)

# Funcion para generar hash SHA256
def calculate_hash(filename):

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


# Archivo que queremos controlar
filename = "documento.txt"

# Archivo donde guardamos el hash original
hash_file = "integrity_hash.txt"

if not os.path.exists(filename):

    print("\nERROR: No existe documento.txt")

    exit()


# Generar hash actual
current_hash = calculate_hash(filename)

print("\nArchivo:", filename)

print("\nHash SHA-256:")
print(current_hash)


# Comprobar si existe un hash anterior
if not os.path.exists(hash_file):

    with open(hash_file, "w") as file:
        file.write(current_hash)

    print("\n[REGISTRO] Huella digital guardada.")

else:

    with open(hash_file, "r") as file:
        original_hash = file.read().strip()

    print("\nComparando integridad...")

    if current_hash == original_hash:

        print("\n[SEGURO] El archivo no ha cambiado.")

    else:

        print("\n[ALERTA] EL ARCHIVO FUE MODIFICADO.")

print("\nAnalisis finalizado.")
print("=" * 50)
