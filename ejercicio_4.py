#definir función
import random

def calcular_promedio_lista(lista):
    suma= 0
    for i in lista:
        suma=suma+i
        promedio=suma/len(lista)
        return promedio
    
#lista vacía
lista=[]
#tamaño lista
n= int(input("digite el tamaño de la lista: "))


for i in range(n):
  num=random.randint(14,18)
  lista.append(num)

#procesamiento
print("lista: ", lista)
print("el promedio de la lista es: ", calcular_promedio_lista(lista))