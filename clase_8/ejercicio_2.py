"""2-Escribir una función parecida a la anterior, pero la misma deberá calcular y 
devolver el promedio de los números positivos."""

from paquete.validaciones import *

def promedio_positivos(lista:list)->float:
    """promedio de una lista

    Args:
        lista (list): lista

    Returns:
        float: promedio de los numeros positivos dentro de una lista
    """
    if verificar_tipo(lista,list):
   
        total = 0
        cantidad_numeros = 0
        for numero in lista:
            if verificar_tipo(numero,int) or verificar_tipo(numero,float):
                if numero > 0:
                    total += numero
                    cantidad_numeros += 1
        if cantidad_numeros == 0:
            cantidad_numeros = 1
        return total / cantidad_numeros
    

lista = ["S",3,"#",-3 ]
print(f"Promedio de la lista: {promedio_positivos(lista)}")