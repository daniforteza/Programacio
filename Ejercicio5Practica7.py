frase=str(input("Escribe una frase:"))
vocal=str(input("Escriba una vocal:"))
def f(x):
    for i in x:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
            print(vocal,end="")
        else:
            print(i,end="")
f(frase)