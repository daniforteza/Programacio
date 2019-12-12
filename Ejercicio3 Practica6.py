
nota=int(input("Escriba las notas:"))
list=[]
while nota>-1 and nota<11:
    list+=[nota]
    nota=int(input("Escriba la nota recibida:"))
print("Las notas recibidas son",list,)