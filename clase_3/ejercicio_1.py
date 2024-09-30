"""Crear una función que permita determinar si un número es par o no.
La función retorna true en caso afirmativo y false en caso contrario.
"""
def es_par(numero:int)->bool:
    """es par

    Args:
        numero (int): numero

    Returns:
        bool: True si el numero es par
    """
    return numero % 2 == 0

print(f"2 es par: {es_par(2)}")


