#from tkinter import * # importar todas las clase de la lib 
try:
    import tkinter as tk
except:
    import tkinter as tk

from tkinter import Frame, IntVar, Radiobutton, StringVar, Tk, messagebox, ttk

import hm_camara_vehiculo as hm

raiz = Tk()  # ventana

# Funciones a usar
dron = None
    
def crear_dron():
    global dron
    match opcion.get():
        case 0:
            #largo, ancho, capacidad, velocidad_maxima
            dron = hm.DronDigital(miLargo.get(), miAncho.get(), miCapacidad.get(), miVelocidadMaxima.get())
            messagebox.showinfo ('Dron Digital','Capacidad: ' + str(dron.capacidad))
            messagebox.showinfo ('Dron Digital',dron.tomar_video())

        case 1:
            #  largo, ancho, numero_tomas, velocidad_maxima, altura_maxima
            dron = hm.DronAnalogico(miLargo.get(),miAncho.get(),miNumeroTomas.get(), miVelocidadMaxima.get(), miAlturaMaxima.get())
            messagebox.showinfo ('Dron Analogico','Altura maxima: '+str(dron.altura_maxima))
            messagebox.showinfo ('Dron Analogico',dron.revelar())

def tomar_foto():
    messagebox.showinfo ('Dron Analogico',dron.tomar_foto())
    
def revelar():
    messagebox.showinfo ('Dron Analogico',dron.revelar())

def tomar_video():
    messagebox.showinfo ('Dron Analogico',dron.tomar_video())
    #botonVideo.config(state=tk.DISABLED)
  
def salir():
    raiz.destroy()

# atributos de la raiz
raiz.title('Herencia Multiple - Drones')
raiz.resizable(True, True)
raiz.iconbitmap('olimpiada.ico')
raiz.geometry('750x350')
raiz.config(bg='#75C3D9')

miFrame = Frame(raiz, width=1200,height=300) #, padding=10)
#miFrame.pack(side='right', 'left', 'top', padx=1', pady=10')
miFrame.config(bg="#FFDD33")
miFrame.grid() #  permite el manejo de filas y columnas en el grid

# Estilo para formatear algunos widgets como el boton
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = '#3390FF', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','#3390FF')])

# variables
miLargo = StringVar()
miAncho = StringVar()
miCapacidad = StringVar()
miNumeroTomas = StringVar()
miVelocidadMaxima = StringVar()
miAlturaMaxima = StringVar()
miMensaje = StringVar()
opcion = IntVar()

# cajas de Texto
cajaLargo = ttk.Entry(miFrame, textvariable=miLargo, width=36,
                       foreground="blue", justify="right").grid(row=1, column=1, padx=10, pady=10)

cajaAncho = ttk.Entry(miFrame, textvariable=miAncho, width=36, 
                     foreground="blue", justify="right").grid(row=2, column=1, padx=10, pady=10)

cajaCapacidad = ttk.Entry(miFrame, textvariable=miCapacidad, width=36, 
                         foreground="blue", justify="right").grid(row=3, column=1, padx=10, pady=10)

cajaNumeroTomas = ttk.Entry(miFrame, textvariable=miNumeroTomas, width=36, 
                         foreground="blue", justify="right").grid(row=1, column=3, padx=10, pady=10)
                         
cajaVelocidadMaxima = ttk.Entry(miFrame, textvariable=miVelocidadMaxima, width=36, 
                         foreground="blue", justify="right").grid(row=2, column=3, padx=10, pady=10)
                         
cajaAlturaMaxima = ttk.Entry(miFrame, textvariable=miAlturaMaxima, width=36, 
                         foreground="blue", justify="right").grid(row=3, column=3, padx=10, pady=10)

# Etiquetas
ttk.Label(miFrame, text= "Largo: ", background='#FFDD33').grid(row=1, column=0, padx=10, pady=10)
ttk.Label(miFrame, text= "Ancho",background='#FFDD33').grid(row=2, column=0, padx=10, pady=10)
ttk.Label(miFrame, text= "Capacidad: ", background='#FFDD33').grid(row=3, column=0, padx=10, pady=10)
ttk.Label(miFrame, text= "Numero de Tomas", background='#FFDD33').grid(row=1, column=2, padx=10, pady=10)
ttk.Label(miFrame, text= "Velocidad Maxima: ", background='#FFDD33').grid(row=2, column=2, padx=10, pady=10)
ttk.Label(miFrame, text= "Altura Maxima: ", background='#FFDD33').grid(row=3, column=2, padx=10, pady=10)

etiqMensaje = ttk.Label(miFrame, text= "",textvariable=miMensaje,  background='#FFDD33').grid(row=5, column=0, padx=10, pady=10)

# Botones
botonFoto = ttk.Button(miFrame, text="Tomar foto", command=tomar_foto, padding=10, width=15).grid (row=4, column=0)
botonRevelar = ttk.Button(miFrame, text="Revelar", command=revelar, padding=10, width=15, state=tk.DISABLED).grid (row=4, column=1)
botonVideo = ttk.Button(miFrame, text="Tomar video", command=tomar_video, padding=10, width=15, state=tk.NORMAL).grid (row=4, column=2)
botonSalir = ttk.Button(miFrame, text="Salir", command=salir, padding=10, width=15).grid (row=4, column=3)

# RadioButton
Radiobutton(miFrame, variable=opcion, value=0, text="Digital", command=crear_dron, background='#FFDD33').grid(row=0, column=0, padx=10, pady=10)
Radiobutton(miFrame, variable=opcion, value=1, text="Analogico", command=crear_dron, background='#FFDD33').grid(row=0, column=1, padx=10, pady=10)

match opcion.get():
    case 0:
        messagebox.showinfo("Digital", "digital")
    #    botonRevelar.config(state=tk.DISABLED)
    #    botonVideo.config(state=tk.NORMAL)
    case 1:
         messagebox.showinfo("analogico", "Analogico")
    #    botonRevelar.config(state=tk.NORMAL)
    #    botonVideo.config(state=tk.DISABLED)

raiz.mainloop()  # final