def number(n):
    if n %2==0:
        return"es par"
    else:
        return"no es par"
print('ingrese un numero para verificar si es par')
x=int(input())
print(number(x))