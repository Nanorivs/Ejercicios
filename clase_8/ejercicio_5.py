"""5-Escribir una función que reciba como parámetros una lista de enteros y 
muestre la/las posiciones en donde se encuentra el valor máximo hallado"""
from paquete.validaciones import *




def indices_maximo_entero(lista:list)->list:
    """indices de una lista

    Args:
        lista (list): lista

    Returns:
        list: indices del maximo valor entero de una lista
    """
    from ejercicio_4 import maximo_entero

    indice_valor_maximo = maximo_entero(lista)
    max_valor = lista[indice_valor_maximo]
    indices = [ ]    

    if indice_valor_maximo != None:
        for i in range(len(lista)):
                if lista[i] == max_valor:
                     indices.append(i)
    
    return indices     

      


lista = [10,"50",3,10,"$"]

print(f"Indices maximo entero: {indices_maximo_entero(lista)}")


