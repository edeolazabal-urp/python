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

def existe_alumno_codigo(lista, codigo):
    for i in range(0, len(lista)):
        if lista[i].codigo_alumno == codigo:
            return lista[i].nombre_alumno
    return ''

def existe_curso_codigo(lista, codigo):
    for i in range(0, len(lista)):
        if lista[i].codigo_curso == codigo:
            return lista[i].nombre_curso
    return ''

def agregar_alumno(lista, idAlumno, nombreAlumno):
    a = Alumno()
    a.codigo_alumno = int(idAlumno)
    a.nombre_alumno = nombreAlumno
    if existe_alumno(lista, a.codigo_alumno, a.nombre_alumno):
        # print("Datos de alumno ya existe")
        return False
    else:
        lista.append(a) 
        return True

def agregar_curso(lista):
    c = Curso()
    c.codigo_curso = int(input ('Ingrese codigo del curso: '))
    c.nombre_curso = input('Ingrese el nombre del curso: ')
    lista.append(c)   

def agregar_evaluacion(lista):
    e = Evaluacion()
    # Verificar que exista el alumno
    e.codigo_alumno = int(input ('Ingrese codigo del alumno: '))
    e.nombre_alumno = existe_alumno_codigo(Lista_Alumnos, e.codigo_alumno)
    if  e.nombre_alumno == '':
         print ('No existe el alumno')
         return
    # Verificar que exista el curso
    e.codigo_curso = int(input ('Ingrese codigo del curso: '))
    e.nombre_curso = existe_curso_codigo(Lista_Cursos, e.codigo_curso)
    if  e.nombre_curso == '':
         print ('No existe el curso')
         return
    # verificar que la nota este entre 0 y 20
    e.nota = int(input ('Ingrese la nota: '))
    if e.nota < 0 or e.nota > 20:
         print ('La nota debe estar entre 0 y 20')
         return
    # Crea un nuevo elemento de evaluacion
    lista.append(e) 
    
def elimina_evaluacion (lista, codigo_alumno, codigo_curso):
    for i in range (0, len(lista)):
        if lista[i].codigo_alumno == codigo_alumno and lista[i].codigo_curso == codigo_curso:
            del lista[i]
            return True
    return False # no se encontro una evaluacion con el valor buscado

def elimina_alumno (lista, codigo_alumno, listaC):
    # Busca en la lista de Calificaciones
    comparaC = False
    for i in range (0, len(listaC)):
        if listaC[i].codigo_alumno == codigo_alumno:
            comparaC = True
    if comparaC:
        return False ## No se puede eliminar alumno porque tiene calificaciones

    for i in range (0, len(lista)):
        if lista[i].codigo_alumno == codigo_alumno:
            del lista[i]
            return True
    return False # no se encontro una evaluacion con el valor buscado

def elimina_curso (lista, codigo_curso, listaC):
    # Busca en la lista de Calificaciones
    comparaC = False
    for i in range (0, len(listaC)):
        if listaC[i].codigo_curso == codigo_curso:
            comparaC = True
    if comparaC:
        return False ## No se puede eliminar alumno porque tiene calificaciones

    for i in range (0, len(lista)):
        if lista[i].codigo_curso == codigo_curso:
            del lista[i]
            return True
    return False # no se encontro una evaluacion con el valor buscado

def imprime_lista_alumnos(lista):
    salida = f"Cod\tNombre\n"  
    salida += f"---\t------------\n"
    for elem in lista:
        salida += (str(elem.codigo_alumno)+'\t'+ elem.nombre_alumno + "\n")
    salida += f"---\t------------\n"
    return salida
               
def imprime_lista_cursos(lista):
    print ("Cod", "Nombre")
    print ("---", "------")
    for elem in lista:
        print (elem.codigo_curso, elem.nombre_curso)
    print ("---", "------")
    
def imprime_lista_evaluaciones(lista):
    print ("Alumno", "Curso", "nota")
    print ("------", "-----", "----")
    for elem in lista:
        print (elem.nombre_alumno, elem.nombre_curso, elem.nota)
    print ("------", "-----", "----")
    
def menu(listaA, listaC, listaE ):
    print ()
    print ('1. Agregar Alumno')
    print ('2. Agregar Curso')
    print ('3. Agregar Calificacion')
    print ('4. Eliminar Alumno')
    print ('5. Eliminar Curso')
    print ('6. Eliminar Calificacion')
    print ('7. Mostrar lista de Evaluacion')
    print ('8. Salir')
    
    Elemento = int(input("Escoja una opcion: "))
    
    match (Elemento):
        case 1:
            agregar_alumno(listaA)
        case 2:
            agregar_curso(listaC)            
        case 3:
            agregar_evaluacion(listaE)  
        case 4:
            codigo_alumno = int (input ('Ingrese el codigo de alumno: '))
            if elimina_alumno(listaA, codigo_alumno, listaE):
                print ('Registro eliminado con exito')
            else:
                print ('No se pudo eliminar')
        case 5:
            codigo_curso = int (input ('Ingrese el codigo de curso: '))
            if elimina_curso(listaC, codigo_curso, listaE):
                print ('Registro eliminado con exito')
            else:
                print ('No se pudo eliminar')           
        case 6:
            codigo_alumno = int (input ('Ingrese el codigo de alumno: '))
            codigo_curso = int (input ('Ingrese el codigo de curso: '))
            if elimina_evaluacion(listaE, codigo_alumno, codigo_curso):
                print ('Registro eliminado con exito')
            else:
                print ('No se encontro el registro')
        case 7:
            imprime_lista_alumnos(listaA)
            imprime_lista_cursos(listaC) 
            imprime_lista_evaluaciones(listaE)  
        case 8:
            return False
    return True

