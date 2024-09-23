"""6-Escribir una función llamada reemplazar_nombres que reciba como parámetros 
una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. 
La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista 
con su correspondiente reemplazo y luego retornar la cantidad total de 
reemplazos realizados."""
from paquete.validaciones import *

def reemplazar_nombres(lista:list,nombre:str,reemplazo:str)->int:
    """reemplazar nombres

    Args:
        lista (list): lista
        nombre (str): nombre a reemplazar
        reemplazo (str): reemplazo

    Returns:
        int: cantidad de reemplazos que se realizó en la lista
    """
    reemplazos = 0
    if verificar_tipo(lista,list):
        for elemento in lista:
            if verificar_tipo(elemento,str):
                if elemento == nombre:
                    elemento = reemplazo
                    reemplazos += 1
    return reemplazos



lista = ["Lolo",9,"%a",79]
print(f"Reemplazos:  {reemplazar_nombres(lista,"Lolo","Don")}")


            

