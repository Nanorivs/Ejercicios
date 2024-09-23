"""Escribe funciones para calcular el área las siguientes figuras geométricas:
Circulo
Rectangulo
Cuadrado
Triangulo rectangulo
"""
PI = 3.14159
def calcular_area_circulo(radio:float)->float:
    """calcular el area de un circulo

    Args:
        radio (float): radio del circulo

    Returns:
        float: area del circulo
    """
    return PI * radio**2

def calcular_area_rectangulo(base:float,altura:float)->float:
    """calcular el area de un rectangulo

    Args:
        base (float): base
        altura (float): altura

    Returns:
        float: area del rectangulo
    """
    return base * altura

def calcular_area_cuadrado(lado:float)->float:
    """calcular el area de un cuadrado

    Args:
        lado (float): medida de un lado

    Returns:
        float: area de un cuadrado
    """
    return calcular_area_rectangulo(lado,lado)

def calcular_area_triangulo_rectangulo(base:float,altura:float)->float:
    """calcular el area de un triangulo rectangulo

    Args:
        base (float): base
        altura (float): altura

    Returns:
        float: el area de un triangulo rectangulo
    """
    return 0.5 * calcular_area_rectangulo(base,altura)

