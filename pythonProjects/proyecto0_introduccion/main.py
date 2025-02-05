def tiposDeDatos():
    """
    Los tipos de datos en Python son: int, float, complex, str, bool, list, tuple, dict, set.
    """

    entero = 5
    flotante = 5.5
    complejo = 5 + 5j
    cadena = 'Hola mundo'
    booleano = True

    print(f'Entero: {entero}')
    print(f'Flotante: {flotante}')
    print(f'Complejo: {complejo}')
    print(f'Cadena: {cadena}')
    print(f'Booleano: {booleano}')

    print(f'Tipo de dato de la variable entero: {type(entero)}')
    print(f'Tipo de dato de la variable flotante: {type(flotante)}')
    print(f'Tipo de dato de la variable complejo: {type(complejo)}')
    print(f'Tipo de dato de la variable cadena: {type(cadena)}')
    print(f'Tipo de dato de la variable booleano: {type(booleano)}')

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

def difernciaEntreListasYTuplas():
    """
    Las listas son mutables, es decir, se pueden modificar sus elementos.
    Las tuplas son inmutables, es decir, no se pueden modificar sus elementos.

    Las listas se definen con corchetes [] y las tuplas con paréntesis ().
    """

    lista = [1, 2, 3]
    tupla = (1, 2, 3)

    lista[0] = 4
    print(lista)

    try:
        tupla[0] = 4
    except TypeError:
        print('No se puede modificar una tupla')

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

def estructurasControl():
    """
    Las estructuras de control en Python son: if, elif, else, for, while.
    """

    edad = 18

    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')

    for i in range(5):
        print(i)

    x = 0
    while x < 5:
        print(x)
        x += 1

def entradaSalida():
    """
    La entrada y salida de datos en Python se realiza con las funciones input() y print().
    """

    nombre = input('Ingresa tu nombre: ')
    print(f'Hola {nombre}')

def excepciones():
    """
    Las excepciones en Python se manejan con las sentencias try, except, else, finally.
    """

    try:
        x = 5 / 0
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    else:
        print('División exitosa')
    finally:
        print('Fin del programa')

if __name__ == '__main__':
    """
    Función principal.
    __name__ es una variable especial que se inicializa con el valor 
    '__main__' cuando el script se ejecuta directamente
    
    Si el script se importa como un módulo, __name__ se inicializa con el nombre del módulo.
    """
    tiposDeDatos()
    operadoresAritmeticos()
    operadoresComparacion()
    listasPython()
    tuplasPython()
    difernciaEntreListasYTuplas()
    diccionariosPython()
    setsPython()
    operadoresLogicos()
    estructurasControl()
    entradaSalida()
    excepciones()
