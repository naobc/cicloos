'''
Crea una programa que pida un número y calcule su factorial (El factorial de un número es el 
producto de todos los enteros entre 1 y el propio número y se representa por el número seguido 
de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)
'''
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
numero = int(input("Introduce un número para calcular su factorial: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")