from dominio import Tarea
from persistencia import guardar_tarea, obtener_tarea
from app import mostrar_menu

def crear_tarea():
    nombre = input("Nombre de la tarea: ")
    descripcion = input("Descripcion de la tarea: ")
    tarea = Tarea(nombre, descripcion)
    guardar_tarea(tarea)
    
def ver_tareas():
    tareas = obtener_tarea()
    for tarea in tareas:
        print(f"Tarea: {tarea.nombre}, Descripcion: {tarea.descripcion}")
        
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            crear_tarea()
        elif opcion == 2:
            ver_tareas()
        elif opcion == 3:
            print("El programa ha finalizado")
            break