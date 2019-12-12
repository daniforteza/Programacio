numero1=int(input("Escribe un numero: "))
list=[numero1]
numero2=int(input("Escribe un numero mayor que %d:" % (numero1)))

while numero1 >=numero2:
    numero2 =int(input("%d no es mayor que %d. Escribe un numero mayor que %d:"%(numero2, numero1, numero1)))

numero=int(input("Escribe un numero entre %d y %d: " % (numero1, numero2)))
while numero > numero1 and numero < numero2:
    list += [numero]
    numero =int(input("Escribe un numero entre %d y %d: " % (numero1,numero2)))
list +=[numero2]
print("Los numeros de  lista que has escrito són:",list,)