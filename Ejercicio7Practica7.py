frase=str(input("Escriba una frase:"))
aux=0
def f(x,m):
    m=0
    for i in x:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            m+=1
    print("El numero de vocales ha sido",m,)

f(frase,aux)