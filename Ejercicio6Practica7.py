nombre=str(input("Escriba un nombre:"))
caracter=str(input("Escriba un caracter,puede estar o no en el nombre:"))

def f(x):
    for i in x:
        aux=0
        if i==caracter:
            aux+=1
        else:
            aux-=1
    if aux>1:
        print ("Tu nombre no tiene ese caracter.")
    else:
        print ("Tu nombre tiene ese caracter.")
f(nombre)