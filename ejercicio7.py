'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
while True:
    caracter = input("Introduce un carácter (o un espacio para terminar): ")
    if caracter == " ":
        break
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("VOCAL")
    else:
        print("NO VOCAL")