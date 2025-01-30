# Un grupo de estudiantes quiere aprovechar la tarde del domingo yendo al cine. Ha decidido ir hasta 
# el Unicentro y se encuentran que no pueden comprar mas de 7 boletos por persona y un aviso que indica
# que las boleta cuesta $12.000 pero se puede obtener descuentos por la compra si cumplen con ciertas condiciones 
    # 1.	Si compran más de cinco boletas le dan un 15% de descuento sobre el valor a pagar 
    # 2.	Si compran tres, cuatro o cinco boletas le dan un 10% de descuento sobre el valor a pagar 
    # 3.	Pero si compran solo hasta dos boletas no tienen descuento
# El mismo aviso aparece una nota que indica que si la compra será pagada utilizando la tarjeta cineco, 
# tendrá derecho a un 10% del valor a pagar, como descuento adicional a los descuentos ya obtenidos.

# Desarrolle una ciolucion para determinar cuanto se debe pagar por la compra de la(s) boleta(s), 
# el nombre de la persona que realizara la compra y la cantidad máxima de boletas compradas.


        #Condiciones de compra
    # cuantas personas van a comprar boletos solo se pueden comprar 7 boletos por persona
    # si no se puede comprar se debe cambiar le numero de personas o el de boletos
    # pedir nombre de la persona que va a comprar
    # se debe almacenar en un archivo de texto el nombre de la persona y el numero de boletos comprados 
    # El programa no se cerrara, se debe preguntar si desea comprar mas boletoso no
    #El total de boletos comprados se debe guardar en un archivo de texto con el nombre de la persona y el numero de boletos
    # si se compra mas de 7 boletos se debe preguntar si desea comprar mas boletos
    #Solo se va a guardar en el txt el nombre de quien compro y el total
    
import os
from io import open

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidadPersonasVenta = 0
        self.boletos = 0
        self.metodoPago = ""
        self.total = 0
        
    def asignarCompra(self, cantidadPersonasVenta, boletos):
        self.cantidadPersonasVenta = cantidadPersonasVenta
        self.boletos = boletos
    
    def calcularTotal(self):
        precio = 12.00
        total = self.boletos * precio
        if self.boletos > 5:
            total *= 0.85  # 15% de descuento
        elif self.boletos > 3:
            total *= 0.90  # 10% de descuento
        self.total = total
        return total
        
        
    def aplicarDescuentoTarjeta(self):
        self.total *= 0.90  # Descuento adicional del 10% por tarjeta CINECO
            
            
    def __str__(self):
      return f"{self.nombre}, {self.total:.2f}"

class Boleto: # Valida que no se exceda el número máximo permitido de boletos por persona.
    Cantidad_Boleto_Max_Persona = 7

    def validarCantidadBoletos(cantidadPersonasVenta, boletos):
        return boletos <= cantidadPersonasVenta * Boleto.Cantidad_Boleto_Max_Persona
 
def limpiarArchivo():
     with open("ticket.txt", "w") as fichero:
         fichero.write("") 
    
def imprimirTicket(compras):
    with open("ticket.txt", "w") as fichero:
        total_general = 0
        for compra in compras:
            fichero.write(f"{compra}\n")
            total_general += compra.total
        fichero.write(f"Total general: ${total_general:.2f}\n")
        print(f"Ticket generado. Total general: ${total_general:.2f}")

def mostrarTicket():
    with open("ticket.txt", "r") as fichero:
        print("\n--- Ticket generado ---")
        for linea in fichero:
            print(linea.strip())
        print("--- Fin del ticket ---\n")
    
def optionMenuCinepolis():
    limpiarArchivo()
    compras = []
    os.system("cls")
    print("Cinepolis, digite la opcion a escoger :)")
    print("1. Comprar")
    print("2. Salir")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        comprarBoletos(compras)
    elif opcion == 2:
        os.system("cls")
        print("Cinepolis")
        print("Gracias por comprar")
        
def comprarBoletos(compras):
    os.system("cls")
    print("Ingrese el nombre de la persona que va a comprar:")
    nombre = input("Nombre: ")
    cliente = Persona(nombre)
    
    cantidadPersonasVenta = int(input("Ingrese la cantidad de personas que va a comprar: "))
    boletos = int(input("Ingrese la cantidad de boletos que va a comprar: "))
    
    while not Boleto.validarCantidadBoletos(cantidadPersonasVenta, boletos):
        os.system("cls")
        print(f"No puedes comprar más de {cantidadPersonasVenta * Boleto.Cantidad_Boleto_Max_Persona} boletos.")
        print("1. Cambiar la cantidad de boletos")
        print("2. Cambiar la cantidad de personas")
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            boletos = int(input("Ingrese la cantidad de boletos: "))
        elif opcion == 2:
            cantidadPersonasVenta = int(input("Ingrese la cantidad de personas: "))
       # boletos = int(input("Ingrese la cantidad de boletos: "))
            
    cliente.asignarCompra(cantidadPersonasVenta, boletos)
    total = cliente.calcularTotal()
    
    os.system("cls")
    print(f"El total de los boletos es ${total:.2f}")
    print("1. Pagar con tarjeta CINECO (10% de descuento adicional)")
    print("2. Pagar con efectivo")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        cliente.metodoPago = "CINECO"
        cliente.aplicarDescuentoTarjeta()
    else:
        cliente.metodoPago = "EFECTIVO"
        
    print(f"Compra terminada. El total es ${cliente.total:.2f}")
    compras.append(cliente)
    
    print("Desea continuar con otra compra? 1. Si, 2. No")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        comprarBoletos(compras)
    elif opcion == 2:
        print("Compra finalizada, imprimiendo ticket")
        imprimirTicket(compras)
        mostrarTicket()
            
if __name__ == "__main__":
    optionMenuCinepolis()