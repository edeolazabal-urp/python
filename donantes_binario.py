import pickle

# Generar datos para los archivos donante1 y donante2

class Donante:
    def __init__(self, nombre, zona, donacion):
        self.nombre = nombre
        self.zona = zona
        self.donacion = donacion
    def __str__(self):
        return (f'Donante (nombre={self.nombre}, zona={self.zona}, donacion={self.donacion})')
    
class Resumen:
    def __init__(self, zona, total):
        self.zona = zona
        self.total = total
    def __str__(self):
        return (f'Resumen (zona={self.zona}, total={self.total})')

    
donante1 = [Donante('Juan', 1, 100),
            Donante('Pedro', 1, 125),
            Donante('Jose', 2, 150),
            Donante('Maria', 1, 40)]
donante2 = [Donante('Andres', 2, 210),
            Donante('Rosa', 1, 130),
            Donante('Carlos', 3, 45)]

def generar_datos_csv():
    def generar_csv(nombre_archivo, arreglo_datos):
        with open(nombre_archivo, 'w') as arch:
            for donante in arreglo_datos:
                arch.write(f'{donante.nombre};{donante.zona};{donante.donacion}\n')
    generar_csv('donante1.csv', donante1)
    generar_csv('donante2.csv', donante2)
        
   
def convertir_csv_a_bin():
    def generar_binario(nombre_archivo):
        with open(f'{nombre_archivo}.csv', 'r') as arch:
            with open(f'{nombre_archivo}.bin', 'wb') as arch_bin:
                pickle.dump(arch.read(), arch_bin)
    generar_binario('donante1')
    generar_binario('donante2')          
                
def leer_archivos_bin_generar_resumen_csv():
    def leer_binario(nombre_archivo):
        with open(f'{nombre_archivo}', 'rb') as arch_bin:
            datos = pickle.load(arch_bin)
            print (datos)
            return datos
    def encuentra_zona(valor, arreglo):
        for i in range(len(arreglo)):
            if arreglo[i].zona == valor:
                return i
        return -1
    def genera_resumen_csv(d3):
        res = []
        print(d3)
        filas = d3.split('\n')
        for donante in filas:
            campos = donante.strip('\n').split(';')
            if len(campos) == 1:
                break
            don = Donante(campos[0], campos[1], campos[2])
            print(don)
            # pregunta si zona ya existe
            posicion = encuentra_zona(don.zona, res)
            if posicion == -1:  # si no existe, total = donacion
               res.append(Resumen(don.zona, int(don.donacion)))
            else:  # si ya existe, total += donacion
               res[posicion].total += int(don.donacion)
        print("Resumen:") 
        # Genera el archivo resumen.csv
        with open ('resumen.csv', 'w') as arch:
            for r in res:
                arch.write(f'{r.zona};{r.total}\n')
                print (r)
        return res
           
    d1, d2, resumen = [], [], []
    d1 = leer_binario('donante1.bin')
    d2 = leer_binario('donante2.bin')
    d3 = f'{d1}{d2}'
    genera_resumen_csv(d3)  

def convertir_resumen_csv_a_bin():
    # Poner el csv en un arreglo de objetos
    resumen = []
    with open ('resumen.csv', 'r') as arch:
        for elem in arch:
            parte = elem.strip('\n').split(';')
            resumen.append(Resumen (parte[0], int(parte[1])))
    print('Contenido del csv como arreglo')
    for i in range(len(resumen)):
        print(resumen[i])  
    # Grabe el archivo binario con el contenido del arreglo
    with open('resumen.bin', 'wb') as arch_bin:
        pickle.dump(resumen, arch_bin)
    
def mostrar_resumen_bin():
    with open('resumen.bin', 'rb') as arch_bin:
        resumen = pickle.load(arch_bin)
        print('Resumen del archivo binario')
        for elem in resumen:
            print (f'{elem.zona}\t\t{elem.total}')

generar_datos_csv()
convertir_csv_a_bin()
leer_archivos_bin_generar_resumen_csv()
convertir_resumen_csv_a_bin()
mostrar_resumen_bin()