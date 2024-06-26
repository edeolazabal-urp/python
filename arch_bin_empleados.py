import struct


# Función para escribir registros de empleados en un archivo binario
def write_employee_records_to_binary(filename, employees):
    with open(filename, 'wb') as file:
        for employee in employees:
            name_bytes = employee[0].encode('utf-8')
            print(f'nombre={name_bytes}')
            name_length = len(name_bytes)
            age = employee[1]
            salary = employee[2]
            # Empaquetamos primero la longitud del nombre
            file.write(struct.pack('I', name_length))
            # Empaquetamos el nombre, la edad y el salario
            print(f'len(nombre)={name_length}, nombre={name_bytes}, edad={age}, salario={salary}')
            packed_data = struct.pack(f'{name_length}sIf', name_bytes, age, salary)
            file.write(packed_data)

# Función para leer registros de empleados desde un archivo binario
def read_employee_records_from_binary2(filename):
    with open(filename, 'rb') as file:
        while True:
            binary_data = file.read(4)
            name_length = struct.unpack('I', binary_data)[0]
            print(f'len={name_length}')            
            unpacked_data = struct.unpack(f'{name_length}sIf', binary_data)
            print(unpacked_data)


def read_employee_records_from_binary(filename):
    employees = []
    with open(filename, 'rb') as file:
        while True:
            name_length_data = file.read(4)
            if not name_length_data:
                break
            name_length = struct.unpack('I', name_length_data)[0]
            name_data = file.read(name_length)
            age_data = file.read(4)
            salary_data = file.read(4)
            print(f'len(nombre)={name_length}, nombre={name_data}, edad={age_data}, salario={salary_data}')

            name = struct.unpack(f'{name_length}s', name_data)[0].decode('utf-8')
            age = struct.unpack('I', age_data)[0]
            salary = struct.unpack('f', salary_data)[0]
            employees.append((name, age, salary))
    return employees

# Uso del programa
employees = [
    (b"Alice", 30, 70000.0),
    (b"Bob", 25, 50000.0),
    (b"Charlie", 35, 60000.0)
]
filename = 'employees.bin'

# Guardar los registros de empleados en el archivo binario
write_employee_records_to_binary(filename, employees)

# Leer los registros de empleados desde el archivo binario
read_employees = read_employee_records_from_binary2(filename)
print("Registros de empleados leídos:")
for employee in read_employees:
    print(f"Nombre: {employee[0]}, Edad: {employee[1]}, Salario: {employee[2]}")
