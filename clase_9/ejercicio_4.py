from paquete.funciones import *
""" Realizar una funcion que calcule la suma de todos los elementos de una fila perteneciente a una matriz """

def suma_de_elementos_matriz(matriz:list)->list:
    """Sumar elementos de una matriz

    Args:
        matriz (list) : suma total de los elementos de las filas de una matriz
    Returns:
        lista de totales(list): lista de suma de cada fila
    """
    lista_totales = list()

    for fila in matriz:
        total = 0
        
        for indice in range(len(fila)):
            total += fila[indice]
        lista_totales.append(total)
    
    return lista_totales

matriz = crear_matriz(3,3,random=True)
lista_suma_filas = suma_de_elementos_matriz(matriz)

print()
imprimir_matriz(matriz)
print()
for i in range(len(lista_suma_filas)):
    print(f"Total fila {i+1}: {lista_suma_filas[i]}")

