class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una lista de objetos Persona
personas = [Persona("Alicia", 30), Persona("Roberto", 25), Persona("Carlos", 35)]

# Acceder al primer elemento de la lista
primera_persona = personas[0]
print(primera_persona.nombre)  # Output: Alicia
input()

# Imprimir el nombre de cada persona en la lista
for persona in personas:
    print(persona.nombre)
input()

# Filtrar personas mayores de 30 años
mayores_de_30 = list(filter(lambda p: p.edad > 30, personas))
for persona in mayores_de_30:
    print(persona.nombre)  # Output: Carlos
input()

# Ordenar personas por edad
personas_ordenadas = sorted(personas, key=lambda p: p.edad)
for persona in personas_ordenadas:
    print(f"{persona.nombre}: {persona.edad}")
# Output:
# Roberto: 25
# Alicia: 30
# Carlos: 35
input()

# Agregar una nueva persona a la lista
nueva_persona = Persona("David", 28)
personas.append(nueva_persona)
input()

# Remover una persona de la lista por referencia
personas.remove(nueva_persona)

# Remover una persona por índice
ultima_persona = personas.pop()
print(ultima_persona.nombre)  # Output: Carlos (en el estado original)
input()

# Crear una lista con solo los nombres de las personas
nombres = [persona.nombre for persona in personas]
print(nombres)  # Output: ['Alicia', 'Roberto']
input()

# Crear una lista con las edades incrementadas en 1 año
edades_incrementadas = list(map(lambda p: p.edad + 1, personas))
print(edades_incrementadas)  # Output: [31, 26, 36]
input()


