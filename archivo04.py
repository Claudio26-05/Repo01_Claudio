# =========================
# 1. Variables y operaciones
# =========================
# Pide al usuario su nombre y edad, y muestra un mensaje:
# "Hola [nombre], el próximo año tendrás [edad+1] años"

nom=input("Ingresa tu nombre:\n")
edad=int(input("Ingresa tu edad:\n"))

def Saludo(a,b):
    return print(f"Hola {a},el próximo año tendrás {b+1} años")

Saludo(nom,edad)