class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre}."

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def sonido(self):
        return "Sonido de animal"

# Crear una lista de objetos
objetos = [Persona("Juan", 30), Animal("Perro", 5)]

# Obtener información de cada objeto
informacion_objetos = []

for obj in objetos:
    # Obtener el nombre de la clase
    nombre_clase = obj.__class__.__name__
    
    # Obtener todos los atributos y métodos del objeto
    atributos_y_metodos = dir(obj)
    
    # Filtrar sólo los atributos
    atributos = [attr for attr in atributos_y_metodos if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    
    # Agregar la información a la lista
    informacion_objetos.append({
        'clase': nombre_clase,
        'atributos': atributos
    })

# Imprimir la información
for info in informacion_objetos:
    print(f"Clase: {info['clase']}, Atributos: {info['atributos']}")

# Esto imprimirá:
# Clase: Persona, Atributos: ['edad', 'nombre']
# Clase: Animal, Atributos: ['edad', 'especie']
