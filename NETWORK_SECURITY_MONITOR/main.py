
import subprocess
from datetime import datetime

print("=" * 55)
print("             NETWORK SECURITY MONITOR")
print("=" * 55)

print("\nConsultando conexiones TCP...")
print("-" * 55)

try:
    # Consultar conexiones de Windows
    result = subprocess.run(
        ["netstat", "-ano", "-p", "tcp"],
        capture_output=True,
        text=True,
        encoding="cp850",
        errors="replace"
    )

    if result.returncode != 0:
        print("Error al consultar las conexiones.")
        exit()

    connections = []

    # Leer resultados
    for line in result.stdout.splitlines():

        parts = line.split()

        if len(parts) >= 5 and parts[0] == "TCP":

            local_ip = parts[1]
            remote_ip = parts[2]
            state = parts[3]
            pid = parts[4]

            connections.append({
                "local": local_ip,
                "remote": remote_ip,
                "state": state,
                "pid": pid
            })

    # Mostrar conexiones
    established = 0
    listening = 0

    for connection in connections:

        print("\nIP LOCAL:", connection["local"])
        print("IP REMOTA:", connection["remote"])
        print("ESTADO:", connection["state"])
        print("PID:", connection["pid"])

        if connection["state"] == "ESTABLISHED":
            established += 1

        elif connection["state"] == "LISTENING":
            listening += 1

        print("-" * 55)

    # Informe final
    print("\n" + "=" * 55)
    print("                  INFORME")
    print("=" * 55)

    print("\nTotal de conexiones TCP:", len(connections))
    print("Conexiones establecidas:", established)
    print("Puertos en escucha:", listening)

    # Guardar informe
    with open(
        "network_report.txt",
        "w",
        encoding="utf-8"
    ) as report:

        report.write("NETWORK SECURITY MONITOR\n")
        report.write(str(datetime.now()) + "\n\n")

        for connection in connections:

            report.write(
                f"LOCAL: {connection['local']}\n"
            )

            report.write(
                f"REMOTA: {connection['remote']}\n"
            )

            report.write(
                f"ESTADO: {connection['state']}\n"
            )

            report.write(
                f"PID: {connection['pid']}\n"
            )

            report.write("-" * 40 + "\n")

        report.write("\nRESUMEN\n")
        report.write(
            f"Total: {len(connections)}\n"
        )

        report.write(
            f"Establecidas: {established}\n"
        )

        report.write(
            f"En escucha: {listening}\n"
        )

    print("\n[OK] Informe guardado.")
    print("Archivo: network_report.txt")

except FileNotFoundError:
    print("\nERROR: No se encontro netstat.")

except Exception as error:
    print("\nERROR:", error)

print("\nMONITOREO FINALIZADO.")
print("=" * 55)
