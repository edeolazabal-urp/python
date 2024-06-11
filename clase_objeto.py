class Persona:
    nombre = ""
    edad = 0
    
    def __init__(self, *args):
        if len(args) == 0:
            self.edad = 22
            self.nombre = "Juan"
        else:
            self.nombre = args[0]
            self.edad = args[1]
        
    def mostrar(self, *args):
        if len(args) == 0:
            return (self.nombre + '(' + str(self.edad) + ')')
        else:
            return (self.nombre + '(' + str(self.edad) + '),' + args[0] + ' - ' + args[1])
    
jose = Persona()
print (jose.mostrar('Trujillo', 'Perú'))
print (jose.mostrar())

maria = Persona('Maria',25)
print (maria.mostrar('Madrid', 'España'))