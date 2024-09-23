"""Escribir un programa que determine si un año es bisiesto.

Un año es bisiesto si es múltiplo de 4. Los años múltiplos de 100 no son
bisiestos, salvo si ellos también son múltiplos de 400.

Por ejemplo: el año 2000 es bisiesto pero 1900 no.

Pedirle al usuario un año de inicio y otro de fin y mostrar todos los años
bisiestos en ese rango.
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

def es_anio_bisiesto(anio:int)->bool:
    """verificar año bisiesto

    Args:
        anio (int): año

    Returns:
        bool: si es bisiesto, True
    """
    return anio % 4 == 0 and anio % 100 != 0


print("Ingresar año de inicio:   ")
inicio = ingresar_numero()

print("Ingresar año de fin")
fin = ingresar_numero()

if inicio != None and fin != None:

    if inicio > fin:
        auxiliar = fin
        fin = inicio
        inicio = auxiliar
    
    print(f"Años bisiestos entre {inicio} - {fin}: ")

    for año in range(inicio,fin):
        if es_anio_bisiesto(año):
            print(año)
else:
    print("Debe ingresar años validos")
        




