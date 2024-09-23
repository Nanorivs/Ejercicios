"""Crear una función que determine si un numero es primo
La función retorna true en caso afirmativo y false en caso contrario.
"""
def es_numero_primo(numero:int)->bool:
    """verificar si es un numero primo

    Args:
        numero (int): numero

    Returns:
        bool: True si es un numero primo
    """
    respuesta = None
    
    if numero > 0:
        respuesta = True
        for divisor in range(1,numero):
            if numero % divisor == 0:
                respuesta = False
                break
    
    return respuesta