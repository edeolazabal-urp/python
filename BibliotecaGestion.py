import tkinter as tk
from tkinter import ttk, messagebox
import os

def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return [line.strip().split(';') for line in f.readlines()]
    return []

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        for dato in datos:
            f.write(';'.join(dato) + '\n')

class BibliotecaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Biblioteca Gestión")
        self.geometry("800x600")
        
       
        self.crear_menu()
        

        self.crear_treeview()
        

        self.crear_botones()
        

        self.libros = cargar_datos('libros.txt')
        self.usuarios = cargar_datos('usuarios.txt')
        self.prestamos = cargar_datos('prestamos.txt')
        
        self.actualizar_treeview()
    
    def crear_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Registrar Libro", command=self.registrar_libro)
        archivo_menu.add_command(label="Registrar Usuario", command=self.registrar_usuario)
        archivo_menu.add_command(label="Registrar Préstamo", command=self.registrar_prestamo)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
    
    def crear_treeview(self):
        columns = ("ID", "Tipo", "Título/Nombre", "Autor/Correo", "Fecha Préstamo", "Fecha Devolución")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(expand=True, fill='both')
    
    def crear_botones(self):
        boton_frame = tk.Frame(self)
        boton_frame.pack(pady=10)
        
        tk.Button(boton_frame, text="Eliminar Libro", command=self.eliminar_libro).pack(side=tk.LEFT, padx=10)
        tk.Button(boton_frame, text="Eliminar Usuario", command=self.eliminar_usuario).pack(side=tk.LEFT, padx=10)
        tk.Button(boton_frame, text="Eliminar Préstamo", command=self.eliminar_prestamo).pack(side=tk.LEFT, padx=10)
    
    def actualizar_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for libro in self.libros:
            self.tree.insert("", tk.END, values=(libro[0], "Libro", libro[1], libro[2], "", ""))
        for usuario in self.usuarios:
            self.tree.insert("", tk.END, values=(usuario[0], "Usuario", usuario[1], usuario[2], "", ""))
        for prestamo in self.prestamos:
            self.tree.insert("", tk.END, values=(prestamo[0], "Préstamo", prestamo[1], prestamo[2], prestamo[3], prestamo[4]))
    
    def registrar_libro(self):
        def guardar_libro():
            id_libro = id_entry.get()
            titulo = titulo_entry.get()
            autor = autor_entry.get()
            
            if id_libro and titulo and autor:
                self.libros.append([id_libro, titulo, autor])
                guardar_datos('libros.txt', self.libros)
                self.actualizar_treeview()
                registrar_win.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        
        registrar_win = tk.Toplevel(self)
        registrar_win.title("Registrar Libro")
        
        tk.Label(registrar_win, text="ID Libro:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(registrar_win)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="Título:").grid(row=1, column=0, padx=10, pady=10)
        titulo_entry = tk.Entry(registrar_win)
        titulo_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="Autor:").grid(row=2, column=0, padx=10, pady=10)
        autor_entry = tk.Entry(registrar_win)
        autor_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Button(registrar_win, text="Guardar", command=guardar_libro).grid(row=3, column=0, columnspan=2, pady=10)
    
    def registrar_usuario(self):
        def guardar_usuario():
            id_usuario = id_entry.get()
            nombre = nombre_entry.get()
            correo = correo_entry.get()
            
            if id_usuario and nombre and correo:
                self.usuarios.append([id_usuario, nombre, correo])
                guardar_datos('usuarios.txt', self.usuarios)
                self.actualizar_treeview()
                registrar_win.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        
        registrar_win = tk.Toplevel(self)
        registrar_win.title("Registrar Usuario")
        
        tk.Label(registrar_win, text="ID Usuario:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(registrar_win)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
        nombre_entry = tk.Entry(registrar_win)
        nombre_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="Correo:").grid(row=2, column=0, padx=10, pady=10)
        correo_entry = tk.Entry(registrar_win)
        correo_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Button(registrar_win, text="Guardar", command=guardar_usuario).grid(row=3, column=0, columnspan=2, pady=10)
    
    def registrar_prestamo(self):
        def guardar_prestamo():
            id_prestamo = id_entry.get()
            id_libro = libro_entry.get()
            id_usuario = usuario_entry.get()
            fecha_prestamo = prestamo_entry.get()
            fecha_devolucion = devolucion_entry.get()
            
            if id_prestamo and id_libro and id_usuario and fecha_prestamo and fecha_devolucion:
                self.prestamos.append([id_prestamo, id_libro, id_usuario, fecha_prestamo, fecha_devolucion])
                guardar_datos('prestamos.txt', self.prestamos)
                self.actualizar_treeview()
                registrar_win.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
        
        registrar_win = tk.Toplevel(self)
        registrar_win.title("Registrar Préstamo")
        
        tk.Label(registrar_win, text="ID Préstamo:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(registrar_win)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="ID Libro:").grid(row=1, column=0, padx=10, pady=10)
        libro_entry = tk.Entry(registrar_win)
        libro_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="ID Usuario:").grid(row=2, column=0, padx=10, pady=10)
        usuario_entry = tk.Entry(registrar_win)
        usuario_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="Fecha Préstamo:").grid(row=3, column=0, padx=10, pady=10)
        prestamo_entry = tk.Entry(registrar_win)
        prestamo_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(registrar_win, text="Fecha Devolución:").grid(row=4, column=0, padx=10, pady=10)
        devolucion_entry = tk.Entry(registrar_win)
        devolucion_entry.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Button(registrar_win, text="Guardar", command=guardar_prestamo).grid(row=5, column=0, columnspan=2, pady=10)

    def eliminar_libro(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un libro para eliminar")
            return
        values = self.tree.item(selected_item, "values")
        if values[1] == "Libro":
            self.libros = [libro for libro in self.libros if libro[0] != values[0]]
            guardar_datos('libros.txt', self.libros)
            self.actualizar_treeview()
        else:
            messagebox.showerror("Error", "Solo se pueden eliminar libros")

    def eliminar_usuario(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un usuario para eliminar")
            return
        values = self.tree.item(selected_item, "values")
        if values[1] == "Usuario":
            self.usuarios = [usuario for usuario in self.usuarios if usuario[0] != values[0]]
            guardar_datos('usuarios.txt', self.usuarios)
            self.actualizar_treeview()
        else:
            messagebox.showerror("Error", "Solo se pueden eliminar usuarios")
    
    def eliminar_prestamo(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un préstamo para eliminar")
            return
        values = self.tree.item(selected_item, "values")
        if values[1] == "Préstamo":
            self.prestamos = [prestamo for prestamo in self.prestamos if prestamo[0] != values[0]]
            guardar_datos('prestamos.txt', self.prestamos)
            self.actualizar_treeview()
        else:
            messagebox.showerror("Error", "Solo se pueden eliminar préstamos")

if __name__ == "__main__":
    app = BibliotecaApp()
    app.mainloop()
