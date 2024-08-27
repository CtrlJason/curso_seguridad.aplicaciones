#calculadora

user = input("Escriba la operacion que quiere que haga la calculadora + o - : ")

if user == "+":
    num1 = int(input("Escriba el primer numero que desea sumar: "))
    num2 = int(input("Escriba el segundo numero que desea sumar: "))
    resultado = num1 + num2
elif user == "-":
    num1 = int(input("Escriba el primer numero que desea restar: "))
    num2 = int(input("Escriba el segundo numero que desea restar: "))
    resultado = num1 - num2

print(f"El resultado de la operacion es: {resultado}")

def calcular(a,b, opcion):
    if user == "+":
        num1 = int(input("Escriba el primer numero que desea sumar: "))
        num2 = int(input("Escriba el segundo numero que desea sumar: "))
        resultado = num1 + num2
    elif user == "-":
        num1 = int(input("Escriba el primer numero que desea restar: "))
        num2 = int(input("Escriba el segundo numero que desea restar: "))
        resultado = num1 - num2
    if user == "*":
        num1 = int(input("Escriba el primer numero que desea sumar: "))
        num2 = int(input("Escriba el segundo numero que desea sumar: "))
        resultado = num1 * num2
    elif user == "/":
        num1 = int(input("Escriba el primer numero que desea restar: "))
        num2 = int(input("Escriba el segundo numero que desea restar: "))
        resultado = num1 / num2
def datoUser ():
    x = int(input("Escriba un numero: "))
    return x

print(f"El resultado de la operacion es: {resultado}")