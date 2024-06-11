# llamar a atleta con interface tkinter
from atleta_20241 import *
from tkinter import Frame, StringVar, Tk, messagebox, ttk, Button, Entry, Label, Scrollbar, Text
from tkinter.scrolledtext import ScrolledText

raiz = Tk()

# Propiedades de raiz
raiz.title('Registro de Atleta')
raiz.iconbitmap('olimpiada.ico')
raiz.resizable(True, True)
raiz.geometry('950x550')
raiz.config(bg='#abdbe3')

miFrame = ttk.Frame(raiz, width=1200, height=600, padding=10)
#miFrame.pack(side='right', 'left', 'top', padx=1', pady=10')
miFrame.grid()


style = ttk.Style()
style.configure("BY.TLabel", foreground="blue", background="yellow")

style.theme_use("clam")
style.configure("miFrame", background="#ccc", font="Comic Sans MS 20")

l1 = ttk.Label(text="Test", style="BY.TLabel")
l2 = ttk.Label(text="Test", style="BY.TLabel")


# Variables
atl = Atleta()
miNombre = StringVar()
miPeso = StringVar()
miEstatura = StringVar()


atl = Atleta()

# Funciones
def asignar():
   # miNombre.set("Juan Perez")
   # miNombre.set(cajaNombre.get())
   # miPeso.set(cajaPeso.get()

   atl.nombre = miNombre.get()
   atl.peso = float(miPeso.get())
   atl.estatura = float(miEstatura.get())

   messagebox.showinfo('Mensaje', 'Nombre: {0}. Peso: {1} Estatura: {2} IMC: {3}'.format(atl.nombre, 
                        str(atl.peso), str(atl.estatura), str(round(atl.calcular_imc(),2))))
   # messagebox.showinfo('Mensaje', 'Nombre: {0}. Peso: {1}'.format(miNombre.get(), miPeso.get()))


def mensaje():
    atl.comer()
    atl.comer()
    rpta = messagebox.askyesno("Confirmar", "Responder si o No")
    if rpta:
        messagebox.showinfo("Mensaje", "respondio SI: {0} Peso: {1}".format(atl.nombre, str(atl.peso)))
    else:
        messagebox.showwarning("Mensaje", "respondio NO")



#Etiquetas
nombreLabel = ttk.Label(miFrame, text="Nombre:", justify="left").grid(row=0, column=0, sticky="e", padx=10, pady=10)

pesoLabel = ttk.Label(miFrame, text="Peso:").grid(row=1, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = ttk.Label(miFrame, text="Comentario:").grid(row=2, column=0, sticky="e", padx=10, pady=10)

# Cajas de texto
cajaNombre = ttk.Entry(miFrame, textvariable=miNombre, width=36, foreground="blue", justify="left").grid(row=0, column=1, padx=10, pady=10)

cajaPeso = ttk.Entry(miFrame, textvariable=miPeso, width=36, foreground="blue", justify="right").grid(row=1, column=1, padx=10, pady=10)
#cajaPeso = ttk.Entry(miFrame, textvariable=miPeso, width=36, foreground="blue", show="*", justify="left").grid(row=1, column=1, padx=10, pady=10)

cajaEstatura = ttk.Entry(miFrame, textvariable=miEstatura, width=36, foreground="blue", justify="right").grid(row=2, column=1, padx=10, pady=10)


textoComentario = ScrolledText(miFrame, width=26, height=5).grid(row=3, column=1, padx=10, pady=10)

# Botones
botonEnvio = ttk.Button(miFrame, text="Enviar", command=mensaje, padding=10).grid (row=4, column=0)

botonMostrar = ttk.Button(miFrame, text="Mostrar", command=asignar, padding=10).grid (row=4, column=1)

raiz.mainloop()
