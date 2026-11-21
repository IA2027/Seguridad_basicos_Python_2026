
import subprocess
import ipaddress
import time

print("=" * 45)
print("             IP SCANNER")
print("=" * 45)

print("\nEscaner de dispositivos de red local")

# Solicitar rango de red
network = input(
    "\nIntroduce los primeros 3 bloques de tu IP (ej: 192.168.1): "
)

# Validar direccion
try:
    parts = network.split(".")

    if len(parts) != 3:
        raise ValueError

    if not all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        raise ValueError

    print("\nIniciando escaneo...")
    print("-" * 45)

except ValueError:
    print("\nERROR: Direccion de red incorrecta.")
    exit()

active_devices = []

# Escanear direcciones IP
for number in range(1, 255):

    ip = f"{network}.{number}"

    result = subprocess.run(
        ["ping", "-n", "1", "-w", "300", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:

        active_devices.append(ip)

        print(f"[ACTIVO] {ip}")

# Mostrar resultados
print("\n" + "=" * 45)
print("             RESULTADOS")
print("=" * 45)

print(f"\nDispositivos encontrados: {len(active_devices)}")

if active_devices:
    print("\nDirecciones IP activas:")

    for device in active_devices:
        print("-", device)

else:
    print("\nNo se encontraron dispositivos.")

print("\nEscaneo finalizado.")
print("=" * 45)
