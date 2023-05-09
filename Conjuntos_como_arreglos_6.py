"""
6. Conjuntos como arreglos
Un arreglo de elementos de tipo T se puede utilizar para representar un conjunto finito de elementos
del tipo T. Esta representaci ́on es como sigue:
El conjunto A = {x0, x1, x2, . . . , xn−1} se representa como el arreglo (x0, x1, x2, . . . , xn−1).
Usando esta representaci ́on hacer un programa que le permita al usuario leer dos conjuntos de
enteros y escoger mediante un men ́u, una de las siguientes operaciones sobre ellos:
"""

def minimoR(arreglo:list,k):
    if (arreglo == []):
        return k
    if (k <= arreglo[-1]):
        return minimoR(arreglo[:len(arreglo)-1],k)
    else:
        return minimoR(arreglo[:len(arreglo)-1],arreglo[-1])

def minimo(v:list):
    v2 = v.copy()
    return minimoR(v2,v2.pop())

def eliminar_algoR(arreglo:list, valor):
    if(arreglo==[]):
        return arreglo
    if (valor == arreglo[-1]):
        return eliminar_algoR(arreglo[:len(arreglo)-1],valor)
    else:
        return eliminar_algoR(arreglo[:len(arreglo)-1],valor) + [arreglo[-1]]

def eliminar_algo(arreglo:list,valor):
    return eliminar_algoR(arreglo.copy(),valor)

def ordenarR(arreglo:list):
    if (arreglo==[]):
        return arreglo
    minimo_ = minimo(arreglo)
    sin_elemento = eliminar_algo(arreglo,minimo_)
    return [minimo_] + ordenarR(sin_elemento)

def ordenar(arreglo:list):
    return ordenarR(arreglo.copy())

def eliminar_doblesR(arreglo:list):
    """
    Solo para arreglos ordenados
    """
    if (len(arreglo)==1):
        return arreglo
    if (arreglo[0] == arreglo[1]):
        return eliminar_doblesR(arreglo[1:])
    else:
        return [arreglo[0]] + eliminar_doblesR(arreglo[1:])

def esta_presenteR(arreglo:list,valor):
    if (arreglo==[]):
        return False
    if (valor == arreglo[0]):
        return True
    else:
        return esta_presenteR(arreglo[1:],valor)

def esta_presente(arreglo:list,valor):
    return esta_presenteR(arreglo.copy(),valor)


#v = [int(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]
#w = [int(x) for x in input("Ingrese la lista w separado por espacios: ").strip().split(" ")]


def sumar_arregloR(arreglo:list):
    if (arreglo == []):
        return 0
    return arreglo[0] + sumar_arregloR(arreglo[1:])

"""
35. Uni ́on: Calcula en un arreglo la uni ́on de los conjuntos y la imprime.

def unionR(a:list,b:list):
    if (a == [] and b ==[]):
        return []
    elif (a!= [] and b == []):
        return a
    elif (a== [] and b != []):
        return b
    if(a[0] == b[0]):
        return [a[0]] + unionR(a[1:],b[1:])
    elif (a[0] < b[0]):
        return [a[0], b[0]] + unionR(a[1:],b[1:])
    else:
        return [b[0], a[0]] + unionR(a[1:], b[1:])

def union(a:list,b:list):
    a_ = ordenar(a)
    b_ = ordenar(b)
    return eliminar_doblesR(ordenarR(unionR(a_,b_)))
"""
"""
36. Intersecci ́on: Calcula en un arreglo la intersecci ́on de los conjuntos y la imprime.


def interseccionR(a:list,b:list):
    if (a == [] or b == []):
        return []
    if(a[0] == b[0]):
        return [a[0]] + interseccionR(a[1:],b[1:])
    elif (len(a)>len(b)):
        if(esta_presente(a,b[0])):
           return [b[0]] + interseccionR(a, b[1:])
    else:
        if (esta_presente(b,a[0])):
            return [a[0]] + interseccionR(b,a[1:])
    return interseccionR(a,b[1:])

def inteseccion(a:list,b:list):
    return ordenar(interseccionR(a.copy(),b.copy()))

print(inteseccion(v,w))
"""
"""
37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.
"""

"""
39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los
conjuntos y lo imprime.


def pertenece(v:list, w:list, elemento):
    if (esta_presente(v, elemento)):
        print(f'{elemento} pertenence al conjunto v')
    if (esta_presente(w,elemento)):
        print(f'{elemento} pertenece al conjunto w')
"""

"""
40. Contenido: Determina s ́ı el primer conjunto esta contenido en el segundo y lo imprime.


def contenido(v:list,w:list):
    if (v == []):
        return True
    return esta_presente(w,v[-1]) and contenido(v[:len(v)-1],w)

print(contenido(v,w))
"""