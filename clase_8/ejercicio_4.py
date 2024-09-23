"""4-Escribir una función que reciba como parámetros una lista de enteros y 
retorne la posición del valor máximo encontrado."""

from paquete.validaciones import *

def maximo_entero(lista:list)->float:
    """maximo entero

    Args:
        lista (list): lista

    Returns:
        float: indice del maximo valor entero
    """
    if verificar_tipo(lista,list):
       primer_entero = True
       max_entero = 0
       indice = 0
       for i in range(len(lista)):
            if verificar_tipo(lista[i],int):
                numero_actual = lista[i]
                if primer_entero:
                   max_entero = numero_actual
                   primer_entero = False
                   indice = i
                elif numero_actual > max_entero:
                    max_entero = numero_actual
                    indice = i

       if  primer_entero:
            indice = None
       return indice
       
                
    
if __name__ == "__main__":
    lista = ["S",3,"#",-3 ]
    print(f"Indice: {maximo_entero(lista)} ")

