'''
Calcular la distancia entre dos puntos
pedir primer punto luego segundo punto
'''

import math

Punto1=[]
punto2=[]

x1=float(input("Ingrese la coordenada X del primer punto: "))
y1=float(input("Ingrese la coordenada Y del primer punto: "))
Punto1.append(x1)
Punto1.append(y1)

x2=float(input("Ingrese la coordenada X del segundo punto: "))
y2=float(input("Ingrese la coordenada Y del segundo punto: "))
punto2.append(x2)
punto2.append(y2)

def sqrt(x):
    return math.sqrt(x)

print("La distancia es:",sqrt((x2-x1)**2+(y2-y1)**2))