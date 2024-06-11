cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)  # Output: Hola Mundo
input()

nombre = "Juan"
edad = 20
cadena_formateada = f"Me llamo {nombre} y tengo {edad} años."
print(cadena_formateada)  # Output: Me llamo Juan y tengo 20 años.
input()

cadena = "uno,dos,tres,cuatro"
partes = cadena.split(',')
print(partes)  # Output: ['uno', 'dos', 'tres', 'cuatro']
input()

cadena = "Hola Mundo"
cadena_mayusculas = cadena.upper()
cadena_minusculas = cadena.lower()
print(cadena_mayusculas)  # Output: HOLA MUNDO
print(cadena_minusculas)  # Output: hola mundo
input()

cadena = "   Hola Mundo   "
cadena_limpia = cadena.strip()
print(cadena_limpia)  # Output: Hola Mundo
input()

cadena = "Hola Mundo"
empieza_con = cadena.startswith("Hola")
termina_con = cadena.endswith("Mundo")
print(empieza_con)  # Output: True
print(termina_con)  # Output: True
input()

cadena = "Hola Mundo"
indice = cadena.find("Mundo")
print(indice)  # Output: 5
input()

cadena = "Hola Mundo"
longitud = len(cadena)
print(longitud)  # Output: 10
input()

cadena1 = "Hola123"
cadena2 = "Hola"
cadena3 = "123"
print(cadena1.isalnum())  # Output: True (solo contiene letras y números)
print(cadena2.isalpha())  # Output: True (solo contiene letras)
print(cadena3.isdigit())  # Output: True (solo contiene dígitos)
input()

