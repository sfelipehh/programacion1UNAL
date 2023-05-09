"""
1. Granja
En una granja se crían un número de V - Vacas, A - Aves (pollos y gallinas) y E - escorpiones.
Las vacas est ́an encerradas en un corral de N × M metros cuadrados, las aves en un galp ́on y los
escorpiones en vitrinas.
"""
MES = 30
DIA = 1

vacas = 0
aves = 0
escorpiones = 0
corral_x = 0 # m
corral_y = 0 # m
pasto_por_vaca = 0 # m^2
leche_por_vaca = 0

"""
1.
Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿cu ́antos
litros de leche se producen en la granja?.


def leche_producida_en_la_granja(m2Corral, pasto_necesario, litros_por_alimentacion):
    return (m2Corral//pasto_necesario)*litros_por_alimentacion

corral_x = int(input("Ancho del corral de vacas?(m) "))
corral_y = int(input("Largo del corral de vacas?(m) "))
pasto_por_vaca = int(input("Pasto necesario para cada vaca?(m^2) "))
leche_por_vaca = int(input("Litros producidos por vaca alimentada?(L) "))

litros_producidos = leche_producida_en_la_granja(corral_x*corral_y, pasto_por_vaca, leche_por_vaca)

print(f'La cantidad de litros producida en la graja es de {litros_producidos} litros')
"""

"""
2.
Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las gallinas ponen 1 huevo
cada 3 d ́ıas y la otra mitad 1 huevo cada 5 d ́ıas, ¿en un mes cu ́antos huevos producen?
(1 mes ≡ 30 d ́ıas).


def cantidad_de_huevos_en_un_mes(cant_gallinas):
    return (cant_gallinas//2)*(MES//3) + (cant_gallinas//2)*(MES//5)

aves = int(input("Cantidad de aves? "))
gallinas = aves//3

huevos_producidos = cantidad_de_huevos_en_un_mes(gallinas)

print(f'La cantidad de huevos que produciran las gallinas es {huevos_producidos}')
"""

"""
3.
Si los escorpiones de la granja se venden a China, y hay escorpiones de tres diferentes tama ̃nos:
peque ̃nos (con un peso de 20 gramos), medianos (con un peso 30 gramos) y grandes (con
un peso de 50 gramos), ¿cu ́antos kilos de escorpiones se pueden vender sin que decrezca la
poblaci ́on a menos de 2/3?.


def maximos_kilos_sin_disminuir_mucho_la_poblacion(total_escorpiones, escorpiones_de_20g, escorpiones_de_30g, escorpiones_de_50g):
    limite_de_poblacion = total_escorpiones//3
    e20g = escorpiones_de_20g
    e30g = escorpiones_de_30g
    e50g = escorpiones_de_50g
    gramos_a_vender = 0
    while(limite_de_poblacion > 0):

       if e50g>0:
           gramos_a_vender+=50
       elif e30g>0:
           gramos_a_vender+=30
       elif e20g>0:
           gramos_a_vender+=20

       limite_de_poblacion -= 1

    return gramos_a_vender/1000
    
escorpiones_20g = int(input("Cantidad de escorpiones que pesan 20 gramos? "))
escorpiones_30g = int(input("Cantidad de escorpiones que pesan 30 gramos? "))
escorpiones_50g = int(input("Cantidad de escorpiones que pesan 50 gramos? "))
escorpiones = escorpiones_20g + escorpiones_30g + escorpiones_50g

maximos_kilos = maximos_kilos_sin_disminuir_mucho_la_poblacion(escorpiones,escorpiones_20g,escorpiones_30g,escorpiones_50g)

print(f'La cantidad maxima de kilogramos vendibles es {maximos_kilos} kg')
"""

"""
4.
Al granjero se le da ̃no el corral y no sabe si volver a cercar el corral con madera, alambre de
p ́uas o poner reja de metal. Si va a cercar con madera debe poner 4 hileras de tablas, con
varilla 8 hileras y con alambre solo 5 hileras,  ́el quiere saber que es lo menos costoso para
cercar si sabe que el alambre de p ́uas vale P por metro, las tablas a Q por metro y las varillas
S por metro. Dado el tama ̃no del corral y los precios de los elementos, ¿cu ́al cerramiento es
el m ́as econ ́omico?.

def cerramiento_mas_economico(ancho_corral, largo_corral, precio_metro_alambre, precio_metro_tablas, precio_metro_varillas):
    perimetro_corral = 2*(ancho_corral + largo_corral)

    costo_en_alambre = 5*perimetro_corral*precio_metro_alambre
    costo_en_tablas = 4*perimetro_corral*precio_metro_tablas
    costo_en_varillas = 8*perimetro_corral*precio_metro_varillas

    if costo_en_alambre<costo_en_tablas and costo_en_alambre<costo_en_varillas:
        return ("alambre",costo_en_alambre)
    if costo_en_tablas<costo_en_alambre and costo_en_tablas<costo_en_varillas:
        return ("tablas",costo_en_tablas)
    if costo_en_varillas<costo_en_alambre and costo_en_varillas<costo_en_tablas:
        return ("varillas",costo_en_varillas)

corral_x = int(input("Ancho del corral?(m) "))
corral_y = int(input("Largo del corral?(m) "))
precio_alambre = int(input("Precio alambre por metro? "))
precio_tablas = int(input("Precio tablas por metro? "))
precio_varillas = int(input("precio varillas por metro? "))

elemento, costo = cerramiento_mas_economico(corral_x, corral_y, precio_alambre, precio_tablas, precio_varillas)

print(f'El elemento más barato es {elemento} con un costo de {costo}')
"""
