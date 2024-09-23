"""Crear una función que calcule el resultado de la potencia entre dos numeros
recibidos por parametro y lo retorne. Validar que el exponente no sea negativo"""

def potencia(base:int,potencia:int)->int:
    """potencia

    Args:
        base (int): base
        potencia (int): exponente

    Returns:
        int: numero elevado a un exponente
    """
    resultado = 1

    if potencia > 0:
        for i in range(potencia):
            resultado *= base
    
    else:
        return 

    return resultado

print(f"2 al cuadrado: {potencia(2,2)}")