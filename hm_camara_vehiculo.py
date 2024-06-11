# Implementa herencia multiple para clases derivadas de camaa y vehiculo
class Camara:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def tomar_foto(self):
        return "la camara puede tomar fotos"

class Vehiculo:
    def __init__(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima
        
    def avanzar(self):
        return ('El vehiculo puede AVANZAR')
    def detener(self):
        return ('El vehiculo puede DETENERSE')
    
class Digital(Camara):
    def __init__(self, largo, ancho, capacidad):
        super().__init__(largo, ancho)
        self.capacidad = capacidad
        
class Analogica(Camara):
     def __init__(self, largo, ancho, numero_tomas):
        super().__init__(largo, ancho)
        self.numero_tomas = numero_tomas 
        
     def revelar(self):
         return 'La camara puede revelar fotos'
     
class Aereo(Vehiculo):
     def __init__(self, velocidad_maxima):
        super().__init__(velocidad_maxima)
        
     def volar(self):
         return ('El vehiculo puede VOLAR')
     
class Terrestre(Vehiculo):
     def __init__(self, velocidad_maxima):
        super().__init__(velocidad_maxima)
        
     def retroceder(self):
         return ('El vehiculo puede RETROCEDER')
     
class DronDigital(Digital, Aereo):
    def __init__(self, largo, ancho, capacidad, velocidad_maxima):
        Digital.__init__(self, largo, ancho, capacidad)
        Aereo.__init__(self, velocidad_maxima)
        
    def tomar_video(self):
        return ('El Dron puede TOMAR VIDEOS')
    
class DronAnalogico(Analogica, Aereo):
    def __init__(self, largo, ancho, numero_tomas, velocidad_maxima, altura_maxima):
        Analogica.__init__(self, largo, ancho, numero_tomas)
        Aereo.__init__(self, velocidad_maxima)
        self.altura_maxima = altura_maxima

class AutoCamaraAnalogica(Analogica, Terrestre):
    def __init__(self, largo, ancho, numero_tomas, velocidad_maxima, ubicacion):
        Analogica.__init__(self, largo, ancho,numero_tomas)
        Terrestre.__init__(self, velocidad_maxima)
        self.ubicacion = ubicacion
    
class AutoCamaraDigital(Digital, Terrestre):
    def __init__(self, largo, ancho, capacidad, velocidad_maxima, duracion_maxima):
        Digital.__init__(self, largo, ancho, capacidad)
        Terrestre.__init__(self, velocidad_maxima)
        self.duracion_maxima = duracion_maxima  
        
    def reproducir_video(self):
        return ('El video se puede REPRODUCIR')
    
