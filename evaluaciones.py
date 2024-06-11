## Programa de Evaluaciones de alumnos en cursos
## Clases
class Alumno:
    codigo_alumno = 0
    nombre_alumno = ''
    
class Curso:
    codigo_curso = 0
    nombre_curso = ''
    
class Evaluacion(Alumno, Curso):
    nota = 0   
    
## Funciones
def existe_alumno(lista, codigo, nombre):
    for elem in lista:
        if elem.codigo_alumno == codigo or elem.nombre_alumno == nombre:
            return True
    return False

def agregar_alumno(lista):
    a = Alumno()
    a.codigo_alumno = int(input ('Ingrese codigo del alumno: '))
    a.nombre_alumno = input('Ingrese el nombre del alumno: ')
    if existe_alumno(lista, a.codigo_alumno, a.nombre_alumno):
        print("Datos de alumno ya exste")
    else:
        lista.append(a)   

def agregar_curso(lista):
    c = Curso()
    c.codigo_curso = int(input ('Ingrese codigo del curso: '))
    c.nombre_curso = input('Ingrese el nombre del curso: ')
    lista.append(c)    

def imprime_lista_alumnos(lista):
    print ("Cod", "Nombre")
    print ("---", "------")
    print ('Prueba: ' + str(lista[0].codigo_alumno) + ', ' + lista[0].nombre_alumno)
    for elem in lista:
        print (elem.codigo_alumno, elem.nombre_alumno)
    print ("---", "------")
               
def imprime_lista_cursos(lista):
    print ("Cod", "Nombre")
    print ("---", "------")
    for elem in lista:
        print (elem.codigo_curso, elem.nombre_curso)
    print ("---", "------")
    
def menu(listaA, listaC, listaE ):
    print ()
    print ('1. Agregar Alumno')
    print ('2. Agregar Curso')
    print ('3. Agregar Calificacion')
    print ('4. Mostrar lista de Evaluacion')
    print ('5. Salir')
    
    Elemento = int(input("Escoja una opcion: "))
    
    match (Elemento):
        case 1:
            agregar_alumno(listaA)
        case 2:
            agregar_curso(listaC)            
        case 3:
            pass
        case 4:
            imprime_lista_alumnos(listaA)
            imprime_lista_cursos(listaC)                
        case 5:
            return False
    return True


## Ejecucion del programa
Lista_Alumnos = []
Lista_Cursos = []
Lista_Evaluacion = []

opcion = True

while (opcion):
    opcion = menu(Lista_Alumnos, Lista_Cursos, Lista_Evaluacion)