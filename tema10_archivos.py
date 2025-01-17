
from io import open

texto="una linea con texto\notra linea con texto"

fichero=open("fichero.txt","w")
fichero.write(texto)


cadena2="\nEsto es otra cadena"
fichero.write(cadena2)
fichero.close()