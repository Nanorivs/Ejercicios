"""Un número perfecto es un entero positivo, que es igual a la suma de todos los
    enteros positivos (excluido el mismo) que son divisores del número.

    El primer número perfecto es 6, ya que los divisores de 6
    son 1, 2 y 3; y 1 + 2 + 3 = 6.

    Escribir una aplicación que encuentre los 4 primeros números perfectos.
"""


numeros_perfectos = 0
cantidad_a_mostrar = 4
numero_actual = 1

print(f"Primeros {cantidad_a_mostrar} numeros perfectos:")
while True:
    suma_divisores = 0

    for divisor in range(1,numero_actual):
        if numero_actual % divisor == 0:
            suma_divisores += divisor
    
    if suma_divisores == numero_actual:
        print(numero_actual)
        numeros_perfectos += 1

    numero_actual += 1

    if numeros_perfectos == cantidad_a_mostrar:
        break