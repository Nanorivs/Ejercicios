"""Debe crear un programa que permita ingresar:

    -una edad (entre 1 y 99 años, validar mediante una funcion)
    -un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos
    (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje
     y terminar el programa.
   
    Si todos los datos fueron bien ingresados, el programa debe ser capaz de
    indicar, sabiendo que las mujeres se jubilan a los 60 años o mas,
    los hombres con 65 años o mas,
    para los no binarios establecemos un promedio de ambas edades.


    Determinar mediante funciones si una persona puede o no jubilarse.
"""

def ingresar_edad(min:int,max:int)->int:
    """ingresar edad

    Args:
        min (int): limite de edad inferior
        max (int): limite de edad superior

    Returns:
        int:  edad entre el rango establecido, sino None
    """
    
    edad = input()

    if edad == "":
        return
    
    for caracter in edad:
        if caracter < "0" or caracter > "9":
            return
        
    edad = int(edad)
    if edad < min or edad > max:
        return  
    
    return edad

def ingresar_genero()->str:
    """ingresar genero

    Returns:
        str: genero "F" / "M" / "X" caso contrario None
    """

    genero = input()
    genero = genero.upper()

    if genero != "F" and genero != "M" and genero != "X":
        genero = None

    return genero

def validar_jubilacion(genero:str,edad:int)->bool:
    """validar jubilacion 

    Args:
        genero (str): genero de la persona
        edad (int): edad de la persona

    Returns:
        bool: True si  la persona puede jubilarse
    """
    jubilacion = False

    if genero == "F" and edad > 59:
        jubilacion = True
    elif genero == "M" and edad > 64:
        jubilacion = True
    elif genero == "X" and edad > 62:
        jubilacion = True
    
    return jubilacion

print("Ingresar genero:   F - M - X ")
genero = ingresar_genero()

print("Ingresar edad: ")
edad = ingresar_edad(min=1,max=99)

if genero == None:
    print("Genero inexistente")
if edad == None:
    print("Edad invalida")

if genero != None and edad != None:
    if validar_jubilacion(genero,edad):
        print("Se puede jubilar  ")
    else:
        print("No se puede jubilar  ")


