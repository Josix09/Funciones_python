print("................................")
print("- BUSCAR UN NÚMERO EN CONJUNTO -")
print("................................")

#entrada
b=int(input("número a buscar: "))#se recibe el dato del ususario

#procesamiento
a=[1,2,3,4,5] #se almacena la lista de datos
r=False #se inicia la variable r con un valor falso

for i in a:
    if i==b:
        print("lo encontré")
        r=True

if r==False:
    print ("no lo encontré")

#salida

print("nEso era...")
