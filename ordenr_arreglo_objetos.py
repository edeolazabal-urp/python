Ordenar un arreglo de animales de acuerdo a la longitud del nombre, sin usar la función sorted
# Define a list of animals
animals = ['elephant', 'lion', 'giraffe', 'zebra', 'monkey']

# Sort the animals based on the length of their names
for i in range(len(animals)):
    for j in range(i + 1, len(animals)):
        if len(animals[i]) > len(animals[j]):
            # Swap the animals if the length of the name is greater
            animals[i], animals[j] = animals[j], animals[i]

# Print the sorted animals
print(animals)