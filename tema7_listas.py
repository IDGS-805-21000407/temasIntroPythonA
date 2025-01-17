'''
#Listas en Python

lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["juan",45,1.92]

print(type(lista1))
print(len(lista1))  

print(lista1[0])
suma=0
x=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1   
    
    
    
print("La suma es:{}".format(suma))

print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)

print(lista1[3])

lista5=[]

for x in range(5):
    valor=input(input("Ingrese un numero:"))
    lista5.append(valor)
    
print(lista5)



print(lista1)
lista1.pop()
print(lista1)
'''



'''
lista1.sort()#ordena la lista
print(lista1)
lista1.reverse()#invierte la lista
print(lista1)

lista1.remove(10)
print(lista1) #?

lista.clear()
print(lista)#vacia la lista
'''


'''
Crear un programa pedir una cantidad n de numeros y almacenalos en un arreglo la salida debera ser la siguiente:
lista Completa xxxxxxxxx,
Numeros pares de la lista: aaaaaaaa
numeros impares de la lista: rrrrrrr
'''

lista_Datos = []
par_numbers = []    
impar_numbers = []  

cantidad = int(input("Ingrese la cantidad de numeros: "))
for x in range(cantidad):
    valor = int(input("Ingrese un numero: "))  
    lista_Datos.append(valor)
    
print("Los numeros ingresados son:", lista_Datos)

for number in lista_Datos:
    if number % 2 == 0:
        par_numbers.append(number)
    else:
        impar_numbers.append(number)    
        
print("Numeros pares de la lista:", par_numbers)
print("Numeros impares de la lista:", impar_numbers)
