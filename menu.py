### Ejemplo de manejo de Menu
def menu():
    print ('1. Opcion uno')
    print ('2. Opcion dos')
    print ('3. Opcion uno')
    print ('4. Salir')
    
    Elemento = int(input("Escoja ua opcion: "))
    
    match (Elemento):
        case 1:
            print ("Seleciono la opcion 1")
        case 2:
            print ("Seleciono la opcion 2")            
        case 3:
            print ("Seleciono la opcion 3")
        case 4:
            print ("Seleciono la opcion de SALIR")
            return False
    return True

opcion = True

while (opcion):
    opcion = menu()
    
