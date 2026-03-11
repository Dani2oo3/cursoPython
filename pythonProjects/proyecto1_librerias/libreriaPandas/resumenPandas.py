import pandas as pd

# Crear un DataFrame de personas y sus alturas
personas = pd.DataFrame({ 'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana'], 'Altura': [1.75, 1.65, 1.80, 1.70] })

if __name__ == '__main__':
    print('Resumen de Pandas')

    # Mostrar el DataFrame
    print(personas)

    # Mostrar la altura promedio
    print(personas['Altura'].mean())

    # Mostrar la altura máxima
    print(personas['Altura'].max())

    # Mostrar la altura mínima
    print(personas['Altura'].min())

    # Mostrar la altura de la persona más alta
    print(personas[personas['Altura'] == personas['Altura'].max()])