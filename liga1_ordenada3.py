# Ordenar la tabla de Posiciones de la Liga 1 del Perú 
# de acuerdo a los puntos y la diferencia de goles, sin usar la función sorted
class Equipo_Liga:
    def __init__(self, nombre, pg, pe, pp, gf, gc):
        self.nombre = nombre
        self.pg = pg
        self.pe = pe
        self.pp = pp
        self.gf = gf
        self.gc = gc
        self.pj = 'PJ'
        self.dg = 'DG'
        self.ptos = 'Ptos'
        if pg.isdigit():
            self.ptos = (int(self.pg) * 3) + (int(self.pe) * 1)
            self.pj = int(self.pg) + int(self.pe) + int(self.pp)
            self.dg = int(self.gf) - int(self.gc)
        
    def __str__(self):
        return f"{self.nombre};{self.pj};{self.pg};{self.pe};{self.pp};{self.gf};{self.gc};{self.dg};{self.ptos}"

datos = []

def entrada():
    # Leer el archivo CSV
    with open("liga1_aleatorio.csv", "r") as arch:
        for linea in arch:
            partes = linea.strip("\n").split(";")
            equipo = Equipo_Liga(partes[0], partes[1], partes[2], partes[3], partes[4], partes[5])
            datos.append(equipo)
 
def proceso():
    for i in range(len(datos)):
        if datos[i].ptos == 'Ptos':
            continue
        for j in range(i + 1, len(datos)):
            if (datos[j].ptos > datos[i].ptos) or (datos[j].ptos == datos[i].ptos and datos[j].dg > datos[i].dg):
                # Intercambiar
                datos[i], datos[j] = datos[j], datos[i] 

def salida():
    with open("liga1_ordenada3.csv", "w") as arch:
        for equipo in datos:
            arch.write(f"{equipo}\n")
            
# Ejecución de las funciones
entrada()
proceso()
salida()
for dato in datos:
    print(dato)