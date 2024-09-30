from paquete.funciones import *
""" Realizar una funcion que calcule la suma de todos los elementos de una columna perteneciente a una matriz"""
def suma_de_elementos_columna_matriz(matriz:list)->list:
    """Sumar elementos de una matriz

    Args:
        matriz (list) : suma total de los elementos de las columnas de una matriz
    """
    lista_totales = list()

    columnas = len(matriz[0])
    filas = len(matriz)


    for fila in range(filas):
        total = 0
        for columna in range(columnas):
            total += matriz[columna][fila]
        lista_totales.append(total)        
    
    return lista_totales

matriz = crear_matriz(3,3,random=True)
lista_suma_columnas = suma_de_elementos_columna_matriz(matriz)

print()
imprimir_matriz(matriz)
print()
for i in range(len(lista_suma_columnas)):
    print(f"Total columna {i+1}: {lista_suma_columnas[i]}")


