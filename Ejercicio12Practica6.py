print("Vamos a jugar a adivinar el número")
minimo = int (input ( "Escribe un valor mínimo:"))
maximo = int (input ( "Escribe un valor máximo:"))
print("Piensa el número que quieres que adivine entre el máximo y el mínimo.")
print("Voy a ir nombrando números, tu tienes que decirme si tu número es menor, mayor o igual.")
import random
numero=(random.randint (minimo, maximo))
aux1=input("Tu número es:%d?"% (numero) )
while aux1==menor:
    import random
    numero2=(random.randint (minimo, numero))
    aux1=input("Tu número es:%d?"% (numero2) )
while aux1==mayor1:
    import random
    numero3=(random.randint (minimo, numero))
    aux1=input("Tu número es:%d?"% (numero3) )