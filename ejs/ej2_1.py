suma=0
flag= True
while flag:
    print("ingrese un numero")
    x=input()
    
    if int(x)>0: 
        suma += int(x)
        print(suma)
    else :
        flag = False
        print(suma)