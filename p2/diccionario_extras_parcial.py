# -------------------------------------------------------
# CATEGORÍA: Diccionarios (Ejercicios propios)
# -------------------------------------------------------

# juntarPorValores(dic) -> Diccionario:
#   Agrupa las claves de un diccionario original según su valor,
#   generando un nuevo diccionario donde los valores pasan a ser claves
#   y se acumulan las claves originales en listas.

# promedios(materias, notas) -> Diccionario:
#   Calcula el promedio entero de cada materia a partir de dos listas paralelas
#   (materias y notas) y devuelve un diccionario materia → promedio.

# interseccion(dic1, dic2) -> Diccionario:
#   Devuelve un diccionario con las claves que aparecen en ambos diccionarios
#   y como valor una tupla con los valores respectivos de cada uno.

# maximoPorNumero(pares) -> Diccionario:
#   Recibe una lista de pares (x, y) y devuelve un diccionario que asocia a cada x
#   el mayor y con el que aparece.

# palabrasPorTamaño(palabras) -> Diccionario:
#   Agrupa las palabras de una lista según su longitud, devolviendo un diccionario
#   con clave igual a la longitud y valor la lista de palabras.

# maximoPorClave(dic) -> None:
#   Modifica el diccionario in-place reemplazando cada lista de enteros asociada
#   a una clave por su máximo valor.

# cantidadAntonimos(dic) -> int:
#   Devuelve la cantidad de pares de claves con valores opuestos en el diccionario.
#   Cada par se cuenta una sola vez.

# traduccion(lista_morse, significado, mensaje) -> list[str]:
#   Traduce un mensaje codificado en Morse a caracteres usando un diccionario creado
#   a partir de las claves y significados proporcionados.


# -------------  Ejercicio 1  -----------------------------------------------
from p2.diccionario import Diccionario


def juntarPorValores(dic: Diccionario) -> Diccionario:
    """
    Agrupa las claves del diccionario según su valor.

    Args:
        dic (Diccionario): Diccionario donde las claves son strings y los valores enteros.

    Returns:
        Diccionario: Nuevo diccionario donde cada valor original es clave y el valor es la lista de claves asociadas.

    Example:
        >>> dic = Diccionario({"a": 1, "b": 2, "c": 1})
        >>> juntarPorValores(dic)
        {1: ["a", "c"], 2: ["b"]}
    """
    res = Diccionario()

    for clave in dic.keys():
        valor = dic[clave]  # significado de la clave
        if valor in res:  # ¿ya existe la lista?
            lista = res[valor]  # obtenemos la lista
            lista.append(clave)  # agregamos la clave actual
        else:  # primer aparición de ese valor
            res[valor] = [clave]  # creamos la nueva lista

    return res


# -------------  Ejercicio 2  -----------------------------------------------
def promedios(materias: list, notas: list) -> Diccionario:
    """
    Calcula el promedio entero de notas por materia.

    Args:
        materias (list): Lista de nombres de materias.
        notas (list): Lista de enteros con las notas correspondientes.

    Returns:
        Diccionario: Diccionario con cada materia como clave y su promedio entero como valor.

    Raises:
        ValueError: Si las listas no tienen el mismo largo.

    Example:
        >>> promedios(["Mat", "Física", "Mat"], [8, 7, 6])
        {"Mat": 7, "Física": 7}
    """

    if len(materias) != len(notas):
        raise ValueError("Ambas listas deben tener el mismo tamaño")

    # Diccionario temporal: materia → [suma, cantidad]
    acumulados = Diccionario()

    for i in range(len(materias)):
        mat = materias[i]
        nota = notas[i]

        if mat in acumulados:
            datos = acumulados[mat]  # [suma, cantidad]
            datos[0] += nota
            datos[1] += 1
        else:
            acumulados[mat] = [nota, 1]

    # Diccionario final con los promedios
    promedios_dic = Diccionario()
    for mat in acumulados.keys():
        suma, cant = acumulados[mat]
        promedios_dic[mat] = suma // cant

    return promedios_dic


# -------------  Ejercicio 3  -----------------------------------------------
def interseccion(dic1: Diccionario, dic2: Diccionario) -> Diccionario:
    """
    Retorna un nuevo diccionario con las claves comunes entre dic1 y dic2.
    El valor asociado es una tupla con los valores de cada uno.

    Args:
        dic1 (Diccionario): Primer diccionario.
        dic2 (Diccionario): Segundo diccionario.

    Returns:
        Diccionario: Diccionario con claves comunes y valores como tuplas.

    Example:
        >>> interseccion(Diccionario({"a": 1, "b": 2}), Diccionario({"b": 3, "c": 4}))
        {"b": (2, 3)}
    """
    inter = Diccionario()
    for clave in dic1.keys():
        if clave in dic2:
            inter[clave] = (dic1[clave], dic2[clave])
    return inter


