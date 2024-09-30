from paquete.funciones import *
""" Realizar una funcion que cree una matriz de NxM cantidad de filas y columnas"""

print("Ingresar cantidad de filas: ")
filas = ingresar_numero()

print("Ingresar cantidad de columnas: ")
columnas = ingresar_numero()

matriz = crear_matriz(filas,columnas,random=True)

print("Nueva matriz")
imprimir_matriz(matriz)

