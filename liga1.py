import csv

# Datos de ejemplo de la tabla de posiciones
tabla_posiciones = [
    {"Posición": 1, "Equipo": "Sporting Cristal", "PJ": 18, "G": 12, "E": 4, "P": 2, "GF": 34, "GC": 12, "DG": 22, "Pts": 40},
    {"Posición": 2, "Equipo": "Alianza Lima", "PJ": 18, "G": 11, "E": 5, "P": 2, "GF": 30, "GC": 15, "DG": 15, "Pts": 38},
    {"Posición": 3, "Equipo": "Universitario", "PJ": 18, "G": 10, "E": 6, "P": 2, "GF": 28, "GC": 14, "DG": 14, "Pts": 36},
    {"Posición": 4, "Equipo": "FBC Melgar", "PJ": 18, "G": 9, "E": 5, "P": 4, "GF": 26, "GC": 18, "DG": 8, "Pts": 32},
    {"Posición": 5, "Equipo": "Deportivo Binacional", "PJ": 18, "G": 8, "E": 6, "P": 4, "GF": 25, "GC": 20, "DG": 5, "Pts": 30},
    {"Posición": 6, "Equipo": "UTC", "PJ": 18, "G": 8, "E": 4, "P": 6, "GF": 22, "GC": 19, "DG": 3, "Pts": 28},
    {"Posición": 7, "Equipo": "Sport Boys", "PJ": 18, "G": 7, "E": 5, "P": 6, "GF": 20, "GC": 18, "DG": 2, "Pts": 26},
    {"Posición": 8, "Equipo": "Cienciano", "PJ": 18, "G": 7, "E": 4, "P": 7, "GF": 19, "GC": 19, "DG": 0, "Pts": 25},
    {"Posición": 9, "Equipo": "Cusco FC", "PJ": 18, "G": 6, "E": 5, "P": 7, "GF": 18, "GC": 20, "DG": -2, "Pts": 23},
    {"Posición": 10, "Equipo": "Carlos A. Mannucci", "PJ": 18, "G": 6, "E": 4, "P": 8, "GF": 17, "GC": 22, "DG": -5, "Pts": 22},
    {"Posición": 11, "Equipo": "Ayacucho FC", "PJ": 18, "G": 5, "E": 5, "P": 8, "GF": 15, "GC": 22, "DG": -7, "Pts": 20},
    {"Posición": 12, "Equipo": "San Martín", "PJ": 18, "G": 5, "E": 4, "P": 9, "GF": 14, "GC": 21, "DG": -7, "Pts": 19},
    {"Posición": 13, "Equipo": "Alianza Atlético", "PJ": 18, "G": 4, "E": 6, "P": 8, "GF": 13, "GC": 20, "DG": -7, "Pts": 18},
    {"Posición": 14, "Equipo": "Universidad César Vallejo", "PJ": 18, "G": 4, "E": 5, "P": 9, "GF": 12, "GC": 19, "DG": -7, "Pts": 17},
    {"Posición": 15, "Equipo": "Academia Cantolao", "PJ": 18, "G": 3, "E": 6, "P": 9, "GF": 11, "GC": 18, "DG": -7, "Pts": 15},
    {"Posición": 16, "Equipo": "Atlético Grau", "PJ": 18, "G": 2, "E": 7, "P": 9, "GF": 10, "GC": 18, "DG": -8, "Pts": 13},
    {"Posición": 17, "Equipo": "Alianza Universidad", "PJ": 18, "G": 2, "E": 6, "P": 10, "GF": 9, "GC": 21, "DG": -12, "Pts": 12},
    {"Posición": 18, "Equipo": "Deportivo Municipal", "PJ": 18, "G": 2, "E": 5, "P": 11, "GF": 8, "GC": 22, "DG": -14, "Pts": 11},
]

# Nombre del archivo CSV
nombre_archivo = "tabla_posiciones_liga1_peru.csv"

# Escribir los datos en el archivo CSV usando el delimitador ";"
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    campos = ["Posición", "Equipo", "PJ", "G", "E", "P", "GF", "GC", "DG", "Pts"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos, delimiter=';')

    escritor_csv.writeheader()
    for equipo in tabla_posiciones:
        escritor_csv.writerow(equipo)

print(f"Archivo '{nombre_archivo}' creado con éxito.")
