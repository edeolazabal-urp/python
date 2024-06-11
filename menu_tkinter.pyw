#1. Importamos tkinter
import tkinter as tk
from math import e
from tkinter import Frame, StringVar, Tk, messagebox, ttk

import evaluaciones_clases as ev

# Listas
Lista_Alumnos = []
Lista_Cursos = []
Lista_Evaluacion = []

# Funciones
def agrega_alumno():
    retorno = ev.agregar_alumno(Lista_Alumnos, miIdAlumno.get(), miNombreAlumno.get())
    # acciones para agregar un nuevo alumno
    if retorno:
        messagebox.showinfo("Alumno", "alumno ingresado con exito")
    else:
        messagebox.showinfo("Alumno", "No se pudo ingresar los datos del alumno")
        
def listar_alumnos():
    # Agregar elementos
    tree.delete(*tree.get_children())
    i = 0
    for elem in Lista_Alumnos:
        i+=1   
        tree.insert("", tk.END, text=f"{i}", values=(f"{elem.codigo_alumno}", f"{elem.nombre_alumno}"))
    
    messagebox.showinfo("Lista de Alumnos", ev.imprime_lista_alumnos(Lista_Alumnos))
       

## Variables


#2. Crear la ventana principal
raiz = Tk()
raiz.title=("Ejemplo de menu desplegable")

miIdAlumno = StringVar()
miNombreAlumno = StringVar()
miIdCurso = StringVar()
miNombreCurso = StringVar()
miNota = StringVar()

raiz.resizable(True, True)
raiz.iconbitmap('olimpiada.ico')
raiz.geometry('750x550')
raiz.config(bg='#75C3D9')

miFrame = Frame(raiz, width=700,height=500) #, padding=10)
#miFrame.pack(side='right', 'left', 'top', padx=1', pady=10')
miFrame.config(bg="#FFDD33")
miFrame.grid() #  permite el manejo de filas y columnas en el grid


#3. Creamos una instancia del Menu Principal
barra_menu = tk.Menu(raiz)
raiz.config(menu=barra_menu)

#4. Crear un menu desplegable
archivo_menu = tk.Menu(barra_menu, tearoff=False)

#5. Agregar elementos al menu desplegable
#archivo_menu.add_command(label="Alumno", command=lambda:messagebox.showinfo("Alumno", "Datos del alumno"))
archivo_menu.add_command(label="Alumno", command=agrega_alumno)
archivo_menu.add_command(label="Curso", command=lambda:messagebox.showinfo("Curso", "Datos del curso"))
archivo_menu.add_command(label="Listar Alumnos", command=listar_alumnos)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=lambda:raiz.quit())

#6.Agregar el menu desplegable
barra_menu.add_cascade(label="Opciones", menu=archivo_menu)

# Dejinir otros widgets del formulario
# cajas de texto
cajaIdAlumno = ttk.Entry(miFrame, textvariable=miIdAlumno, width=36,
                       foreground="blue", justify="right").grid(row=0, column=1, padx=10, pady=10)

cajaNombreAlumno = ttk.Entry(miFrame, textvariable=miNombreAlumno, width=36, 
                     foreground="blue", justify="right").grid(row=1, column=1, padx=10, pady=10)

cajaIdCurso = ttk.Entry(miFrame, textvariable=miIdCurso, width=36,
                     foreground="blue",  justify="right").grid(row=2, column=1, padx=10, pady=10)

cajaNombreCurso = ttk.Entry(miFrame, textvariable=miNombreCurso, width=36, 
                         foreground="blue", justify="right").grid(row=3, column=1, padx=10, pady=10)

cajaNota = ttk.Entry(miFrame, textvariable=miNota, width=36, 
                         foreground="blue", justify="right").grid(row=4, column=1, padx=10, pady=10)

# Etiquetas
etiqIdAlumno = ttk.Label(miFrame, text= "Id Alumno: ", background='#FFDD33').grid(row=0, column=0, padx=10, pady=10)

etiqNombreAlumno = ttk.Label(miFrame, text= "Nombre: ", background='#FFDD33').grid(row=1, column=0, padx=10, pady=10)

etiqIdCurso = ttk.Label(miFrame, text= "Id Curso: ", background='#FFDD33').grid(row=2, column=0, padx=10, pady=10)

etiqNombreCurso = ttk.Label(miFrame, text= "Nombre: ", background='#FFDD33').grid(row=3, column=0, padx=10, pady=10)

etiqNota = ttk.Label(miFrame, text= "Nota: ", background='#FFDD33').grid(row=4, column=0, padx=10, pady=10)

# Crear el widget ttk.Treeview con dos columnas
tree = ttk.Treeview(raiz, columns=("id", "nombre"))

# Definir el encabezado de las columnas
tree.heading("#0", text="Índice")
tree.heading("id", text="Codigo")
tree.heading("nombre", text="Nombre")

# Agregar elementos
#for i in range(10):
#    tree.insert("", tk.END, text=f"Elemento {i}", values=(f"Dato1-{i}", f"Dato2-{i}"))

# Agregar elementos
tree.delete()
for elem in Lista_Alumnos:   
    tree.insert("", tk.END, text="Datos del alumno", values=(f"{elem.codigo_alumno}", f"{elem.nombre_alumno}"))


# Empaquetar el widget ttk.Treeview en la ventana principal
# tree.pack(expand=True, fill="both")
tree.grid(row=4, column=0, padx=10, pady=10)

#7. ejecutar el bucle principal
raiz.mainloop()
