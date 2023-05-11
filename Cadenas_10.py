"""
10. Cadenas
"""

"""
71. Desarrollar un algoritmo que reciba como entrada un car ́acter y de como salida el n ́umero de
ocurrencias de dicho car ́acter en una cadena de caracteres.
"""


def contar_ocurrenciasR(chr: str, string: str):
    if (string == ""):
        return 0
    if (string[0] == chr):
        return 1 + contar_ocurrenciasR(chr, string[1:])
    return contar_ocurrenciasR(chr, string[1:])

"""
72. Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es
subcadena de la segunda. (No se deben usar operaciones de subcadenas propias del lenguaje
de programaci ́on).
"""
def str_contenida(sub: str,cad: str):
    if (cad == "" or len(cad) < len(sub)):
        return False
    if (sub[0] == cad[0]):
        return sub == cad[:len(sub)]
    return str_contenida(sub,cad[1:])

"""
73. Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera est ́a
incluida en la segunda. Se dice que una cadena est ́a incluida en otra, si todos los caracteres
(con repeticiones) de la cadena est ́a en la segunda cadena sin tener en cuenta el orden de los
caracteres.
"""

def caracteres_incluidosR(sub: str, cad: str, i=0):
    if (i == len(sub)):
        return True
    return (contar_ocurrenciasR(sub[i], sub) <= contar_ocurrenciasR(sub[i], cad)) and caracteres_incluidosR(sub, cad, i + 1)

"""
74. Desarrollar un algoritmo que invierta una cadena de caracteres.
"""


def invertir_strR(string: str):
    if (string == ""):
        return ""
    return invertir_strR(string[1:]) + string[0]

"""
75. Desarrollar un algoritmo que determine si una cadena de caracteres es pal ́ındrome. Una cadena
se dice pal ́ındrome si al invertirla es igual a ella misma.
"""


def es_cadena_palindrome(string: str):
    return string == invertir_strR(string)

def es_cadena_palindromeR(string: str, i=1):
    print(i)
    if (string == ""):
        return True
    return (string[0] == string[-1]) and es_cadena_palindromeR(string[1:-1],i+1)

"""
76. Desarrollar un algoritmo que determina si una cadena de caracteres es frase pal ́ındrome. Una
cadena se dice frase pal ́ındrome si la cadena al eliminarle los espacios es pal ́ındrome.
"""


def elimina_espaciosR(string: str):
    if (string == ""):
        return ""
    if (string[0] != " "):
        return string[0] + elimina_espaciosR(string[1:])
    return elimina_espaciosR(string[1:])


def es_frase_palindrome(frase: str):
    return es_cadena_palindrome(elimina_espaciosR(frase))


"""
77. Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
caracteres. El corrimiento circular a izquierda es pasar el primer car ́acter de una cadena como
 ́ultimo car ́acter de la misma.
"""


def corrimiento_circular_izq(string: str):
    return string[1:] + string[0]


"""
78. Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de ca-
racteres. El corrimiento circular a derecha de una cadena es poner el  ́ultimo car ́acter de la
cadena como primer car ́acter de la misma.
"""


def corrimiento_circular_der(string: str):
    return string[-1] + string[:-1]


"""
79. Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de
correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer

car ́acter el car ́acter equivalente para el car ́acter ‘a’, el segundo car ́acter para la ‘b’y as ́ı suce-
sivamente hasta la ‘z’. No se tiene traducci ́on para las may ́usculas ni para la ‘~n’.
"""


def correspondienciaLN(letra: str, correspondencia: str):
    if (letra == " "):
        return letra
    if (letra.isupper()):
        return letra
    indice = int(letra, 36) - 10
    return correspondencia[indice]


def codificarR(mensaje: str, correspondencia: str):
    if (mensaje == ""):
        return ""
    return correspondienciaLN(mensaje[0], correspondencia) + codificarR(mensaje[1:], correspondencia)


"""
80. Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de
correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
car ́acter el car ́acter equivalente para el car ́acter ‘a’, el segundo car ́acter para la ‘b’y as ́ı suce-
sivamente hasta la ‘z’. No se tiene traducci ́on para las may ́usculas ni para la ‘~n’.
"""


def correspondencia_NL_R(letra: str, correspondencia: str, indice=0):
    if (indice == 26):
        return letra
    if (letra == " "):
        return letra
    if (letra == correspondencia[indice]):
        return chr(97 + indice)
    return correspondencia_NL_R(letra, correspondencia, indice + 1)


def decodificarR(mensaje: str, correspondencia: str):
    if (mensaje == ""):
        return ""
    return correspondencia_NL_R(mensaje[0], correspondencia) + decodificarR(mensaje[1:], correspondencia)
