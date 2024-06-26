

import csv
import io
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from pandas import DataFrame

def agregar_datos_csv(nombre, pc1, pc2, pc3, pc4):
    with open('datos.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([nombre, pc1, pc2, pc3, pc4])

def generar_grafico(pc1, pc2, pc3, pc4):
    evaluaciones = ['PC1', 'PC2', 'PC3', 'PC4']
    notas = [int(pc1), int(pc2), int(pc3), int(pc4)]
    plt.bar(evaluaciones, notas)
    plt.xlabel('Calificación')
    plt.ylabel('Nota obtenida')
    plt.title('Desempeño en el semestre')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.clf()  # Corrige el método plt.clf() con paréntesis
    return buffer

def agregar_datos():
    nombre = entry_nombre.get()
    pc1 = entry_pc1.get()
    pc2 = entry_pc2.get()
    pc3 = entry_pc3.get()
    pc4 = entry_pc4.get()
    agregar_datos_csv(nombre, pc1, pc2, pc3, pc4)
    entry_nombre.delete(0, tk.END)
    entry_pc1.delete(0, tk.END)
    entry_pc2.delete(0, tk.END)
    entry_pc3.delete(0, tk.END)
    entry_pc4.delete(0, tk.END)
    actualizar_grafico(pc1, pc2, pc3, pc4)

def actualizar_grafico(pc1, pc2, pc3, pc4):
    notas = [int(pc1), int(pc2), int(pc3), int(pc4)]
    barras.clear()
    barras.bar(['PC1', 'PC2', 'PC3', 'PC4'], notas)
    barras.set_xlabel('Evaluaciones')
    barras.set_ylabel('Notas')
    barras.set_title('Desempeño en el semestre')
    bar1.draw()

window = tk.Tk()

label_nombre = tk.Label(window, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(window)
entry_nombre.pack()

label_pc1 = tk.Label(window, text="PC1:")
label_pc1.pack()
entry_pc1 = tk.Entry(window)
entry_pc1.pack()

label_pc2 = tk.Label(window, text="PC2:")
label_pc2.pack()
entry_pc2 = tk.Entry(window)
entry_pc2.pack()

label_pc3 = tk.Label(window, text="PC3:")
label_pc3.pack()
entry_pc3 = tk.Entry(window)
entry_pc3.pack()

label_pc4 = tk.Label(window, text="PC4:")
label_pc4.pack()
entry_pc4 = tk.Entry(window)
entry_pc4.pack()

framegraficos = tk.Frame(window, bg="#949292", width="215", height="620")
framegraficos.pack(side="bottom", anchor='n', padx=1, pady=1)

Data1 = {'Evaluaciones': ['PC1','PC2','PC3', 'PC4'], 'Nota': [0,0,0,0]}
df1 = DataFrame(Data1, columns=['Evaluaciones', 'Nota'])

grafico1 = plt.Figure(figsize=(6,5), dpi=50)
barras = grafico1.add_subplot(111)
bar1 = FigureCanvasTkAgg(grafico1, framegraficos)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1.plot(kind='bar', legend=True, ax=barras)

button_agregar = tk.Button(window, text="Agregar Datos", command=agregar_datos)
button_agregar.pack()

window.mainloop()
