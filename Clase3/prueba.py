class Motor:
    def start(self):
        return ("Motor encendido")
    
class Coche:
    def __init__(self, motor):
        self.motor = motor
        
    def arrancar(self):
        print(self.motor.start())

motor = Motor()
coche = Coche(motor)
coche.arrancar()