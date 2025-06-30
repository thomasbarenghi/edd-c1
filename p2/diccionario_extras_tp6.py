# -------------------------------------------------------
# CATEGORÍA: Utilidades con listas
# -------------------------------------------------------

# sin_los_repetidos(lista) -> list:
#   Retorna una nueva lista eliminando elementos repetidos.

# lista_a_dic(lista) -> Diccionario:
#   Devuelve un diccionario con cada elemento como clave, y como valor una lista
#   que repite dicho elemento tantas veces como aparece en la lista original.

# list_a_dic(lista_de_tuplas) -> Diccionario:
#   Convierte una lista de tuplas (clave, valor) en un diccionario agrupando
#   los valores en listas bajo sus respectivas claves.

# posibles_pares(dic) -> list[tuple]:
#   Retorna una lista de tuplas (clave, valor) con cada par posible presente en el diccionario.

# contador_apariciones(lista) -> Diccionario:
#   Devuelve un diccionario con la cantidad de apariciones de cada elemento en la lista.

# -------------------------------------------------------
# CATEGORÍA: Utilidades con Diccionario
# -------------------------------------------------------

# sin_los_repetidos_dic(lista) -> Diccionario:
#   Devuelve un diccionario con claves únicas de la lista y valores None.

# mezclar_diccionarios(dic1, dic2) -> Diccionario:
#   Devuelve un nuevo diccionario mezclando dic1 y dic2, priorizando los valores de dic1
#   en caso de claves duplicadas.

# administrar_materias(dic, alumno, materia) -> None:
#   Inserta una materia en la lista de materias del alumno solo si aún no estaba presente.

# contains_value(dic, value) -> bool:
#   Verifica si un valor está contenido en algún campo del diccionario.

# agregar_si_lista(lista, elemento, condicion) -> None:
#   Agrega un elemento a la lista solo si se cumple la condición.

# -------------------------------------------------------
# CATEGORÍA: Promedios y acumulación
# -------------------------------------------------------

# promedios(materias, notas) -> Diccionario:
#   Devuelve un diccionario con las materias como claves y el promedio de sus notas como valor.

# acumular_para_promedio(materias, notas) -> Diccionario:
#   Devuelve un diccionario con suma total y cantidad de notas por materia, para calcular promedios.
def sin_los_repetidos(lista):
    """
    Elimina elementos duplicados de una lista.

    Args:
        lista (list): Lista original con posibles elementos repetidos.

    Returns:
        list: Lista sin elementos repetidos.

    Example:
        >>> sin_los_repetidos(["feliz", "contento", "alegre", "feliz", "alegre"])
        ['feliz', 'contento', 'alegre']
    """
    return list(set(lista))


from p2.diccionario import Diccionario


def sin_los_repetidos_dic(lista):
    """
    Crea un diccionario con los elementos únicos de una lista como claves y None como valor.

    Args:
        lista (list): Lista con elementos repetidos.

    Returns:
        Diccionario: Diccionario con claves únicas y valores None.

    Example:
        >>> sin_los_repetidos_dic(["feliz", "contento", "feliz"])
        {'feliz': None, 'contento': None}
    """
    return Diccionario(lista, [None] * len(lista))


def contador_apariciones(lista):
    """
    Cuenta las apariciones de cada elemento en una lista.

    Args:
        lista (list): Lista de entrada.

    Returns:
        Diccionario: Diccionario con claves como elementos únicos y valores con la cantidad de veces que aparecen.

    Example:
        >>> contador_apariciones(["a", "b", "a", "c", "b", "a"])
        {'a': 3, 'b': 2, 'c': 1}
    """
    res = Diccionario()

    for elemento in lista:
        if elemento in res:
            res[elemento] = res[elemento] + 1
        else:
            res.insert(elemento, 1)

    return res


def mezclar_diccionarios(dic1: Diccionario, dic2: Diccionario):
    """
    Mezcla dos diccionarios, priorizando los valores del primero si hay claves repetidas.

    Args:
        dic1 (Diccionario): Diccionario base.
        dic2 (Diccionario): Diccionario a mezclar.

    Returns:
        Diccionario: Resultado de la mezcla.

    Example:
        >>> d1 = Diccionario(["a"], [1])
        >>> d2 = Diccionario(["a", "b"], [9, 2])
        >>> mezclar_diccionarios(d1, d2)
        {'a': 1, 'b': 2}
    """
    res = dic1.clone()

    for clave in dic2.keys():
        res.insert(clave, dic2[clave])

    return res


def administrar_materias(alumnos_materias_dic: Diccionario, alumno: str, materia: str):
    """
    Agrega una materia a un alumno solo si no la tiene.

    Args:
        alumnos_materias_dic (Diccionario): Diccionario con alumnos como claves y listas de materias como valores.
        alumno (str): Nombre del alumno.
        materia (str): Materia a registrar.

    Example:
        >>> d = Diccionario()
        >>> administrar_materias(d, "Ana", "Química")
        >>> administrar_materias(d, "Ana", "Matemáticas")
        >>> d
        {'Ana': ['Química', 'Matemáticas']}
    """
    if not contains_value(alumnos_materias_dic, alumno):
        alumnos_materias_dic.insert(alumno, [materia])
    else:
        agregar_si_lista(alumnos_materias_dic[alumno], materia, materia not in alumnos_materias_dic[alumno])


