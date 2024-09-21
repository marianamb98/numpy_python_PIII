import numpy as np

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    len_string = lambda x:  len(x)
    print("El título del libro 'Cien años de soledad', tiene", len_string('Cien años de soledad'), "caracteres")

    # 2)
    # Lista de string
    palabras = ['love', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.

    palabras_len = list(map(lambda x: len(x), palabras))


    # Desarrollo de 2) ***************************

    #palabras_len = map(len_string, palabras)
    #palabras_len = list(palabras_len)

    #print(palabras_len)
    
   # palabras_len = list(map(lambda x: len(x), palabras))

    print("La lista de palabras es:", palabras)
    print("El tamaño de cada palabra es:" , palabras_len, "respectivamente.")

    print("Ejercicio 2 - Finalizado")