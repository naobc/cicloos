'''
Crea un programa que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que 
el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), 
si se llega al limite de intentos te muestra el número que había generado.
Para genear un número entero aleatorio se utiliza la función randintdel paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''
import random
def adivina_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 10
    print("¡Bienvenido al juego de adivinar el número!")
    print("He generado un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")
    while intentos > 0:
        intento = int(input(f"Te quedan {intentos} intentos. Introduce un número: "))
        if intento == numero_aleatorio:
            print(f"¡Felicidades! Has adivinado el número en {11 - intentos} intentos.")
            break
        elif intento < numero_aleatorio:
            print("El número es mayor que el que has introducido.")
        else:
            print("El número es menor que el que has introducido.")
        intentos -=1
    if intentos == 0:
        print(f"Lo siento, se han agotado tus intentos. El número era {numero_aleatorio}.")
adivina_numero()