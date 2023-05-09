"""
8. Matrices
"""

"""
52. Desarrollar un programa que sume los elementos de una columna dada de una matriz

"""
def sumar_columnaR(matriz:list, c):
    if (matriz == []):
        return 0
    return sumar_columnaR(matriz[1:],c) + matriz[0][c]

"""
53. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

"""
def sumar_fila(matriz:list, f):
    from Conjuntos_como_arreglos_6 import sumar_arregloR
    return sumar_arregloR(matriz[f])


def sumar_diagonal_negativaR(matriz:list, index):
    if (index > (len(matriz)-1)):
        return 0
    return matriz[index][index] + sumar_diagonal_negativaR(matriz, index+1)

def sumar_diagonal_positivaR(matriz:list, index):
    if (index > (len(matriz)-1)):
        return 0
    return matriz[index][len(matriz)-1-index] + sumar_diagonal_positivaR(matriz,index+1)


"""
54. Desarrollar un algoritmo que determine si una matriz es m´agica. Se dice que una matriz cuadrada
es m´agica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual
"""

def es_magicaR(matriz:list, index):
    if (index> (len(matriz)-1)):
        return True
    if (sumar_fila(matriz,index) != sumar_columnaR(matriz,index)):
        return False
    return True and es_magicaR(matriz,index + 1)

def es_magica(matriz):
    a = sumar_fila(matriz,0)
    return es_magicaR(matriz,0) and (sumar_diagonal_positivaR(matriz,0) == sumar_diagonal_negativaR(matriz,0) == a)