# -------------  Ejercicio 4  -----------------------------------------------
def maximoPorNumero(pares: list) -> Diccionario:
    """
    Dada una lista de pares (x, y), guarda el mayor valor de y observado para cada x.

    Args:
        pares (list[tuple[int, int]]): Lista de tuplas con claves y valores.

    Returns:
        Diccionario: Diccionario con x como clave y el mayor y como valor.

    Example:
        >>> maximoPorNumero([(1, 5), (2, 3), (1, 8)])
        {1: 8, 2: 3}
    """
    res = Diccionario()

    for x, y in pares:
        if x in res:
            if y > res[x]:
                res[x] = y
        else:
            res[x] = y
    return res


# -------------  Ejercicio 5  -----------------------------------------------
def palabrasPorTamaño(palabras: list) -> Diccionario:
    """
    Agrupa palabras por su longitud.

    Args:
        palabras (list): Lista de strings.

    Returns:
        Diccionario: Diccionario donde la clave es la longitud y el valor una lista de palabras de esa longitud.

    Example:
        >>> palabrasPorTamaño(["hola", "adiós", "a", "sol"])
        {4: ["hola", "sol"], 5: ["adiós"], 1: ["a"]}
    """
    res = Diccionario()
    for palabra in palabras:
        tam = len(palabra)
        if tam in res:
            res[tam].append(palabra)
        else:
            res[tam] = [palabra]
    return res


# -------------  Ejercicio 6  -----------------------------------------------
def maximoPorClave(dic: Diccionario) -> None:
    """
    Reemplaza, para cada clave del diccionario, su lista de enteros por el mayor de ellos.

    La operación es in-place.

    Args:
        dic (Diccionario): Diccionario con listas de enteros como valores.

    Example:
        >>> d = Diccionario({"a": [1, 3, 2], "b": [5]})
        >>> maximoPorClave(d)
        >>> d
        {"a": 3, "b": 5}
    """
    for clave in dic.keys():
        lista_valores = dic[clave]
        dic[clave] = max(lista_valores)


def cantidadAntonimos(dic: Diccionario) -> int:
    """
    Devuelve la cantidad de pares de claves con valores opuestos en el diccionario.

    Se considera que dos claves forman un par antónimo si sus valores son opuestos
    (v y -v). Cada par se cuenta solo una vez. No se usan estructuras auxiliares.

    Args:
        dic (Diccionario): Diccionario con claves de cualquier tipo y valores enteros.

    Returns:
        int: Número de pares antónimos detectados.

    Example:
        >>> d = Diccionario(
        ...     ["casa", "perro", "auto", "gato", "remera", "botella"],
        ...     [1,       4,      -1,     5,      8,        -4]
        ... )
        >>> cantidadAntonimos(d)
        2
    """
    pares = 0
    for clave in dic.keys():
        valor = dic[clave]
        if valor > 0:
            for otra in dic.keys():
                if dic[otra] == -valor:
                    pares += 1
                    break
    return pares


def traduccion(lista_morse: list, significado: list, mensaje: list) -> list:
    """
    Traduce un mensaje en código Morse usando listas de claves y significados.

    Crea un diccionario que relaciona códigos Morse con letras y
    devuelve una lista con los caracteres traducidos del mensaje original.

    Args:
        lista_morse (list[str]): Lista con códigos Morse como strings de 3 bits.
        significado (list[str]): Letras o caracteres asociados a cada código.
        mensaje (list[str]): Lista de códigos Morse a traducir.

    Returns:
        list[str]: Lista con caracteres traducidos en el orden del mensaje.

    Example:
        >>> claves = ['000', '001', '010', '100', '011', '110', '111']
        >>> valores = ['k', 'r', 'c', 'd', 'e', 'o', ' ']
        >>> mensaje = ['011', '100', '111', '001', '110', '010', '000']
        >>> traduccion(claves, valores, mensaje)
        ['e', 'd', ' ', 'r', 'o', 'c', 'k']
    """
    morse_dic = Diccionario(lista_morse, significado)
    salida = []
    for codigo in mensaje:
        salida.append(morse_dic[codigo])
    return salida
