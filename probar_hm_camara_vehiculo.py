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
    
# Prueba
## Camara
largo = int(input('Ingrese el largo: '))
ancho = int(input('Ingrese el ancho: '))

c1 = Camara(largo, ancho)  # crear el objet

print ('largo:',c1.largo, 'ancho:',c1.ancho)  # valores de los atributos
print (c1.tomar_foto())  # ejecutar metodo

## Vehiculo
velocidad_maxima = int(input('Ingrese el velocidad maxima: '))

v1 = Vehiculo(velocidad_maxima)

print ('Velocidad maxima: ', v1.velocidad_maxima)
print(v1.avanzar())
print(v1.detener())

## Camara Digital
capacidad = int(input('Ingrese la capacidad de la camara: '))

c2 = Digital(largo, ancho, capacidad)

print ('Capacidad: ', c2.capacidad)
print(c2.tomar_foto())

## Camara Analogica
numero_tomas = int(input('Ingrese el numero de tomas de la camara: '))

c3 = Analogica(largo, ancho, numero_tomas)

print ('Capacidad: ', c3.numero_tomas)
print(c3.revelar())

## Vehiculo Aereo
v2 = Aereo(velocidad_maxima)

print(v2.volar())

## Vehiculo Terrestre
v2 = Terrestre(velocidad_maxima)

print(v2.retroceder())

## Dron Camara Digital
dron_d = DronDigital(largo, ancho, capacidad, velocidad_maxima)

print(dron_d.tomar_video())

## Dron Camara Analogica
altura_maxima = int(input('Ingrese la altura maxima que puede alcanzar: '))

dron_a = DronAnalogico(largo, ancho, numero_tomas, velocidad_maxima, altura_maxima)

print('Altura maxima: ', dron_a.altura_maxima)
print(dron_a.tomar_foto())
print(dron_a.volar())
print(dron_a.revelar())

## Dron Camara Digital
duracion_maxima = int(input('Ingrese la duracion maxima en horas: '))
auto_d = AutoCamaraDigital(largo, ancho, capacidad, velocidad_maxima, duracion_maxima)

print('Duracion maxima: ', duracion_maxima)
print(dron_d.tomar_foto())
print(dron_d.volar())
print(dron_d.tomar_video())

## Auto Camara Analogica
ubicacion = input('Ingrese ubicacion de la camara en el vehiculo: ')

auto_a = AutoCamaraAnalogica(largo, ancho, numero_tomas, velocidad_maxima, ubicacion)

print('Ubicacion: ', auto_a.ubicacion)
print(auto_a.tomar_foto())
print(auto_a.avanzar())
print(auto_a.retroceder())

## Auto Camara Digital
duracion_maxima = int(input('Ingrese la duracion maxima en horas: '))
auto_d = AutoCamaraDigital(largo, ancho, capacidad, velocidad_maxima, duracion_maxima)

print('Duracion maxima: ', duracion_maxima)
print(auto_d.reproducir_video())
print(auto_d.retroceder())
print(auto_d.detener())



    