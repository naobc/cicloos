'''
Programa que pida 10 números e imprima el promedio de estos.
Se utilizan los conceptos del programa anterior de contador y acumulador.
'''
contador = 0
acumulador = 0
for i in range(1, 11):
    numero = float(input(f"Introduce el número {i}: "))
    acumulador += numero
    contador += 1
promedio = acumulador / contador
print(f"El promedio de los 10 números introducidos es: {promedio}")