# Implementa herencia multiple
class Vehiculo:
    def desplazar(self):
        print("Se desplaza en VEHICULO")

class Terrestre:
    def desplazar(self):
        print("Se desplaza por medio TERRESTRE")

class Acuatico:
    def desplazar(self):
        print("Se desplaza por medio ACUATICO")

# Clases que reciben herencia multiple
class Automovil(Terrestre, Vehiculo):
    def desplazar(self):
        super().desplazar()
        print ("Usa un AUTOMOVIL")

class Barco(Acuatico, Vehiculo):
    def desplazar(self):
        super().desplazar()
        print ("Usa un BARCO")
        
auto = Automovil()
auto.desplazar()

barco = Barco()
barco.desplazar()
