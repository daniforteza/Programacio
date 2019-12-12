numero=int(input("Escribe un numero:"))
if numero==0:
    print("El numero 0 es un numero neutro y no está considerado como numero primo.")
if numero==1:
    print("El numero 1 no está considerado como numero primo.")
divisor =(numero%2)
while divisor>1  and numero%divisor==0:
    divisor=divisor-1
if divisor ==1:
    print ("El numero %d es primo."% (numero))
else:
    print ("El numero %d no es primo."% (numero))