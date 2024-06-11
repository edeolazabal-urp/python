#1. Importar modulo tkinter
import tkinter as tk
from tkinter import messagebox

#2. Crear una ventana principal
root = tk.Tk()
root.title("Ejemplo de Menú")

#3. Crea una instancia de Menu y la agrega a la ventana principal
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

#4. Crear un menu despleagable
archivo_menu = tk.Menu(barra_menu, tearoff=0)

#5. Agrega elementos al menu desplegable
archivo_menu.add_command(label="Abrir", command=lambda: messagebox.showinfo("Mensaje", "Abrir archivo"))
archivo_menu.add_command(label="Guardar", command=lambda: messagebox.showinfo("Mensaje", "Guardar archivo"))
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

#6. Agrega el menu desplegable a la barra de menu principal
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)

#7. Ejecuta el bucle pricipal
root.mainloop()






