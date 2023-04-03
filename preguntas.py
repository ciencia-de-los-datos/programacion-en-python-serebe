"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214

    """
    # ejercicio numero 1
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    contador=0
    for i in range(0,len(informacion)):
        contador+=int(informacion[i][1])
    return contador


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    # ejercicio numero 2
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][0])
    elementos=sorted(set(lista))
    auxiliar_2=list()
    for i in elementos:
        contador=0
        for j in range(0,len(informacion)):
            if i==informacion[j][0]:
                contador+=1
        auxiliar_2.append((i,contador))
    return [auxiliar_2[index] for index in range(0,len(auxiliar_2))]


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    # ejercicio numero 3
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][0])
    elementos=sorted(set(lista))
    auxiliar_2=list()
    for i in elementos:
        contador=0
        for j in range(0,len(informacion)):
            if i==informacion[j][0]:
                contador+=int(informacion[j][1])
        auxiliar_2.append((i,contador))
    return auxiliar_2


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    # ejercicio numero 4
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][2][5:7])
    elementos=sorted(set(lista))
    auxiliar_2=list()
    for i in elementos:
        contador=0
        for j in range(0,len(informacion)):
            if i==informacion[j][2][5:7]:
                contador+=1
        auxiliar_2.append((i,contador))
    return auxiliar_2


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    # ejercicio numero 5
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][0])
    elementos=sorted(set(lista))
    auxiliar_2=list()
    for i in elementos:
        auxiliar=list()
        for j in range(0,len(informacion)):
            if i==informacion[j][0]:
                auxiliar.append(int(informacion[j][1]))
        auxiliar_2.append((i,max(auxiliar),min(auxiliar)))
    return auxiliar_2


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    # ejercicio numero 6
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista_2=list()
    contador=list()
    for k in range(0,len(informacion)):
        lista=[informacion[k][4].replace(',',':').split(':')[index] for index in range(0,len(informacion[k][4].replace(',',':').split(':')),2)]
        for i in range(0,len(lista)):
            lista_2.append(lista[i])
    elementos=sorted(set(lista_2))
    auxiliar_2=list()
    for k in elementos:
        auxiliar=list()
        for j in range(0,len(informacion)):
            lista=informacion[j][4].replace(',',':').split(':')
            if k in lista:
                auxiliar.append(int(lista[lista.index(k)+1]))
        auxiliar_2.append((k,min(auxiliar),max(auxiliar)))
    return auxiliar_2


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    # ejercicio numero 7
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][1])
    elementos=sorted(set(lista))
    auxiliar_2=list()
    for g in elementos:
        auxiliar=list()
        for j in range(0,len(informacion)):
            if g==informacion[j][1]:
                auxiliar.append(informacion[j][0])
        auxiliar_2.append((int(g),auxiliar)) 
    return auxiliar_2


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    # ejercicio numero 8
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][1])
    elementos=sorted(set(lista))
    auxiliar_2=list()
    for g in elementos:
        auxiliar=list()
        for j in range(0,len(informacion)):
            if g==informacion[j][1]:
                if g not in auxiliar:
                    auxiliar.append(informacion[j][0])
        auxiliar_2.append((int(g),sorted(set(auxiliar)))) 
    return auxiliar_2


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # ejercicio numero 9
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista_2=list()
    contador=list()
    for k in range(0,len(informacion)):
        lista=[informacion[k][4].replace(',',':').split(':')[index] for index in range(0,len(informacion[k][4].replace(',',':').split(':')),2)]
        for i in range(0,len(lista)):
            lista_2.append(lista[i])
    elementos=sorted(set(lista_2))
    auxiliar_2=dict()
    for k in elementos:
        contador=0
        for j in range(0,len(informacion)):
            lista=informacion[j][4].replace(',',':').split(':')
            if k in lista:
                contador+=1
        auxiliar_2[k]=contador
    return auxiliar_2


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    # ejercicio numero 10
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    for i in range(0,len(informacion)):
        lista.append((informacion[i][0],len(informacion[i][3].split(',')),len(informacion[i][4].split(','))))
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    # ejercicio numero 11
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista_2=list()
    contador=list()
    for k in range(0,len(informacion)):
        lista=informacion[k][3].split(',')
        for i in range(0,len(lista)):
            lista_2.append(lista[i])
    elementos=sorted(set(lista_2))
    auxiliar_2=dict()
    for k in elementos:
        contador=0
        for j in range(0,len(informacion)):
            lista=informacion[j][3].split(',')
            if k in lista:
                contador+=int(informacion[j][1])
        auxiliar_2[k]=contador
    return auxiliar_2


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    # ejercicio numero 12
    def leer_archivo(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            lines=[line.replace('\n','')for line in lines]
        return [line.split("\t") for line in lines]
    informacion=leer_archivo("data.csv")
    lista=list()
    contador=0
    for i in range(0,len(informacion)):
        lista.append(informacion[i][0])
    elementos=sorted(set(lista))
    auxiliar_2=dict()
    for k in elementos:
        contador=0
        for j in range(0,len(informacion)):
            if k==informacion[j][0]:
                lista=informacion[j][4].replace(',',':').split(':')
                for m in range(1,len(lista),2):
                    contador+=int(lista[m])
        auxiliar_2[k]=contador
    return auxiliar_2
