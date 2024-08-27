import ./a funciones-1.py

def nombre_user(): #Metodo SOLID cada modulo tiene una resposabilidad - Este modulo pide el nombre y retorna el nombre
    nombre = input("Como te llamas: ")
    return nombre
def edad_user(): # Este modulo pide la edad y retorna la edad
    edad = int(input("Que edad tienes: "))
    return edad
def calculo(edad): # Este modulo pide la edad y retorna el valor de la edad
    total = edad + 10
    return total
edad = edad_user() # Guardo el dato del metodo en una variable param reutilizar
print(f"Tu nombre es {nombre_user()} y tu edad actual es {edad}. Tu edad en 10 años es de: {calculo(edad)}") # Invocamos los retornos en el print

# Para importar otro archivo se pone el nombre del mismo para poder traer la funcion que se requiere