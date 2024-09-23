def limpiar()->None:
    """limpiar pantalla
    """
    import os
    os.system("cls")

def ingresar_estado()->str:
    """ingresar estado civil

    Returns:
        str: estado civil "soltero" "casado" "viudo"
    """
    estado = None
    while estado != "soltero" and estado != "casado" and estado != "viudo":
        estado = input("Ingresar estado civil: soltero - casado - viudo   ")
        estado = estado.lower()
    return estado

def ingresar_edad(minimo:int)->int:
    """ingresar edad

    Args:
        minimo (int): limite de edad minimo

    Returns:
        int: edad
    """
    
    while True :
            limpiar()
            print(f"Ingresar edad(+{minimo}): ")
            edad = ingresar_numero()
            if edad != None :
                 if edad >= minimo:
                    return edad
    
def ingresar_nombre()->str:
    """ingresar nombre

    Returns:
        str: nombre
    """
    return input("Ingresar nombre:  ")

def ingresar_sexo()->str:
    """ingresar sexo

    Returns:
        str: sexo "F", "M"
    """
    while True:
        limpiar()
        sexo = input("Ingresar sexo: F / M :  ")

        if sexo == "f" or sexo == "m" or sexo == "F" or sexo == "M":
            sexo = sexo.upper()
            return sexo

def ingresar_dni()->int:
    """ingresar DNI

    Returns:
        int DNI (8 digitos)
    """
    dni = 0

    while True:
        limpiar()
        print("Ingresar DNI:  ")
        dni = ingresar_numero()
        if dni != None:
            if validar_largo(8,dni):
                return dni

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

def validar_largo(cantidad_caracteres:int,numero:int)->bool:
    """validar largo de un numero

    Args:
        cantidad_caracteres (int): cantidad de digitos deseada
        numero (int): numero a verificar

    Returns:
        bool: True si el numero cumple con la cantidad de digitos
    """
    numero = str(numero)
    return len(numero) == cantidad_caracteres

