
import socket

print("=" * 45)
print("             PORT SCANNER")
print("=" * 45)

# Solicitar direccion IP
target = input("\nIntroduce una IP para analizar: ")

# Puertos habituales
ports = [21, 22, 25, 53, 80, 443, 3306, 3389, 8080]

open_ports = []

print("\nIniciando analisis...")
print("-" * 45)

# Analizar puertos
try:
    socket.inet_aton(target)

    for port in ports:

        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        client.settimeout(0.5)

        result = client.connect_ex((target, port))

        if result == 0:
            print(f"[ABIERTO] Puerto {port}")
            open_ports.append(port)

        else:
            print(f"[CERRADO/FILTRADO] Puerto {port}")

        client.close()

except OSError:
    print("\nERROR: Direccion IP incorrecta.")

# Resultados
print("\n" + "=" * 45)
print("             RESULTADOS")
print("=" * 45)

print(f"\nPuertos analizados: {len(ports)}")
print(f"Puertos abiertos: {len(open_ports)}")

if open_ports:
    print("\nPuertos encontrados:")
    for port in open_ports:
        print("-", port)
else:
    print("\nNo se encontraron puertos abiertos.")

print("\nAnalisis finalizado.")
print("=" * 45)
