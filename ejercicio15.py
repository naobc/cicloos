'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''
numero = int(input("Introduce un número entero: "))
binario = bin(numero)[2:]
print(f"El número {numero} en binario es: {binario}")