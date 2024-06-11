# Importa los elementos del archivo 
import persona_20241 as pers


# Crea la clase con herencia
class Atleta(pers.Persona):
    estatura = 0

    def __init__(self, *args):
        match len(args):
            case 0:
                pers.Persona.__init__(self)  # invocamos al constructor de la clase base sin argumentos
                self.estatura = 1.5
            case 3:
                pers.Persona.__init__(self, args[0], args[1])
                self.estatura = args[2]

    def calcular_imc(self):
         return (self.peso * 1.0) / (self.estatura * self.estatura)
     


