from paquete.funciones import *
""" Realizar una funcion que calcule la suma de todos los elementos de una matriz """

def suma_de_elementos_matriz(matriz:list)->int:
    """Sumar elementos de una matriz

    Args:
        matriz (int) : suma total de los elementos de una matriz
    """
    total = 0
    for fila in matriz:
        
        for indice in range(len(fila)):
            total += fila[indice]
    
    return total

if __name__ == "__main__":

    matriz = crear_matriz(5,5,random=True)

    imprimir_matriz(matriz)

    suma = suma_de_elementos_matriz(matriz)
    print(f"Suma de sus elementos: {suma}")


            