def agregar_si_lista(lista: list, elemento: any, condicion: any):
    """
    Agrega un elemento a una lista si la condición es verdadera.

    Args:
        lista (list): Lista donde agregar.
        elemento (any): Elemento a agregar.
        condicion (bool): Condición que determina si se agrega o no.

    Example:
        >>> l = [1, 2]
        >>> agregar_si_lista(l, 3, True)
        >>> l
        [1, 2, 3]
    """
    if condicion:
        lista.append(elemento)


def contains_value(dic, value):
    """
    Verifica si un valor está presente entre los valores del diccionario.

    Args:
        dic (Diccionario): Diccionario donde buscar.
        value (any): Valor a buscar.

    Returns:
        bool: True si el valor está presente, False en caso contrario.

    Example:
        >>> d = Diccionario(["Juan"], [["Mate"]])
        >>> contains_value(d, ["Mate"])
        True
    """
    return value in dic.values()


from p1.utils.utils_listas import contar


def lista_a_dic(lista):
    """
    Convierte una lista en un diccionario donde cada clave es un elemento
    y su valor es una lista del elemento repetido según la cantidad de veces que aparece.

    Args:
        lista (list): Lista de entrada.

    Returns:
        Diccionario: Diccionario con claves únicas y listas como valores.

    Example:
        >>> lista_a_dic(["a", "b", "a"])
        {'a': ['a', 'a'], 'b': ['b']}
    """
    res = Diccionario()
    for elemento in lista:
        cantidad = contar(lista, lambda x, elem=elemento: x == elem)
        res.insert(elemento, [elemento] * cantidad)

    return res


from p1.utils.utils_listas import reducir


def promedios(materias, notas):
    """
    Calcula el promedio de notas para cada materia.

    Args:
        materias (list): Lista de materias.
        notas (list): Lista de notas correspondientes.

    Returns:
        Diccionario: Diccionario con cada materia y su promedio.

    Example:
        >>> promedios(["Mat", "Mat", "Física"], [8, 6, 10])
        {'Mat': 7.0, 'Física': 10.0}
    """
    dic_materia_notas = Diccionario()
    acumulados_dic = acumular_para_promedio(materias, notas)

    for materia_str in acumulados_dic.keys():
        acumulados_list_int = acumulados_dic[materia_str]
        reductor = lambda v1, v2: v1 / v2
        dic_materia_notas[materia_str] = reducir(acumulados_list_int, reductor)

    return dic_materia_notas


def acumular_para_promedio(lista1, lista2) -> Diccionario:
    """
    Devuelve un diccionario con la suma total y la cantidad por cada clave.

    Args:
        lista1 (list): Claves.
        lista2 (list): Valores asociados.

    Returns:
        Diccionario: Diccionario con listas [suma, cantidad].

    Example:
        >>> acumular_para_promedio(["a", "a", "b"], [2, 4, 3])
        {'a': [6, 2], 'b': [3, 1]}
    """
    acumulados_dic = Diccionario()

    for i, clave in enumerate(lista1):
        valor_actual_int = lista2[i]

        if clave in acumulados_dic:
            acumulados_dic[clave][0] += valor_actual_int
            acumulados_dic[clave][1] += 1
        else:
            acumulados_dic.insert(clave, [valor_actual_int, 1])

    return acumulados_dic


def posibles_pares(dic: Diccionario):
    """
    Genera todos los pares (clave, valor) de un diccionario donde cada valor es una lista.

    Args:
        dic (Diccionario): Diccionario con listas como valores.

    Returns:
        list: Lista de tuplas (clave, valor_individual).

    Example:
        >>> d = Diccionario({1: [2, 3]})
        >>> posibles_pares(d)
        [(1, 2), (1, 3)]
    """
    res = []
    for key_int in dic.keys():
        value_list_int = dic[key_int]

        for value_int in value_list_int:
            res.append((key_int, value_int))

    return res


def list_a_dic(lista_de_tuplas):
    """
    Convierte una lista de tuplas (clave, valor) en un diccionario agrupando los valores por clave.

    Args:
        lista_de_tuplas (list[tuple]): Lista de pares clave-valor.

    Returns:
        Diccionario: Diccionario con claves únicas y listas de valores agrupados.

    Example:
        >>> list_a_dic([(1, 2), (1, 3), (2, 4)])
        {1: [2, 3], 2: [4]}
    """
    res = Diccionario()

    for tupla in lista_de_tuplas:
        v1 = tupla[0]
        v2 = tupla[1]

        if v1 in res.keys():
            res[v1].append(v2)
        else:
            res.insert(v1, [v2])

    return res
