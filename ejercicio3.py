
'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problemas se requiere de un acumulador y un contador
'''
contador = 0
acumulador = 0
while True:
    numero = float(input("Introduce un número (o 0 para terminar): "))
    if numero == 0:
        break
    acumulador += numero
    contador += 1
if contador > 0:
    media = acumulador / contador
    print(f"La suma de los números es: {acumulador}")
    print(f"La media de los números es: {media}")
else:
    print("No se han introducido números para calcular la suma o la media.")
