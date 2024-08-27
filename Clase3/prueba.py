class Motor:
    def start():
        return "Motor encendido"
    
class Coche:
    def __init__(self, motor):
        self.motor = motor
        
    def arrancar(self):
        print(self.motor)

motor = Motor()
coche = Coche(motor)
coche.arrancar()