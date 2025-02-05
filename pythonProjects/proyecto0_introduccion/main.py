"""
Proyecto 0: Introducción a Python.

Este proyecto es una introducción a Python, en el cual se explican los conceptos básicos de Python.

Creado por: Daniel Fernández | 05/02/2025

Cuenta con funciones que explican los conceptos básicos de Python, estas se llaman en el main.
"""

def tiposDeDatos():
    """
    Los tipos de datos en Python son: int, float, complex, str, bool, list, tuple, dict, set.

    int: Números enteros.
    float: Números decimales.
    complex: Números complejos.
    str: Cadenas de texto.
    bool: Valores booleanos (True o False).
    list: Listas.
    tuple: Tuplas.
    dict: Diccionarios.
    set: Sets.
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
    """
    Los operadores aritméticos en Python son: +, -, *, /, //, %, **.

    +: Suma.
    -: Resta.
    *: Multiplicación.
    /: División.
    //: División entera.
    %: Módulo.
    **: Potencia.
    """

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
    """
    Los operadores de comparación en Python son: ==, !=, >, <, >=, <=.

    ==: Igualdad.
    !=: Diferencia.
    >: Mayor que.
    <: Menor que.
    >=: Mayor o igual que.
    <=: Menor o igual que.

    """

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

    Las listas se definen con corchetes [].
    a una lista se accede mediante su índice.
    """

    lista = [1, 2, 3, 4, 5]
    print(lista)
    print(f'Elemento en la posición 0: {lista[0]}')
    print(f'Elemento en la posición 1: {lista[1]}')

    # también se puede acceder a los elementos de una lista mediante índices negativos (de derecha a izquierda)
    print(f'Elemento en la posición -4: {lista[-4]}')
    print(f'Elemento en la posición -5: {lista[-5]}')

    lista[0] = 6
    print(lista)

    """
    Con la lista puedes hacer varias funciones, como agregar elementos, eliminar elementos, etc.
    """
    # Agregar elementos
    lista.append(6)
    print(lista)

    # Eliminar elementos por valor
    lista.remove(6)
    print(lista)

    # Insertar elementos
    lista.insert(0, 6)
    print(lista)

    """
    Diferencia entre agregar e insertar, agregar agrega al final de la lista, 
    insertar agrega en la posición que le indiques
    """

    # Eliminar elementos por índice
    lista.pop(0)
    print(lista)

    # Eliminar elementos repetidos
    lista.append(6)
    lista.append(6)
    print(lista)
    lista = list(set(lista))
    print(lista)

    """
    Para eliminar elementos repetidos, se convierte la lista en un set y luego se vuelve a convertir en lista.
    Es un truquito para eliminar elementos repetidos.
    """

    # Ordenar elementos
    lista.sort()
    print(lista)

    # Invertir elementos
    lista.reverse()
    print(lista)

    # Longitud de la lista
    print(len(lista))

    # Copiar una lista
    lista2 = lista.copy()
    print(lista2)

    """
    Para copiar una lista, no se puede hacer lista2 = lista, ya que si se modifica lista2, también se modifica lista.
    Por ello, se usa el método copy().
    """

    # Limpiar una lista
    lista.clear()
    print(lista)

    # Eliminar una lista
    del lista
    try:
        print(lista)
    except NameError:
        print('La lista ya no existe')

def tuplasPython():
    """
    Las tuplas en Python son colecciones de elementos ordenados e inmutables.

    Cuando usar una tupla frente a una lista:
    - Cuando no necesitas modificar los elementos.
    - Cuando quieres una lista más rápida.
    - Cuando quieres hacer una clave de un diccionario.
    - Cuando quieres usar una tupla como un argumento de una función.
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

def diferenciaEntreListasYTuplas():
    """
    Las listas son mutables, es decir, se pueden modificar sus elementos.
    Las tuplas son inmutables, es decir, no se pueden modificar sus elementos.

    Las listas se definen con corchetes [] y las tuplas con paréntesis ().

    Las listas son mas rápidas que las tuplas. (se puede comprobar con el módulo timeit)
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

    Los diccionarios se definen con llaves {}.

    Los diccionarios se acceden mediante clave-valor.
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

    Los sets se definen con llaves {}.

    Los sets se pueden realizar operaciones de conjuntos como unión, intersección, diferencia y diferencia simétrica.

    Los sets no soportan indexación, es decir, no se puede acceder a un elemento mediante su índice.
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

    and: Devuelve True si ambos operandos son True.
    or: Devuelve True si al menos uno de los operandos es True.
    not: Devuelve True si el operando es False.
    """

    a = True
    b = False

    print(f'AND: {a and b}')
    print(f'OR: {a or b}')
    print(f'NOT: {not a}')

def estructurasControl():
    """
    Las estructuras de control en Python son: if, elif, else, for, while.

    Algo importante es que en python al no tener ; o no usar llaves importa la indentación.
    """

    """
    Vamos a hacer un if para saber si eres mayor de edad o no.
    
    Primero lo haremos con una buena identación y luego con una mala identación.
    """

    #Bien identado
    edad = 18
    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')
        print("Esto se ejecuta siempre que no se cumpla la condición")

    #Mal identado
    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')
    print("Esto se ejecuta siempre")

    """
    Logicamente aqui también importa la identación.
    """

    # for
    for i in range(5):
        print(i)

    # while
    x = 0
    while x < 5:
        print(x)
        x += 1

def entradaSalida():
    """
    La entrada y salida de datos en Python se realiza con las funciones input() y print().

    input(): Lee una cadena de texto desde la entrada estándar.
    print(): Escribe una cadena de texto en la salida estándar.
    """

    nombre = input('Ingresa tu nombre: ')
    print(f'Hola {nombre}')

def excepciones():
    """
    Las excepciones en Python se manejan con las sentencias try, except, else, finally.

    try: Bloque de código que puede lanzar una excepción.
    except: Bloque de código que se ejecuta si se lanza una excepción.
    else: Bloque de código que se ejecuta si no se lanza una excepción.
    finally: Bloque de código que se ejecuta siempre, haya o no una excepción.

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
    diferenciaEntreListasYTuplas()
    diccionariosPython()
    setsPython()
    operadoresLogicos()
    estructurasControl()
    entradaSalida()
    excepciones()
