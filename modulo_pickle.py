import datetime
import pickle


def main():
    # uso del modulo 'pickle' para serializar y deserializar objetos Python:
    print ('Uso del modulo pickle para serializar y deserializar objetos Python')
    
    # Datos que queremos escribir (cadena, entero, flotante, fecha, booleano)
    data = [
        ("Alice", 30, 72.5, str(datetime.date(2024, 6, 17)), True),
        ("Bob", 25, 80.0, str(datetime.date(2023, 12, 25)), False),
        ("Charlie", 35, 65.3, str(datetime.date(2022, 1, 1)), True)
    ]
    
    archivo = 'datas.pickle'
    
    with open(archivo, 'wb') as file:
        pickle.dump(data, file) 

    print("lectura de datos desde el archivo datas.pickle")
    with open(archivo, 'rb') as file:
        data_read = pickle.load(file)
        
        print ('Tipo de datos de la variable recuperada:', type(data_read))
        
        for item in data_read:
            print(item) 
            fecha_dt = datetime.datetime.strptime(item[3], "%Y-%m-%d").date()
            print(fecha_dt)

if __name__ == "__main__":
    main()
    
    