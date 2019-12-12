limite = int(input("Escriba el valor límite: "))
list=[]
while limite <= 0:
    limite = int(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))
numero1 = int(input("Escriba un número: "))
list+=[numero1]
numero2=int(input("Escriba otro número:"))
suma=numero1+numero2
while suma<limite:
    numero3 = int(input("Escriba otro número: "))
    suma+=numero3
    if suma>limite:
        numero2=int(input("La suma de los numeros ha sobrepasado el limite,escribe un número menor :"))
        list+=[numero2]    
    else:
        print("El límite a igualar es",limite,".""Los numeros introducidos són",list,",la suma de estos números es ",limite,)
    
