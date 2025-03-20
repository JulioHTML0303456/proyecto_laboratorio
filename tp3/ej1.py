list=[{"nombre":'julito',"apellido":"bravito","edad":21},
      {"nombre":'alberto',"apellido":"gonzales","edad":23},
      {"nombre":'esteban',"apellido":"osuna","edad":14}]
print("inserte un nombre")
sign=input()
i=0
while i<len(list):
    if sign == list[i]["nombre"]:
        print(list[i]["nombre"],list[i+1]["edad"])
    i+=1
i=0
while i<len(list):
    if sign == list[i]["nombre"]:
        print (list[i])
    i+=1