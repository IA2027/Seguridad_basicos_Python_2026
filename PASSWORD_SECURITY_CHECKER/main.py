
import string

print("=" * 45)
print("       PASSWORD SECURITY CHECKER")
print("=" * 45)

password = input("\nIntroduce una contraseña: ")

score = 0
recommendations = []

# Comprobar longitud
if len(password) >= 12:
    score += 2
else:
    recommendations.append("Utiliza al menos 12 caracteres.")

# Comprobar mayusculas
if any(c.isupper() for c in password):
    score += 1
else:
    recommendations.append("Agrega letras mayusculas.")

# Comprobar minusculas
if any(c.islower() for c in password):
    score += 1
else:
    recommendations.append("Agrega letras minusculas.")

# Comprobar numeros
if any(c.isdigit() for c in password):
    score += 1
else:
    recommendations.append("Agrega numeros.")

# Comprobar caracteres especiales
if any(c in string.punctuation for c in password):
    score += 1
else:
    recommendations.append("Agrega caracteres especiales.")

# Mostrar resultados
print("\n" + "=" * 45)
print("             ANALISIS")
print("=" * 45)

print(f"\nLongitud: {len(password)} caracteres")
print(f"Puntuacion: {score}/6")

if score <= 2:
    print("\nSEGURIDAD: DEBIL")
elif score <= 4:
    print("\nSEGURIDAD: MEDIA")
else:
    print("\nSEGURIDAD: FUERTE")

if recommendations:
    print("\nRECOMENDACIONES:")
    for item in recommendations:
        print("-", item)
else:
    print("\nExcelente. Cumple todos los criterios.")

print("\n" + "=" * 45)
print("       ANALISIS FINALIZADO")
print("=" * 45)
