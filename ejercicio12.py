'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''
saldo_total = 0
for mes in range(1, 13):
    deposito = float(input(f"Introduce la cantidad depositada en el mes {mes}: "))
    saldo_total += deposito
    print(f"Al final del mes {mes}, llevas ahorrado: {saldo_total:.2f} unidades monetarias.")
print(f"\nTotal ahorrado al final del año: {saldo_total:.2f} unidades monetarias.")