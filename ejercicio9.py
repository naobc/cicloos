'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
    
    if limite_inferior < limite_superior:
        break
    else:
        print("El límite inferior debe ser menor que el límite superior. Vuelve a intentarlo.")
suma_intervalo = 0
fuera_intervalo = 0
limites_iguales = False
while True:
    numero = int(input(f"Introduce un número (0 para terminar): "))
    
    if numero == 0:
        break
    if limite_inferior < numero < limite_superior:
        suma_intervalo += numero
    elif numero == limite_inferior or numero == limite_superior:
        limites_iguales = True
    else:
        fuera_intervalo += 1
print(f"\nSuma de los números dentro del intervalo: {suma_intervalo}")
print(f"Números fuera del intervalo: {fuera_intervalo}")
print(f"¿Se introdujo algún número igual a los límites? {'Sí' if limites_iguales else 'No'}")
