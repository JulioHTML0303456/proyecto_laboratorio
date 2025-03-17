list =["manzana","pera","anana","banana"]
print("inserte un numero")
x=input()
flag= True
while flag:
    if int(x) > 3:
        print("inserte un numero")
        x=input()
    else:
        flag=False

print(list[int(x)])