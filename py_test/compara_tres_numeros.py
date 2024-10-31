def asignar_mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
def asignar_menor(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
def asignar_medio(a, b, c):
    if a < b and a > c or a > b and a < c:
        return a
    elif b < a and b > c or b > a and b < c:
        return b
    else:
        return c
def crear_lista_ordenada(a, b, c):
    lista = []
    lista.append(asignar_menor(a, b, c))
    lista.append(asignar_medio(a, b, c))
    lista.append(asignar_mayor(a, b, c))
    return lista
def crear_lista(a, b, c):
    return [a, b, c]