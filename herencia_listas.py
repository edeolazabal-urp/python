class Lista:
    def __init__(self):
        self.lista = []
        
    def poner(self,x):
        # self.lista += [x]
        self.lista.append(x)
    def sacar(self):
        pass
    def mostrar(self):
        return self.lista
    def primero(self):
        if not self.vacio():
            return self.lista[0]
    def ultimo(self):
        if not self.vacio():
            return self.lista[-1]
    def vacio(self):
        return len(self.lista) == 0
    
class Pila(Lista):
    def sacar(self):
        if not self.vacio():
           #del self.lista[-1]
            self.lista.pop()
            
class Cola(Lista):
    def sacar(self):
        if not self.vacio():
            #del self.lista[0]
            self.lista.pop(0)
            
# Probar
c = Cola()
c.poner('1')
c.poner('2')
c.poner('3')
print(']Cola: ',c.mostrar())
print('Primero: ',c.primero())
print('Ultimo: ',c.ultimo())
c.sacar()
print ('---')
print('Cola: ',c.mostrar())
print('Primero: ',c.primero())
print('Ultimo: ',c.ultimo())

p = Pila()
p.poner('a')
p.poner('b')
p.poner('c')
print('Pila: ',p.mostrar())
print('Primero: ',p.primero())
print('Ultimo: ',p.ultimo())
p.sacar()
print ('---')
print('Pila: ',p.mostrar())
print('Primero: ',p.primero())
print('Ultimo: ',p.ultimo())



    
