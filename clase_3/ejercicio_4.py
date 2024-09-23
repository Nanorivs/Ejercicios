"""Realizar un programa en donde se puedan utilizar los prototipos de la función
Sumar en sus 4 combinaciones.
sumar1(int, int) -> int;
sumar2() -> int;
sumar3(int, int) -> None;
sumar4() -> None;
"""
def sumar1(operando1:int,operando2:int)->int:
    """sumar mediante parametros

    Args:
        operando1 (int): operando 1
        operando2 (int): operando 2

    Returns:
        int: suma de los operandos
    """
    return operando1 + operando2

def sumar2() -> int:
    """sumar con input interno

    Returns:
        int: retorna la suma de los inputs
    """
    operando1 = int(input("Ingresar operando 1: "))
    operando2 = int(input("Ingresar operando 2: "))
    return operando1 + operando2

def sumar(operando1:int,operando2:int) -> None:
    """sumar mediante parametros,sin retorno

    Args:
        operando1 (int): operando 1
        operando2 (int): operando 2
    """
    print(f"{operando1} + {operando2} = {operando1+operando2}")

def sumar4() -> None:
    """sumar con input interno, sin retorno
    """
    operando1 = int(input("Ingresar operando 1: "))
    operando2 = int(input("Ingresar operando 2: "))
    print(f"{operando1} + {operando2} = {operando1+operando2}")


