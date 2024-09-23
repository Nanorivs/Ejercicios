"""Un centro numérico es un número que separa una lista de números enteros
    (comenzando en 1) en dos grupos de números, cuyas sumas son iguales.

    El primer centro numérico es el 6, el cual separa la lista (1 a 8) en los
    grupos: (1; 2; 3; 4; 5) y (7; 8) cuyas sumas son ambas iguales a 15.
    El segundo centro numérico es el 35, el cual separa la lista (1 a 49) en
    los grupos: (1 a 34) y (36 a 49) cuyas sumas son ambas iguales a 595.

    Se pide elaborar una aplicación que calcule los centros numéricos entre
    1 y el número que el usuario ingrese por consola.
"""

numero_usuario = 49
centro_numerico = 1

suma_primer_mitad = 0
suma_segunda_mitad = 0

while centro_numerico <= numero_usuario:
    suma_primer_mitad = 0
    suma_segunda_mitad = 0
    segunda_mitad = centro_numerico + 1

    for numero in range(centro_numerico):
        suma_primer_mitad += numero
    
    for numero in range(segunda_mitad,numero_usuario):
        suma_segunda_mitad += numero
    suma_segunda_mitad += numero_usuario

    if suma_primer_mitad == suma_segunda_mitad:
        break

    centro_numerico += 1

if suma_primer_mitad == suma_segunda_mitad:
    print(f"Centro numérico entre 1 y {numero_usuario}: {centro_numerico}")
    print(f"Ambas sumas de: {suma_primer_mitad}")
else:
    print(f"No hay un centro numérico entero entre 1 y {numero_usuario}")


