'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
def es_primo(n):
    if n <= 1:
        return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True 
cantidad = int(input("Introduce la cantidad de números primos que quieres mostrar: "))
contador = 0
numero = 2 
print(f"Los primeros {cantidad} números primos son:")

while contador < cantidad:
    if es_primo(numero):
        print(numero, end=" ")
        contador += 1
    numero += 1