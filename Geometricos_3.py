"""
3. Geométricos
"""

"""
14.
Dadas la pendiente y el punto de corte de dos rectas, determinar si son paralelas, perpendi-
culares o ninguna de las anteriores.


def perpendicular_paralela_o_no(m1,m2):
  if (m1==m2):
    return "paralelas"
  elif (m1==-m2):
    return "perpendiculares"
  else:
    return "ni paralelas ni perpendiculares"

m1 = float(input("Ingrese pendiente 1: "))
m2 = float(input("Ingrese pendiente 2: "))
p1 = float(input("Ingrese punto de corte 1: "))
p2 = float(input("Ingrese punto de corte 2: "))

respuesta = perpendicular_paralela_o_no(m1,m2)

print(f'Las rectas son {respuesta}')
"""