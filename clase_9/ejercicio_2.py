from paquete.funciones import *
"""  Realizar una funcion que cree una matriz identidad de N cantidad de filas y columnas """

def crear_matriz_identidad(tamanio:int)->list:
    matriz = crear_matriz(tamanio,tamanio)
    
    for indice in range(tamanio):
        matriz[indice][indice] = 1

    return matriz

print("Matriz cuadrada")
print("Ingresar tamaño de matriz ")
tamanio = ingresar_numero()
matriz = crear_matriz_identidad(tamanio)

print("matriz identidad: ")
imprimir_matriz(matriz)



