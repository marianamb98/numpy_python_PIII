import numpy as np

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.

    lista_str = ['5', 'b', '3', '', '7', 'NaN', 'E', '0']
    lista_num = [int(x) if (x.isdigit()) else 0 for x in lista_str]
    print("La lista inicial es:", lista_str)
    print("El resultado de la conversión de la lista es:", lista_num)

    # Prueba con número negativo

    lista_str = ['-5', 'b', '-3', '', '7', 'NaN', 'E', '0']
    lista_numeros = [int(x) if(x.isdigit()) else 0 for x in lista_str]
    print("Lista inicial con numeros negativos:", lista_str)
    print("Conversión de la lista:", lista_numeros)

    print('La función isdigit tomó los numeros negativos como string')

    lista_numeros = [int(x) if(x.lstrip('-').isdigit()) else 0 for x in lista_str]
    print('Si utilizo el método lstrip, la lista resultante será:', lista_numeros)

    print("Ejercicio 4 - Finalizado")