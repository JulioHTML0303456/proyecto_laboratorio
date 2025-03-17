list=[]
flag= True
olist=[]
count=0

i=0
while flag:
    print("inserte un nombre a la lista, terminar y o n")
    sign=input() 
    if sign == "y":
        flag=True
    elif sign =="n":
        break  
    list.append(sign)
    if  list[i][0]=="a" or list[i][0] == "e" :
        count+=1
    i+=1
list.sort()
olist.append(list)
print(olist,count)

print("busque un nombre")
name=input()

for x in olist:
    if name == olist[x]:
        print(name)
        break    