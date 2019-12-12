print ("Vamos a jugar a 'Adivina el número'.")
print("Entre que numeros esta tu numero pensado?")
import random
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
numero=(random.randint (minimo, maximo))
aux=1
numero2=int(input("Escriba un número:"))

while numero2<numero or numero2>numero:  
    if numero2<numero:
        print("Demasiado pequeño")
        numero2=int(input("Vuelve a probar:"))
        aux+=1
    if numero2>numero:
        print("Demasiado grande.")
        numero2=int(input("Vuelve a probar:"))
        aux+=1
    
print("Correcto,has acertado el numero en ",aux,"intentos.")
