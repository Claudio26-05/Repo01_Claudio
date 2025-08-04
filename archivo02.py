#Generando una Calculadora basica en python

num01=int(input("Ingresa un numero bro:\n"))
num02=int(input("Ingresa otro numero bro:\n"))

op= input("Ingresa el operador:\n1.+\n2.-\n3./\n4.*\n")
def resultado(a,b,c):
    if c in ["+", "-", "/", "*"]:
        if c=="+":
            return a+b
        elif c=="-":
            return a-b
        elif c=="/":
            return a/b
        elif c=="*":
            return a*b
    else:
        print("Elige los signos, no los números!!!")

print (f"El resultado de la suma de {num01} y {num02} es : {resultado(num01,num02,op)}")


