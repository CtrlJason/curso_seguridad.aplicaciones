
def HomeScreen():
    print("Bienvenido a la universidad\n")
    nombre = input("Escriba su nombre: ")
    apellido = input("Escriba su apellido: ")
    edad = int(input("Escriba su edad: "))
    return nombre, apellido, edad

class AppUniversidad:
    def __init__(self, servicio_estudiante):
        self.servicio_estudiante = servicio_estudiante
        
    def crear_estudiante(self):
        self.servicio_estudiante = HomeScreen()
        return self.servicio_estudiante
    
class RegistroEstudiantes:
    def __init__(self, estudiantes):
        self.estudiantes = estudiantes
        
    def estudiantes_guardados(self):
        self.estudiantes.append(AppUniversidad.crear_estudiante)
        return self.estudiantes
registro = RegistroEstudiantes()

if __name__ == "__main__":
    HomeScreen()
    registro.estudiantes_guardados()
    print(registro.estudiantes_guardados)