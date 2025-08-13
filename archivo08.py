# =========================
# 5. Funciones
# =========================
# Crea una función area_circulo(radio) que devuelva el área
PI = 3.14 

def area_circulo(radio):
    return PI * (radio ** 2)  

radio = float(input("Ingresa el radio:\n"))
print(f"El área del círculo es: {area_circulo(radio)}")
