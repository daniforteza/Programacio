print("Escriba un nombre de alumno:")
nombre=str(input())
print("Escriba una nota de este alumno")
nota=int(input())
list=[]

while nota>0 or nota<10:
    print("Escriba otra nota")
    nota=int(input())
    list+=[[nombre,nota]]
    if nota<0 or nota>10:
        print("Escriba el siguiente alumno:")
        nombre=str(input())
        if nombre=(" "):
            print ("Los nombres y notas són:")
            for i in list:
              print(i)    