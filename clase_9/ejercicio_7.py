from paquete.funciones import *
""" Realizar una funcion que calcule el producto entre una matriz y un escalar"""


def multiplicar_matriz(matriz:list,escalar:int)->None:
    """multiplicar matriz por un escalar

    Args:
        matriz (list):  matriz
        escalar (int): escalar
    """

    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in range(filas):
        for columna in range(columnas):
            matriz[fila][columna] *= escalar

matriz = crear_matriz(3,3,random=True)


imprimir_matriz(matriz)

print("Ingresar un numero")
escalar = ingresar_numero()
print(f"Matriz multiplicada por {escalar}")
multiplicar_matriz(matriz,escalar)
imprimir_matriz(matriz)



