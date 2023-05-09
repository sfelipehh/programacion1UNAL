"""
5. Arreglos
"""
"""
23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de n ́umeros enteros
(reales).

def sumaArregloR(arreglo):
    if (arreglo == []):
        return 0
    return arreglo.pop() + sumaArregloR(arreglo)

v = [float(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]

suma = sumaArregloR(v.copy())

print(f'La suma de los elementos de v es {suma}')

"""

"""
24.
Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).

def promedioR(arreglo:list, n):
    if arreglo==[]:
        return 0
    return (arreglo.pop()/n) + promedioR(arreglo,n)

v = [float(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]

promedio = promedioR(v.copy(),len(v))

print(f'El promedio de v es {promedio}')
"""

"""
25.
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de n ́umeros enteros
(reales) de igual tama ̃no. Sean v = (v1, v2, . . . , vn) y w = (w1, w2, . . . , wn) dos arreglos, el
producto de v y w (notado v ⋅ w) es el n ́umero: v1 ∗ w1 + v2 ∗ w2 + ⋯ + vn ∗ wn


def producto_puntoR(arreglo1:list, arreglo2:list):
    if (arreglo1 == [] and arreglo2 == []):
        return 0
    return (arreglo1.pop()*arreglo2.pop()) + producto_puntoR(arreglo1,arreglo2)

def producto_punto(arreglo1:list, arreglo2:list):
    return producto_puntoR(arreglo1.copy(),arreglo2.copy())


v = [float(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]
w = [float(x) for x in input("Ingrese la lista w separado por espacios: ").strip().split(" ")]

p_punto = producto_punto(arreglo1,arreglo2)

print(f'El producto punto de v y w es {p_punto}')
"""

"""
26. Desarrollar un algoritmo que calcule el m ́ınimo de un arreglo de n ́umeros enteros (reales).

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

v = [int(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]

minimo = minimo(v)

print(f'El minimo de v es {minimo}')


"""
27. Desarrollar un algoritmo que calcule el m ́aximo de un arreglo de n ́umeros enteros (reales).

def maximoR(arreglo:list,k):
    if (arreglo == []):
        return k
    if (k > arreglo[-1]):
        return k
    if (k < (vn := arreglo.pop())):
        return maximoR(arreglo,vn)

def maximo(v:list):
    v2 = v.copy()
    return maximoR(v2,v2.pop())

v = [float(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]

maximo = maximo(v)

print(f'El maximo de v es {maximo}')
"""

"""
28. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de
igual tama ̃no. Sean v = (v1, v2, . . . , vn) y w = (w1, w2, . . . , wn) dos arreglos, el producto directo
de v y w (notado v ∗ w) es el vector: (v1 ∗ w1, v2 ∗ w2, . . . , vn ∗ wn).

def producto_directoR(v:list,w:list):
    if (v == [] and w ==[]):
        return []
    return [v.pop(0)*w.pop(0)] + producto_directoR(v,w)

v = [float(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]
w = [float(x) for x in input("Ingrese la lista w separado por espacios: ").strip().split(" ")]

p_directo = producto_directoR(v.copy(),w.copy())

print(f'El producto directo de v y w es {p_directo}')
"""


"""
30. Hacer un algoritmo que deje al final de un arreglo de n ́umeros todos los ceros que aparezcan
en dicho arreglo.

def quita_cerosR(arreglo:list):
    if (arreglo==[]):
        return []
    if (arreglo[-1] == 0):
        arreglo.pop()
        return quita_cerosR(arreglo)
    else :
        last = arreglo.pop()
        return quita_cerosR(arreglo) + [last]
def poner_ceros(arreglo:list, n):
    return arreglo + ([0]*n)
def mover_ceros(v:list):
    sin_ceros = quita_cerosR(v.copy())
    return poner_ceros(sin_ceros,len(v)- len(sin_ceros))

v = [float(x) for x in input("Ingrese la lista v separado por espacios: ").strip().split(" ")]

ceros_acomodados = mover_ceros(v)

print(f'El resultado de colocar los ceros al final es {ceros_acomodados}')
"""

"""
31. Suponga que un arreglo de enteros esta lleno de unos y ceros y que el arreglo representa un
n ́umero binario al rev ́es. Hacer un algoritmo que calcule los n ́umeros en decimal que representa
dicho arreglo de unos y ceros.

def decodificacion_binarioR(arreglo:list, n):
    if (arreglo == []):
        return 0
    else:
        return (arreglo.pop()*(2**n)) + decodificacion_binarioR(arreglo,n-1)

def decodificacion_binario(arreglo:list):
    return decodificacion_binarioR(arreglo.copy(),len(arreglo)-1)

v = [int(x) for x in input("Ingrese el numero binario separado por espacios: ").strip().split(" ")]

numero_decimal = decodificacion_binario(v)

print(f'El numero representado por este numero binario es {numero_decimal}')
"""


"""
32.Hacer un algoritmo que dado un n ́umero entero no negativo, cree un arreglo de unos y ceros
que representa el n ́umero en binario al rev ́es.

def codificacion_binarioR(n):
    if (n == 1):
        return [n]
    else:
        return [n%2] + codificacion_binarioR(n//2)

entero = int(input("Ingresa un número entero no negativo: "))

lista_binaria = codificacion_binarioR(entero)

print(f'El número {entero} como binario al revés es {lista_binaria}')

"""
