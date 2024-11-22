'''
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
'''
numero_inferior = int(input("Introduce el primer número (limite inferior): "))
numero_superior = int(input("Introduce el segundo número (limite superior): "))
if numero_inferior % 2 != 0:
    numero_inferior += 1
for numero in range(numero_inferior, numero_superior + 1, 2):
    print(numero)