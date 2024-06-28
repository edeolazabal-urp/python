import pickle

import reporte_con_imagen_pdf as reporte


class Notas:
    def __init__(self, pc1, pc2):
        self.pc1 = int(pc1)
        self.pc2= int(pc2)
    def __str__(self):
        return f'Notas ({self.pc1}, {self.pc2})'

with open('notas_pc.bin', 'rb') as arch_bin:
    notas = pickle.load(arch_bin)
    nombres =['Juan Perez', 'Ana Gómez', 'Pedro López', 'María Torres', 'José García', 'Laura Martínez', 'Carlos Rodríguez', 'Sofía Hernández', 'Javier Díaz']  
    
    for i in range(len(notas)):
        nota = Notas(notas[i].pc1, notas[i].pc2)
        reporte.generar_reporte_con_imagen(nombres[i], nota)
    
