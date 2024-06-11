#from tkinter import * # importar todas las clase de la lib tkinter
import tkinter as tk
from tkinter import Frame, PhotoImage, StringVar, Tk, messagebox, ttk

import empleado as emp

# definicion de empleado se hara en la funcion que llama el boton calcular
# atl1 = atl.Atleta()

# Funciones a usar
def calcular():
    empleado = None
    match miTipo.get():
        case 'Empleado':
            empleado = emp.Empleado()
            empleado.salario = miSalario.get()
            messagebox.showinfo('Empleados', 
                      'El salario es: ' + str(empleado.calcular_salario()))
        case 'Gerente':
            empleado = emp.Gerente()
            empleado.salario = miSalario.get()
            empleado.bono = miBono.get()
            messagebox.showinfo('Empleados', 
                      'El salario es: ' + str(empleado.calcular_salario()))
            
        case 'EmpleadoDeOficina':
            empleado = emp.EmpleadoDeOficina()
            empleado.salario = miSalario.get()
            empleado.tarifa = miTarifa.get()
            empleado.horas_extras = miHoras_extras.get()
            messagebox.showinfo('Empleados', 
                      'El salario es: ' + str(empleado.calcular_salario()))

   
def salir():
    raiz.destroy()

    

raiz = Tk()  # ventana
# atributos de la raiz
raiz.title('Empleados')
raiz.resizable(True, True)
raiz.iconbitmap('olimpiada.ico')
raiz.geometry('750x550')
raiz.config(bg='#75C3D9')

miFrame = Frame(raiz, width=700, background='#F8C471',
                    height=500)
#miFrame.pack(side='right', 'left', 'top', padx=1', pady=10')
miFrame.grid()

# variables
miSalario = StringVar()
miBono = StringVar()
miTarifa = StringVar()
miHoras_extras = StringVar()
miTipo = StringVar()

# cajas de texto
cajaSalario = ttk.Entry(miFrame, textvariable=miSalario, width=36,
                       foreground="blue", justify="right").grid(row=0, column=1, padx=10, pady=10)

cajaBono = ttk.Entry(miFrame, textvariable=miBono, width=36, 
                     foreground="blue", justify="right").grid(row=1, column=1, padx=10, pady=10)

cajaTarifa = ttk.Entry(miFrame, textvariable=miTarifa, width=36, 
                         foreground="blue", justify="right").grid(row=2, column=1, padx=10, pady=10)

cajaHoras_extras = ttk.Entry(miFrame, textvariable=miHoras_extras, width=36, 
                         foreground="blue", justify="right").grid(row=3, column=1, padx=10, pady=10)


comboTipo = ttk.Combobox(miFrame, textvariable=miTipo, width = 36,
    state="readonly",
    values=["Empleado", "Gerente", "EmpleadoDeOficina"]
).grid(row=4, column=1, padx=10, pady=10)

# Etiquetas
etiqSalario = ttk.Label(miFrame, text= "Salario: ", background='#F8C471').grid(row=0, column=0, padx=10, pady=10)

etiqBono = ttk.Label(miFrame, text= "Bono: ", background='#F8C471').grid(row=1, column=0, padx=10, pady=10)

etiqTarifa = ttk.Label(miFrame, text= "Tarifa: ", background='#F8C471').grid(row=2, column=0, padx=10, pady=10)

etiqHoras_extras = ttk.Label(miFrame, text= "Horas Extras: ", background='#F8C471').grid(row=3, column=0, padx=10, pady=10)

etiqTipo = ttk.Label(miFrame, text= "Tipo: ", background='#F8C471').grid(row=4, column=0, padx=10, pady=10)


# Botones
img_boton = PhotoImage(file="calculadora.png").subsample(16)
botonCalcular = ttk.Button(miFrame, text="Calcular", command=calcular, padding=10, image=img_boton, compound=tk.TOP).grid (row=5, column=0)

img2_boton = PhotoImage(file="salida.png").subsample(16)
botonSalir = ttk.Button(miFrame, text="Salir", command=salir, padding=10, image=img2_boton, compound=tk.TOP).grid (row=5, column=1)

raiz.mainloop()  # final