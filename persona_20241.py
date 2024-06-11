class Persona:
    nombre = ''
    peso = 0

    def __init__(self, *args):
        match len(args):
            case 0:
                self.nombre = '<<indefinido>>'
                self.peso = 50
            case 2:
                self.nombre = args[0]
                self.peso = args[1]

    def comer(self):
        self.peso += 1

    def correr(self, *args):
        match len(args):
            case 0:
                self.peso -= 1
            case 1:
                self.peso -= (args[0] / 10) * 2

# probar
# per = Persona('Maria', 55)
# per.correr(40)

# print (per.nombre, per.peso)