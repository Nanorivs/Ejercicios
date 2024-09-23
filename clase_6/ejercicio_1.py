"""Implementar las funciones de esta seccion utilizando tanto recursividad como repetitividad:


1- Desarrolla una funcion que calcule la suma de los digitos de un numero. 

"""

def ingresar_numero()->int:
    """ingresar numero

    Returns:
        int: numero entero, sino None
    """
    
    numero = input()

    if numero == "":
        return
    
    for caracter in numero:
        if caracter < "0" or caracter > "9":
            return
        
    numero = int(numero)
    
    return numero

def suma_recursiva(numero:int)->int:
    """suma recursiva

    Args:
        numero (int): numero entero

    Returns:
        int: suma de los digitos de un numero entero
    """

    if numero < 10:
        return numero
    else:
        
        return numero % 10 + suma_recursiva(numero//10)
    
def suma_repeticion(numero:int)->int:
    """suma por repeticion

    Args:
        numero (int): numero entero

    Returns:
        int: suma de los digitos de un numero entero
    """

    numero = str(numero)
    suma = 0

    for digito in numero:
        suma += int(digito)

    return suma
    
print(f"Suma recursiva de 123: {suma_recursiva(123)}" )
print(f"Suma por repetición de 123: {suma_repeticion(123)}")

