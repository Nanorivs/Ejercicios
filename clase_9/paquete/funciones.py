def ingresar_numero()->int:
    """ingresar numero

    Returns:
        int: retorna un numero,caso contrario None
    """
    
    numero = input()

    if numero == "":
        return
    
    for caracter in numero:
        if caracter < "0" or caracter > "9":
            return
        
    numero = int(numero)
    return numero

def swap_values(value1:any,value2:any)->None:
    """swap values

    Args:
        value1 (any): variable 1
        value2 (any): variable 2

    Returns: None,intercambia valor de las variables
    """
    aux = value1
    value1 = value2
    value2 = aux
    
def numero_random(min:int,max:int)->int:    
    """numero random

    Args:
        min (int): limite inferior
        max (int): limite superior

    Returns:
        int: numero aleatorio entre el rango
    """
    from random import randint
    if  type(min)  != int or type(max) != int:
        return
    
    if min > max:
        aux = min
        min = max
        max = aux

    return randint(min,max)

def verificar_tipo(value: any, tipo_esperado: type) -> bool:
    """Verificar si la variable es del tipo especificado.

    Args:
        value (any): La variable a verificar.
        tipo_esperado (type): El tipo esperado de la variable.

    Returns:
        bool: True si la variable es del tipo especificado, False en caso contrario.
    """
    return isinstance(value, tipo_esperado)

def crear_matriz(filas:int,columnas:int,random:bool = False)->list:
    """crear matriz

    Args:
        matriz (list): 
        filas (int): cantidad de  filas
        columnas (int): cantidad de columnas
        ceros (bool) : si True,todos los elementos son cero

    Returns:
        list: matriz inicializada con ceros
    """
    matriz = [ ]
    for fila in range(filas):
        fila = []
        for columna in range(columnas):
            fila.append(0)

        matriz.append(fila)

    if random:
        for fila in range(filas):
            for columna in range(columnas):
                matriz[fila][columna] = numero_random(1,9)
    return matriz

def imprimir_matriz(matriz:list)->None:
    """imprimir matriz por consola

    Args:
        matriz (list): matriz
    """
    print()
    
    for fila in matriz:
        print(fila)

    print()
    


