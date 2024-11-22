'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''
base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))
resultado = 1
for _ in range(exponente):
    resultado *= base
print(f"El resultado de {base} elevado a {exponente} es: {resultado}")
