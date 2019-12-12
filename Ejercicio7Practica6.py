limite = int(input("Escriba el valor límite: "))
list=[]
while limite <= 0:
    limite = int(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))
numero = int(input("Escriba un número: "))
suma=numero
list+=[numero]
while suma< limite:
    numero = int(input("Escriba otro número: "))
    suma += numero
    list+=[numero]
print("El límite a superar es",limite,".""Los numeros introducidos són",list,"la suma de estos números es ",suma,)