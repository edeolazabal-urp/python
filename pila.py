class Pila:
    def __init__(self):
        self.lista=[]
        
    def poner(self, x):
        self.lista= self.lista+[x]
            
    def sacar(self):
        if not self.vacia():
            del self.lista[-1]
            
    def tope(self):
        if not self.vacia():
            return self.lista[-1]
            
    def mostrar(self):
        return self.lista
        
    def vacia(self):
        return len(self.lista) == 0
            
            
# Prueba
p1 = Pila()
p1.poner(1)
p1.poner(2)
print(p1.mostrar())
p1.poner('a')
p1.poner('b')
p1.poner(True)
print(p1.mostrar())
p1.sacar()
print(p1.mostrar())
p1.poner([1, 'Lima'])
print(p1.mostrar())
print(p1.tope())
print(p1.vacia())


