'''
Clases Vehiculo
Fecha: 10/10/2024
'''
class Vehiculo:
    def __init__(self, velocidad_maxima=None):
        if velocidad_maxima is not None:
            self.velocidad_maxima = velocidad_maxima
        else:
            self.velocidad_maxima = 75
    def avanzar(self):
        print ('avanzó')
    def detener(self):
        print ('se detuvo')

class VehiculoAereo(Vehiculo):
    def __init__(self, velocidad_maxima=None):
        super().__init__(velocidad_maxima)
    
    def volar(self):
        print ('voló')  

class VehiculoTerrestre(Vehiculo):
    def __init__(self, velocidad_maxima=None):
        super().__init__(velocidad_maxima)
    
    def retroceder(self):
        print ('retrocedió')       
