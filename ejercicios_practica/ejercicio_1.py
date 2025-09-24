# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # numeros_potencia = list(map....)

    # Desarrollo de 1) ***************************
    
    potencia_2 = lambda x: x**2
    pot_3 = potencia_2(3)

    print('El número 3 elevado al cuadrado es:',pot_3)

    # Desarrollo de 2) ***************************

    numeros_map = map(potencia_2, numeros)
    numeros_map = list(numeros_map)

    print(numeros_map)
    
    numeros_lambda = list(map(lambda x: x**2, numeros))

    print(numeros_lambda)


    print("Ejercicio 1 Finalizado")
