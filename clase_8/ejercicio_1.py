"""1-Escribir una función que reciba una lista de enteros, la misma calculará y 
devolverá el promedio de todos los números"""
from paquete.validaciones import *

def promedio_lista(lista:list)->float:
    """promedio de una lista

    Args:
        lista (list): lista

    Returns:
        float: promedio de los elementos que son numeros enteros de una lista
    """
    if verificar_tipo(lista,list):
        total = 0
        cantidad_numeros = 0
        for numero in lista:
            if verificar_tipo(numero,int) or verificar_tipo(numero,float):
                total += numero
                cantidad_numeros += 1
        if cantidad_numeros == 0:
            cantidad_numeros = 1
        return total / cantidad_numeros
    

lista = ["S",3,"#",0 ]
print(f"Promedio de la lista: {promedio_lista(lista)}")
