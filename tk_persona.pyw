import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
    
    def comer(self):
        self.peso += 2
    
    def caminar(self):
        self.peso -= 1

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Personas")
        self.personas = []

        # Widgets
        self.nombre_label = tk.Label(root, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=10, pady=10)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        self.peso_label = tk.Label(root, text="Peso:")
        self.peso_label.grid(row=1, column=0, padx=10, pady=10)
        self.peso_entry = tk.Entry(root)
        self.peso_entry.grid(row=1, column=1, padx=10, pady=10)

        self.agregar_button = tk.Button(root, text="Agregar Persona", command=self.agregar_persona)
        self.agregar_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.personas_label = tk.Label(root, text="Personas:")
        self.personas_label.grid(row=3, column=0, padx=10, pady=10)
        self.personas_listbox = tk.Listbox(root)
        self.personas_listbox.grid(row=3, column=1, padx=10, pady=10)
        self.personas_listbox.bind('<<ListboxSelect>>', self.mostrar_persona)

        self.peso_actual_label = tk.Label(root, text="Peso Actual:")
        self.peso_actual_label.grid(row=4, column=0, padx=10, pady=10)
        self.peso_actual_value = tk.Label(root, text="---")
        self.peso_actual_value.grid(row=4, column=1, padx=10, pady=10)

        self.comer_button = tk.Button(root, text="Comer (+2kg)", command=self.comer)
        self.comer_button.grid(row=5, column=0, padx=10, pady=10)

        self.caminar_button = tk.Button(root, text="Caminar (-1kg)", command=self.caminar)
        self.caminar_button.grid(row=5, column=1, padx=10, pady=10)

    def agregar_persona(self):
        nombre = self.nombre_entry.get()
        try:
            peso = float(self.peso_entry.get())
            persona = Persona(nombre, peso)
            self.personas.append(persona)
            self.personas_listbox.insert(tk.END, nombre)
            self.nombre_entry.delete(0, tk.END)
            self.peso_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Peso debe ser un número válido.")

    def mostrar_persona(self, event):
        seleccion = self.personas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            persona = self.personas[indice]
            self.peso_actual_value.config(text=str(persona.peso))
    
    def comer(self):
        seleccion = self.personas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            persona = self.personas[indice]
            persona.comer()
            self.peso_actual_value.config(text=str(persona.peso))

    def caminar(self):
        seleccion = self.personas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            persona = self.personas[indice]
            persona.caminar()
            self.peso_actual_value.config(text=str(persona.peso))

# Iniciar la aplicación
root = tk.Tk()
app = App(root)
root.mainloop()
