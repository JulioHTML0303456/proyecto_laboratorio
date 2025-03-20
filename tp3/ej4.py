def check():
    print('escriba una palabra')
    palabra=input()
    palabra = palabra.replace(" ", "")
    inverse=palabra[::-1]
    
    if inverse == palabra:
        return 'es un palindromo'
    else:
        return 'no es un palindromo'

print(check())