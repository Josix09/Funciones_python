print("................................")
print("- BUSCAR UN NÚMERO EN CONJUNTO -")
print("................................")
# definición de la función

def buscarDatoEnLista (datoABuscar,lista):
 r=False
 for i in lista:
    if i == datoABuscar :
        r=True
        return r
    
#entrada
dato=int(input("número a buscar: ")) # se recibe el dato del usuario

#procesamiento
lista=[1,2,3,4,5] # se almacena una lista de datos
if buscarDatoEnLista(dato,lista):
   print("lo encontré")

else:
   print("no lo encontré")

#salida
print("/nEso era...")
     
          
