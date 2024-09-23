"""Debemos alquilar el servicio de transporte para llegar a Mar del Plata con un
grupo de personas, de cada persona debemos obtener los siguientes datos:

- número de cliente
- estado civil ("soltero", "casado"  o "viudo")
- edad (solo mayores de edad, más de 17)
- dni (validar que el numero sea de 8 digitos)

NOTA: el precio por pasajero es de $60000.

Se debe informar (solo si corresponde):

a)  La cantidad de personas con estado "casado" de más de 40 años y
    menos de 60 años.
b)  el número de cliente y edad de la mujer soltera más joven.
c)  cuánto sale el viaje total sin descuento.
d)  si hay más del 50% de los pasajeros que tiene más de 60 años , el precio
    final tiene un descuento del 25%, que solo mostramos si corresponde.

Crear funciones para realizar la validación e ingreso de datos, incorporandolas a nuestros módulos

"""
from paquete.funciones import *
precio_pasaje = 60000

punto_a = "Casados de 40 a 60 años: 0"
punto_b = "mujer mas joven: no hay"
punto_c = "Precio del viaje: $0"
punto_d = "Precio final: $0"

primer_edad = True
edad_menor = 0


print("Ingrese numero de cliente")
nro_cliente = ingresar_numero()
precio_total = 0
precio_final = 0
estado_civil = None
edad = 0
dni = 0

contador_a = 0
total_pasajeros = 0

contador_mayor_60 = 0

descuento = 0.25

while nro_cliente != None:
   
    limpiar()
    total_pasajeros += 1

    estado_civil = ingresar_estado()

    sexo = ingresar_sexo()

    edad = ingresar_edad(minimo=18)
        
    dni = ingresar_dni()


    if (estado_civil == "casado") and (edad > 39 and edad < 61):
        contador_a += 1
    

    punto_a = f"Casados de 40 a 60 años: {contador_a}" 

    if sexo == "F" :
        if primer_edad:
            edad_menor = edad
            primer_edad = False
        elif edad < edad_menor :
            edad_menor = edad
            
        punto_b = f"Mujer mas joven: {dni},{edad} años"        


    precio_total += precio_pasaje
    punto_c = f"Precio del viaje:  ${precio_total}"

    if edad > 60:
        contador_mayor_60 += 1

    if contador_mayor_60 > total_pasajeros // 2:
        precio_final = precio_total - (precio_total) * descuento
    else:
        precio_final = precio_total
    
    punto_d = f"Precio final: ${precio_final}"

    

    print("Ingrese numero de cliente")
    nro_cliente = ingresar_numero()

limpiar()
print(punto_a)
print(punto_b)
print(punto_c)
print(punto_d)






    

