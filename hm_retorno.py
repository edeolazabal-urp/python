# Implementa herencia multiple
class Vehiculo:
    def desplazar(self):
        return "Se desplaza en VEHICULO\n"

class Terrestre:
    def desplazar(self):
        return "Se desplaza por medio TERRESTRE\n"

class Acuatico:
    def desplazar(self):
        return "Se desplaza por medio ACUATICO\n"

# Clases que reciben herencia multiple
class Automovil(Terrestre, Vehiculo):
    def desplazar(self):
        return  super().desplazar() + "Usa un AUTOMOVIL"

class Barco(Acuatico, Vehiculo):
    def desplazar(self):
        return  super().desplazar() + "Usa un BARCO"
        
auto = Automovil()
print (auto.desplazar())

barco = Barco()
print(barco.desplazar())
