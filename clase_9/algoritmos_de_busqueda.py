#Algoritmos de busqueda

def busqueda_lineal(lista : list, valor : any) -> int:
    """
    Realiza una busqueda sobre una lista de forma lineal

    Parametros:
    lista: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o el indice del primer elemento que
    coincide con el valor buscado
    """
    retorno = None
    for i in range(len(lista)):
        if lista[i] == valor:
            retorno = i
            break
    return retorno


def busqueda_lineal_matriz(matriz : list, valor : any) -> list:
    """
    Realiza una busqueda sobre una matriz de forma lineal

    Parametros:
    matriz: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o una lista con los indices del elemento
    encontrado
    """
    retorno = None
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                retorno = [i,j]
                break
    return retorno

def busqueda_lineal_matriz2(matriz : list, valor : any) -> list:
    """
    Realiza una busqueda sobre una matriz de forma lineal

    Parametros:
    matriz: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o una lista con los indices del elemento
    encontrado
    """
    retorno = None
    for i in range(len(matriz)):
        resultado = busqueda_lineal(matriz[i], valor)
        if resultado != None:
            retorno = [i, resultado]
            break
    return retorno

#Estamos buscando el 2


# [ 1 , 2 , 3 , 4 , 5]
#   ^       ^       ^


# [ 4 ]
#   ^
def busqueda_binaria(lista, valor):
    """
    Realiza una busqueda sobre una lista ordenada de forma binaria

    Parametros:
    lista: representa el conjunto de datos sobre el cual se va a realizar la busqueda
    valor: valor del cual se desea saber su indice

    Retorno: 
    Retorna None si el valor no se encuentra o el indice del primer elemento que
    coincide con el valor buscado
    """
    
    izquierda = 0
    derecha =  len(lista) - 1
    retorno = None

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if valor == lista[medio]:
            retorno = medio
            break
        else:
            if valor > lista[medio]:
                izquierda = medio + 1
            else:
                derecha = medio - 1
    return retorno



lista = [1,2,3,4,5,6,7,8,9,10]

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#print(busqueda_lineal_matriz(matriz, 3))
#print(busqueda_lineal_matriz(matriz, 1))


print(busqueda_binaria(lista, 3))
print(busqueda_binaria(lista, 7))
print(busqueda_binaria(lista, 11))

