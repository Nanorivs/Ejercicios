from paquete.funciones import *
"""Realizar una funcion que calcule la suma de dos matrices"""

def sumar_matrices(matriz1:list,matriz2:list)->int:
    from ejercicio_3 import suma_de_elementos_matriz
    """sumar 2 matrices

    Args:
        matriz1 (list): matriz 1
        matriz2 (list): matriz 2

    Returns:
        int: suma total de los elementos de ambas matrices
        
    """
    suma_matriz1 = suma_de_elementos_matriz(matriz1)
    suma_matriz2 = suma_de_elementos_matriz(matriz2)

    return suma_matriz1 + suma_matriz2

matriz_1 = crear_matriz(3,4,random=True)
matriz_2 = crear_matriz(1,2,random=True)

total = sumar_matrices(matriz_1,matriz_2)

imprimir_matriz(matriz_1)
imprimir_matriz(matriz_2)

print(f"Total de la suma de sus elementos: {total}")