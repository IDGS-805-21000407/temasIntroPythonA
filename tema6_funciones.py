import os


def funcion1():
    os.system("cls")
    print("dame dos numeros:")
    num1=int(input("primer numero: "))
    num2=int(input("segundo numero: "))
    res=num1+num2
    print("la suma de {} + {} es {}".format(num1,num2,res))


def run():
    os.system("cls")
    print("menu de opciones")
    print("1. Suma de los dos numeros")
    print("2. otra opcion")
    print("3. salir")   
    opcion = int(input("ingresa unaopcion: "))
    if opcion==1:
        funcion1()
    elif opcion==2:
        funcion2()
 
if __name__=="__main__":
     run()

