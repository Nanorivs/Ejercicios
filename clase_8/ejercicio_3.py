"""3-Escribir una función que calcule y retorne el producto de todos los elementos 
de la lista que recibe como parámetro."""

from paquete.validaciones import *

def producto_numeros(lista:list)->float:
    """producto de numeros

    Args:
        lista (list): lista

    Returns:
        float: producto de los numeros de una lista, si no hay, None
    """
    if verificar_tipo(lista,list):
        producto = 1
        for numero in lista:
            if verificar_tipo(numero,int) or verificar_tipo(numero,float):
                producto *= numero
        return producto
                    
        
    

lista = ["S",3,"#",-3 ]
print(f"Promedio de la lista: {producto_numeros(lista)}")