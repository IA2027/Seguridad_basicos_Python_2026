
from urllib.parse import urlparse
import ipaddress

print("=" * 50)
print("          PHISHING URL DETECTOR")
print("=" * 50)

url = input("\nIntroduce una URL para analizar: ").strip()

# Palabras sospechosas
suspicious_words = [
    "login",
    "verify",
    "secure",
    "account",
    "password",
    "bank",
    "update",
    "confirm"
]

alerts = []

# Comprobar formato
if not url.startswith(("http://", "https://")):
    url = "https://" + url

parsed = urlparse(url)

domain = parsed.hostname or ""

print("\nAnalizando URL...")
print("-" * 50)

# Comprobar HTTPS
if parsed.scheme != "https":
    alerts.append("La URL no utiliza HTTPS.")

# Comprobar longitud
if len(url) > 100:
    alerts.append("La URL tiene una longitud elevada.")

# Comprobar direccion IP
try:
    ipaddress.ip_address(domain)
    alerts.append("El dominio utiliza una direccion IP.")
except ValueError:
    pass

# Comprobar palabras sospechosas
for word in suspicious_words:
    if word in url.lower():
        alerts.append(
            f"Palabra potencialmente sospechosa: {word}"
        )

# Comprobar cantidad de subdominios
if domain.count(".") >= 4:
    alerts.append("El dominio tiene muchos subdominios.")

# Mostrar resultados
print("\nURL ANALIZADA:")
print(url)

print("\nRESULTADO DEL ANALISIS:")
print("-" * 50)

if alerts:

    print("[ADVERTENCIA] Se encontraron indicadores.")

    for alert in alerts:
        print("-", alert)

    print("\nRIESGO: REQUIERE REVISION")

else:

    print("[INFO] No se detectaron indicadores basicos.")
    print("RIESGO: SIN INDICADORES DETECTADOS")

print("\nAnalisis finalizado.")
print("=" * 50)
