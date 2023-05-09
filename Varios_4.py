"""
4. Varios
"""
"""
20. Si un amigo, no tan amigo, me presta K pesos a i pesos de inter ́es diario, ¿cu ́anto le pagar ́e
en una semana si el inter ́es es simple?, ¿y cu ́anto si el inter ́es es compuesto?.
"""

def interes_compuestoR(capital, interes, tiempo, cuota):
    if(tiempo==0):
        return capital
    nuevo_capital  = capital*(1+interes) - cuota
    return interes_compuestoR(nuevo_capital, interes,tiempo-1,cuota)

def biseccion_interes_compuesto(a,b,capital,interes,tiempo):
    f_a = interes_compuestoR(capital,interes,tiempo,a)
    f_b = interes_compuestoR(capital,interes,tiempo,b)
    nueva_cuota = (a + b) / 2
    f_m = interes_compuestoR(capital, interes, tiempo, nueva_cuota)
    if (f_a==0):
        return a
    if (f_b==0):
        return b
    ##print("Cuota:",nueva_cuota,"\t f_m:",f_m,"\t b-a",b-a,"\t f_a:",f_a,"\t f_b:",f_b)
    if (abs(b-a)<=0.00000001):
        return b
    if ((f_a>0)!=(f_m>0)):
        return biseccion_interes_compuesto(a,nueva_cuota,capital,interes,tiempo)
    else:
        return biseccion_interes_compuesto(nueva_cuota,b,capital,interes,tiempo)

