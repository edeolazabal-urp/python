# Superclase
class Empleado:
    # atributos
    salario = 0
    # Constructor
    # metodos
    def calcular_salario(self):
        return float(self.salario)

# Sub-Clases 
class Gerente(Empleado):
    bono = 0
    def calcular_salario(self):
        return (float(super().calcular_salario()) + float(self.bono))
    
class EmpleadoDeOficina(Empleado):
    tarifa = 0
    horas_extras = 0
    def calcular_salario(self):
        return (float(super().calcular_salario()) + (float(self.tarifa) * float(self.horas_extras)))
    


# Prueba
'''
emp1 = Empleado()
emp1.salario = 1000
print (emp1.calcular_salario() )
input('Visualizar los resultados')

emp2 = Gerente()
emp2.salario = 3000
emp2.bono = 500
print (emp2.calcular_salario() )
input('Visualizar los resultados')

emp3 = EmpleadoDeOficina()
emp3.salario = 2000
emp3.tarifa = 10
emp3.horas_extras = 25
print (emp3.calcular_salario() )
'''


