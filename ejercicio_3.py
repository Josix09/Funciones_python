# construir una función que reciba como parámetro una lista de datos numéricos y retorne la suma de dichos datos.


#entrada (creamos una lista vacía)
import random

lista=[]

#tamaño de la lista
n=int(input("digite el tamaño de la lista: " ))

for i in range(n):
    num=random.randint (1,9)
    lista.append(num)
#definición de la función
suma=0
for i in lista:
    suma=suma+i
def sumar_lista_datos(lista):
    pass

    return suma

print("lista: ", lista)
print("la suma de los datos es: ", sumar_lista_datos(lista))

