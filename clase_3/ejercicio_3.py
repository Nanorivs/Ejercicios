"""Crear una función que pida el ingreso de un numero. Validar que dicho ingreso
sea un numero antes de retornarlo. En caso afirmativo, retornar el numero,
caso contrario retornar None
"""
def verificar_entero()->int:    
    """verificar entero

    Returns:
        int: si el input es un entero,se retorna un entero
    """
    numero = input("Ingresar numero: ")

    for caracter in numero:
    
        if caracter < "0" or caracter > "9":
            numero = None
            break
        
    return numero

print(verificar_entero())

