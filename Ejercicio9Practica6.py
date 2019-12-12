print("Escriba un nombre:")
nombre=str(input())
list=[]

while nombre!='s':
    print("Escriba un telefono:")
    telefono=int(input())
    list+=[[nombre,telefono]]
    print("Escriba un nombre:")
    nombre=str(input())
    print ("Los nombres y telefonos de la agenda són:")
    for i in list:
        print(i)