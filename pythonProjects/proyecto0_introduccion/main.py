def operadoresAritmeticos():
    suma = 5 + 2
    resta = 5 - 2
    multiplicacion = 5 * 2
    division = 5 / 2
    divisionEntera = 5 // 2
    modulo = 5 % 2
    potencia = 5 ** 2

    print(f'Suma: {suma}')
    print(f'Resta: {resta}')
    print(f'Multiplicación: {multiplicacion}')
    print(f'División: {division}')
    print(f'División entera: {divisionEntera}')
    print(f'Módulo: {modulo}')
    print(f'Potencia: {potencia}')

def operadoresComparacion():
    igualdad = 5 == 2
    diferencia = 5 != 2
    mayorQue = 5 > 2
    menorQue = 5 < 2
    mayorOIgualQue = 5 >= 2

    print(f'Igualdad: {igualdad}')
    print(f'Diferencia: {diferencia}')
    print(f'Mayor que: {mayorQue}')
    print(f'Menor que: {menorQue}')
    print(f'Mayor o igual que: {mayorOIgualQue}')

def listasPython():
    """
    Las listas en Python son colecciones de elementos ordenados y mutables.
    :return:
    """

    lista = [1, 2, 3, 4, 5]
    print(lista)
    print(f'Elemento en la posición 0: {lista[0]}')
    print(f'Elemento en la posición 1: {lista[1]}')
    print(f'Elemento en la posición 2: {lista[2]}')
    print(f'Elemento en la posición 3: {lista[3]}')
    print(f'Elemento en la posición 4: {lista[4]}')
    print(f'Elemento en la posición -1: {lista[-1]}')
    print(f'Elemento en la posición -2: {lista[-2]}')
    print(f'Elemento en la posición -3: {lista[-3]}')
    print(f'Elemento en la posición -4: {lista[-4]}')
    print(f'Elemento en la posición -5: {lista[-5]}')

    lista[0] = 6
    print(lista)

def tuplasPython():
    """
    Las tuplas en Python son colecciones de elementos ordenados e inmutables.
    """

    tupla = (1, 2, 3, 4, 5)
    print(tupla)
    print(f'Elemento en la posición 0: {tupla[0]}')
    print(f'Elemento en la posición 1: {tupla[1]}')
    print(f'Elemento en la posición 2: {tupla[2]}')
    print(f'Elemento en la posición 3: {tupla[3]}')
    print(f'Elemento en la posición 4: {tupla[4]}')
    print(f'Elemento en la posición -1: {tupla[-1]}')
    print(f'Elemento en la posición -2: {tupla[-2]}')
    print(f'Elemento en la posición -3: {tupla[-3]}')
    print(f'Elemento en la posición -4: {tupla[-4]}')
    print(f'Elemento en la posición -5: {tupla[-5]}')

"""
Las listas son mutables, es decir, se pueden modificar sus elementos.
Las tuplas son inmutables, es decir, no se pueden modificar sus elementos.
    
Las listas se definen con corchetes [] y las tuplas con paréntesis ().
"""

def diccionariosPython():
    """
    Los diccionarios en Python son colecciones de elementos no ordenados, mutables e indexados.
    """

    diccionario = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'edad': 28
    }
    print(diccionario)
    print(f'Nombre: {diccionario["nombre"]}')
    print(f'Apellido: {diccionario["apellido"]}')
    print(f'Edad: {diccionario["edad"]}')

    diccionario['nombre'] = 'Karla'
    print(diccionario)

    diccionario['sexo'] = 'Femenino'
    print(diccionario)

    del diccionario['sexo']
    print(diccionario)

def setsPython():
    """
    Los sets en Python son colecciones de elementos no ordenados y sin elementos duplicados.
    """

    set1 = {1, 2, 2, 3, 3, 4, 5}
    print(set1)

    set2 = {3, 4, 5, 6, 7}
    print(set2)

    print(f'Unión: {set1 | set2}')
    print(f'Intersección: {set1 & set2}')
    print(f'Diferencia: {set1 - set2}')
    print(f'Diferencia simétrica: {set1 ^ set2}')

def operadoresLogicos():
    """
    Los operadores lógicos en Python son: and, or, not.
    """

    a = True
    b = False

    print(f'AND: {a and b}')
    print(f'OR: {a or b}')
    print(f'NOT: {not a}')

if __name__ == '__main__':
    operadoresAritmeticos()
    operadoresComparacion()
    listasPython()
    tuplasPython()
    diccionariosPython()
    setsPython()
    operadoresLogicos()
