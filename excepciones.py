def excepcion1():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

def excepcion2():
    try:
        value = int("abc")
    except ValueError:
        print("Error: No se puede convertir la cadena a un número entero.")

def excepcion3():
    try:
        value = int("abc")
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: No se puede convertir la cadena a un número entero.")


def excepcion4():    
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado: {result}")
    finally:
        print("Esta línea se ejecutará siempre.")
    
## excepcion1()
## excepcion2()
excepcion3()
excepcion4()   