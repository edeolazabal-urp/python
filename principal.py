import subprocess
import tkinter as tk 


def abrir_programa1():
    subprocess.Popen(["python", "subprograma.py"])

def abrir_programa2():
    pass

def abrir_programa3():
    pass

def abrir_programa4():
    pass

root = tk.Tk()

root.title("Barra de menus en Tk")
root.config(width=400, height=300)
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
menu_archivo.add_command(
    label="Programa 1",
    accelerator="Ctrl+N",
    command=abrir_programa1
)
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
root.config(menu=barra_menus)

tk.Button(root, text="Programa 1", command=abrir_programa1).pack()
tk.Button(root, text="Programa 2", command=abrir_programa2).pack()
tk.Button(root, text="Programa 3", command=abrir_programa3).pack()
tk.Button(root, text="Programa 4", command=abrir_programa4).pack()
root.mainloop()