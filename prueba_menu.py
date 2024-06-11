from tkinter import Button, Entry, Label, Menu, StringVar, Tk, messagebox


def corre_mensaje(dato):
    campo = dato # texto_caja.get()
    messagebox.showinfo('Prueba', 'Dato ingresado:' + campo)
       
ventana = Tk()
ventana.title('Ejemplo de uso de Menu')

texto_caja = StringVar()

etiq1 = Label(ventana, text='Dat0: ').grid(row=0, column=0, padx=10, pady=5)
caja1 = Entry(ventana, textvariable=texto_caja, foreground='blue', width=18, justify='left').grid(row=0, column=1, padx=10, pady=5)

boton1 = Button(ventana, text='Ejecutar', command=lambda:corre_mensaje(texto_caja.get())).grid(row=0, column=2, padx=10, pady=5)

#3. Creamos una instancia del Menu Principal
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

#4. Crear un menu desplegable
archivo_menu = Menu(barra_menu, tearoff=False)

#5. Agregar elementos al menu desplegable
#archivo_menu.add_command(label="Alumno", command=lambda:messagebox.showinfo("Alumno", "Datos del alumno"))
archivo_menu.add_command(label="Alumno", command=lambda:messagebox.showinfo("Alumno", "Datos del Alumno"))
archivo_menu.add_command(label="Curso", command=lambda:messagebox.showinfo("Curso", "Datos del curso"))
archivo_menu.add_command(label="Listar Alumnos", command=lambda:messagebox.showinfo("Alumno", "LListar Alumnos"))
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=lambda:messagebox.showinfo("Salir", "Salir"))

#6.Agregar el menu desplegable
barra_menu.add_cascade(label="Opciones", menu=archivo_menu)
ventana.mainloop()