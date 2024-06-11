from ast import Pass
from enum import auto
import hm_retorno as hm
#from tkinter import * # importar todas las clase de la lib tkinter
from tkinter import Frame, IntVar, StringVar, Tk, messagebox, ttk, Radiobutton

# definicion de empleado se hara en la funcion que llama el boton calcular

# Funciones a usar
def desplazar():
    empleado = None
    match miTipo.get():
        case 'Vehiculo':
            vehiculo = hm.Vehiculo()
            miMensaje.set(vehiculo.desplazar())
            messagebox.showinfo('Vehiculo', vehiculo.desplazar())
            
        case 'Terrestre':
            terrestre = hm.Terrestre()
            miMensaje.set(terrestre.desplazar())
            messagebox.showinfo('Terrestre', terrestre.desplazar())
            
        case 'Acuatico':
            acuatico = hm.Acuatico()
            miMensaje.set(acuatico.desplazar())
            messagebox.showinfo('Acuatico', acuatico.desplazar())
            
        case 'Automovil':
            automovil = hm.Automovil()
            miMensaje.set(automovil.desplazar())
            messagebox.showinfo('Automovil', automovil.desplazar())
            
        case 'Barco':
            barco = hm.Barco()
            miMensaje.set(barco.desplazar())
            messagebox.showinfo('Barco', barco.desplazar())
            
    match opcion.get():
        case 0:
            messagebox.showinfo('Opcion', 'Escogio FALSO')
        case 1:
            messagebox.showinfo('Opcion', 'Escogio VERDADERO')

            

   
def salir():
    raiz.destroy()
    
def opciones():
    messagebox.showinfo ("Mensaje", "Opcion escogida: " + str(opcion.get()))


    

raiz = Tk()  # ventana
# atributos de la raiz
raiz.title('Herencia Multiple - Vehiculos')
raiz.resizable(True, True)
raiz.iconbitmap('atleta.ico')
raiz.geometry('550x350')
raiz.config(bg='#75C3D9')

miFrame = Frame(raiz, width=500,height=300) #, padding=10)
#miFrame.pack(side='right', 'left', 'top', padx=1', pady=10')
miFrame.config(bg="#FFDD33")
miFrame.grid() #  permite el manejo de filas y columnas en el grid

# Estilo para formatear algunos widgets como el boton
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = '#3390FF', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','#3390FF')])

# variables
miTipo = StringVar()
miMensaje = StringVar()
opcion = IntVar()

# combo box
comboTipo = ttk.Combobox(miFrame, textvariable=miTipo, width = 36,
    state="readonly",
    values=["Vehiculo", "Terrestre", "Acuatico", "Automovil", "Barco"]
).grid(row=0, column=1, padx=10, pady=10)

Radiobutton(miFrame, variable=opcion, value=1, text="Verdadero", background='#FFDD33').grid(row=3, column=0, padx=10, pady=10)
Radiobutton(miFrame, variable=opcion, value=0, text="False", background='#FFDD33').grid(row=3, column=1, padx=10, pady=10)

# Etiquetas
etiqTipo = ttk.Label(miFrame, text= "Tipo: ", background='#FFDD33').grid(row=0, column=0, padx=10, pady=10)
etiqMensaje = ttk.Label(miFrame, text= "",textvariable=miMensaje,  background='#FFDD33').grid(row=2, column=0, padx=10, pady=10)


# Botones
botonCalcular = ttk.Button(miFrame, text="Desplazar", command=desplazar, padding=10).grid (row=1, column=0)

botonSalir = ttk.Button(miFrame, text="Salir", command=salir, padding=10).grid (row=1, column=1)

raiz.mainloop()  # final