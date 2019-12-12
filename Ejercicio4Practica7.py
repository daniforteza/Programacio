frase=str(input("Escribe una frase:"))

def f(x):
    for i in x:
        if i==(" "):
            print("*",end="")
        else:
            print(i,end="")

f(frase)