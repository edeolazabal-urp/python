import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear un Frame
frame = tk.Frame(root, bg="lightgray", padx=20, pady=20, relief=tk.GROOVE, borderwidth=2)

# Crear algunos widgets dentro del Frame
label = tk.Label(frame, text="Este es un Frame profesional", font=("Arial", 12))
button = tk.Button(frame, text="Click me", padx=10, pady=5)

# Alinear los widgets dentro del Frame
label.pack(pady=10)
button.pack()

# Empaquetar el Frame en la ventana principal
frame.pack(padx=50, pady=50)

# Ejecutar el bucle principal
root.mainloop()