import csv

# Datos del conjunto
datos = [
    {"Equipo": "Universitario", "PG": 12, "PE": 4, "PP": 1, "GF": 32, "GC": 7},
    {"Equipo": "Sporting Cristal", "PG": 13, "PE": 1, "PP": 3, "GF": 44, "GC": 20},
    {"Equipo": "Melgar", "PG": 12, "PE": 2, "PP": 3, "GF": 36, "GC": 19},
    {"Equipo": "Alianza Lima", "PG": 11, "PE": 0, "PP": 6, "GF": 32, "GC": 16},
    {"Equipo": "Cusco FC", "PG": 9, "PE": 2, "PP": 6, "GF": 22, "GC": 21},
    {"Equipo": "ADT", "PG": 8, "PE": 4, "PP": 5, "GF": 29, "GC": 24},
    {"Equipo": "Cienciano", "PG": 6, "PE": 8, "PP": 3, "GF": 20, "GC": 20},
    {"Equipo": "Comerciantes U.", "PG": 6, "PE": 4, "PP": 7, "GF": 22, "GC": 31},
    {"Equipo": "Los Chankas", "PG": 6, "PE": 3, "PP": 8, "GF": 25, "GC": 26},
    {"Equipo": "Vallejo", "PG": 4, "PE": 8, "PP": 5, "GF": 19, "GC": 24},
    {"Equipo": "Atlético Grau", "PG": 4, "PE": 7, "PP": 6, "GF": 19, "GC": 17},
    {"Equipo": "Sport Boys", "PG": 5, "PE": 4, "PP": 8, "GF": 18, "GC": 20},
    {"Equipo": "Sport Huancayo", "PG": 5, "PE": 4, "PP": 8, "GF": 18, "GC": 29},
    {"Equipo": "UTC", "PG": 4, "PE": 4, "PP": 9, "GF": 21, "GC": 29},
    {"Equipo": "Garcilaso", "PG": 3, "PE": 5, "PP": 9, "GF": 20, "GC": 26},
    {"Equipo": "Alianza Atlético", "PG": 3, "PE": 5, "PP": 9, "GF": 11, "GC": 19},
    {"Equipo": "Mannucci", "PG": 3, "PE": 5, "PP": 9, "GF": 11, "GC": 34},
    {"Equipo": "Unión Comercio", "PG": 1, "PE": 6, "PP": 10, "GF": 17, "GC": 34}
]

# Calcular los puntos para cada equipo
for equipo in datos:
    equipo["Ptos"] = (equipo["PG"] * 3) + (equipo["PE"] * 1)

# Nombre del archivo CSV
nombre_archivo = "tabla_posiciones_liga1_peru_con_puntos.csv"

# Escribir los datos en el archivo CSV usando el delimitador ";"
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    campos = ["Equipo", "PG", "PE", "PP", "GF", "GC", "Ptos"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=';')

    escritor_csv.writeheader()
    for equipo in datos:
        escritor_csv.writerow(equipo)

print(f"Archivo '{nombre_archivo}' creado con éxito.")
