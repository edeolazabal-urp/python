import struct

# Función para escribir una lista de enteros en un archivo binario
def write_integers_to_binary(filename, integers):
    with open(filename, 'wb') as file:
        for number in integers:
            packed_data = struct.pack('i', number)
            file.write(packed_data)

# Función para leer una lista de enteros desde un archivo binario
def read_integers_from_binary(filename):
    integers = []
    with open(filename, 'rb') as file:
        while True:
            data = file.read(4)  # Tamaño de un entero en bytes
            if not data:
                break
            number = struct.unpack('i', data)[0]
            integers.append(number)
    return integers

# Uso del programa
integers = [10, 20, 30, 40, 50]
filename = 'integers.bin'

# Guardar los enteros en el archivo binario
write_integers_to_binary(filename, integers)

# Leer los enteros desde el archivo binario
read_integers = read_integers_from_binary(filename)
print(f"Enteros leídos: {read_integers}")
