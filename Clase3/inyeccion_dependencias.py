class Servicio:
    def __init__(self, repositorio):
        self.repositorio = Repositorio()
        
    def procesar(self):
        datos = self.repositorio.obtener_datos()
        print(f"Procesando {datos}")    
        
class Repositorio:
    def obtener_datos(self):
        return "Datos del repositorio"

repositorio = Repositorio()
servicio = Servicio(repositorio) # Servicio no depende ahora de repositorio para funcionar
servicio.procesar()