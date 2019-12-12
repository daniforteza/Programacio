print ("Escriba un numero:")
numero1=int(input())
list=[numero1]
print ("Escriba un numero mayor que",numero1,":")
numero2=int(input())

while numero2>numero1:
    list+=[numero2]
    numero1=numero2
    print ("Escriba un numero mayor que",numero1,":")
    numero2=int(input())
for i in list:
    print (i,end=",")
    

   