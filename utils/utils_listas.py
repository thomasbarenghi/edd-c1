from functools import reduce


# -------------------------------------------------------
# CATEGORÍA: Búsqueda y validación
# -------------------------------------------------------
# buscar(lista, condicion) -> elemento
# todos(lista, condicion) -> bool
# alguno(lista, condicion) -> bool
# filtrar(lista, condicion) -> lista
# contar(lista, condicion) -> int

# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------
# transformar(lista, funcion) -> lista
# aplanar(lista_de_listas) -> lista
# unicos(lista) -> lista
# reducir(lista, funcion, valor_inicial=None) -> valor
# dividir_por(lista, valor) -> lista
# rotar(lista, n) -> lista
# ordenar_por(lista, clave, descendente=False) -> lista
# invertir(arr) -> lista
# desde_hasta(arr, desde, hasta) -> lista
# inicio_fin_paso(arr, inicio, fin, paso) -> lista

# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------
# sin_el_ultimo(arr) -> lista
# sin_el_primero(arr) -> lista


# -------------------------------------------------------
# CATEGORÍA: Búsqueda y validación
# -------------------------------------------------------

def buscar(lista, condicion):
    """
    Devuelve el primer elemento de la lista que cumple con la condición. Si no hay ninguno, devuelve None.

    Parámetros:
    - lista: lista de elementos.
    - condicion: función que recibe un elemento y devuelve True si coincide.

    Ejemplo:
    buscar(["hola", "chau", "hola"], lambda x: x == "chau")  # "chau"
    """
    for x in lista:
        if condicion(x):
            return x

    return None


def todos(lista, condicion):
    """
    Verifica si todos los elementos de la lista cumplen con una condición.

    Parámetros:
    - lista: lista de elementos.
    - condicion: función que devuelve True o False por cada elemento.

    Ejemplo:
    todos([2, 4, 6], lambda x: x % 2 == 0)  # True
    """
    return all(condicion(x) for x in lista)


def alguno(lista, condicion):
    """
    Verifica si al menos un elemento de la lista cumple con la condición.

    Parámetros:
    - lista: lista de elementos.
    - condicion: función que devuelve True o False por cada elemento.

    Ejemplo:
    alguno([1, 3, 4], lambda x: x % 2 == 0)  # True
    """
    return any(condicion(x) for x in lista)


def filtrar(lista, condicion):
    """
    Devuelve una nueva lista con los elementos que cumplen la condición dada.

    Parámetros:
    - lista: lista de elementos.
    - condicion: función que recibe un elemento y devuelve True si debe incluirse.

    Ejemplo:
    filtrar([1, 2, 3, 4], lambda x: x % 2 == 0) # [2, 4]
    """
    return [x for x in lista if condicion(x)]


def contar(lista, condicion):
    """
    Cuenta cuántos elementos de la lista cumplen con una condición.

    Parámetros:
    - lista: lista de elementos.
    - condicion: función que devuelve True si el elemento debe contarse.

    Ejemplo:
    contar([1, 2, 3, 4], lambda x: x % 2 == 0)  # 2
    """
    return sum(1 for x in lista if condicion(x))


# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------

def transformar(lista, funcion):
    """
    Aplica una función a cada elemento de la lista y devuelve una nueva lista con los resultados.

    Parámetros:
    - lista: lista de elementos.
    - funcion: función que transforma cada elemento.

    Ejemplo:
    transformar([1, 2, 3], lambda x: x * 2)  # [2, 4, 6]
    """
    return [funcion(x) for x in lista]


def aplanar(lista_de_listas):
    """
    Convierte una lista de listas en una sola lista aplanada.

    Parámetros:
    - lista_de_listas: lista que contiene otras listas como elementos.

    Ejemplo:
    aplanar([[1, 2], [3, 4]])  # [1, 2, 3, 4]
    """
    return [x for sublista in lista_de_listas for x in sublista]


def unicos(lista):
    """
    Elimina los elementos duplicados de la lista, manteniendo el orden de aparición.

    Parámetros:
    - lista: lista de elementos.

    Ejemplo:
    únicos([1, 2, 2, 3, 1])  # [1, 2, 3]
    """
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)
    return resultado


def reducir(lista, funcion, valor_inicial=None):
    """
    Reduce una lista aplicando una función acumulativa, como lo hace `reduce`.

    Parámetros:
    - lista: lista de elementos a reducir.
    - funcion: función que toma dos argumentos (acumulador, elemento).
    - valor_inicial (opcional): valor inicial del acumulador.

    Ejemplo:
    reducir([1, 2, 3], lambda acc, x: acc + x, 0)  # 6
    """
    return reduce(funcion, lista, valor_inicial) if valor_inicial is not None else reduce(funcion, lista)


def dividir_por(lista, valor):
    """
    Devuelve una nueva lista con cada elemento dividido por un valor dado.

    Parámetros:
    - lista: lista de números.
    - valor: divisor. Si es cero, se lanza un error.

    Ejemplo:
    dividir_por([10, 20], 10)  # [1.0, 2.0]
    """
    if valor == 0:
        raise ValueError("No se puede dividir por cero")
    return [x / valor for x in lista]


def rotar(lista, n):
    """
    Rota los elementos de una lista n posiciones a la derecha. Si n es negativo, rota a la izquierda.

    Parámetros:
    - lista: lista de elementos.
    - n: número de posiciones a rotar.

    Ejemplo:
    rotar([1, 2, 3, 4], 1) # [4, 1, 2, 3]
    """
    n = n % len(lista)
    return lista[-n:] + lista[:-n]


def ordenar_por(lista, clave, descendente=False):
    """
    Ordena una lista de elementos (como diccionarios o tuplas) usando una función clave.
    Se puede especificar si el orden debe ser descendente.

    Parámetros:
    - lista: lista de elementos.
    - clave: función que devuelve el valor por el cual ordenar cada elemento.
    - descendente (bool): si es True, ordena de mayor a menor. Por defecto es False (ascendente).

    Ejemplo:
    ordenar_por([{'nombre': 'Pedro'}, {'nombre': 'Ana'}], lambda x: x['nombre'])
    # [{'nombre': 'Ana'}, {'nombre': 'Pedro'}]

    ordenar_por([{'nombre': 'Pedro'}, {'nombre': 'Ana'}], lambda x: x['nombre'], descendente=True)
    # [{'nombre': 'Pedro'}, {'nombre': 'Ana'}]
    """
    return sorted(lista, key=clave, reverse=descendente)


def invertir(arr):
    """
    Devuelve la lista con los elementos en orden inverso.

    Parámetros:
    - arr: lista de elementos.

    Ejemplo:
    invertir([1, 2, 3]) # [3, 2, 1]
    """
    return arr[::-1]


def desde_hasta(arr, desde, hasta):
    """
    Devuelve una sublista desde el índice 'desde' hasta el índice 'hasta' (sin incluirlo).

    Parámetros:
    - arr: lista de elementos.
    - desde: índice inicial (incluido).
    - hasta: índice final (no incluido).

    Ejemplo:
    desde_hasta([1, 2, 3, 4], 1, 3) # [2, 3]
    """
    return arr[desde:hasta]


def inicio_fin_paso(arr, inicio, fin, paso):
    """
    Devuelve una sublista desde el índice 'inicio' hasta el índice 'fin' (sin incluirlo) con un paso dado.

    Parámetros:
    - arr: lista de elementos.
    - inicio: índice inicial (incluido).
    - fin: índice final (no incluido).
    - paso: tamaño del paso.

    arr = [10, 20, 30, 40, 50, 60]

    arr[::2]    # → [10, 30, 50]
    arr[1::2]   # → [20, 40, 60]
    arr[::-1]   # → [60, 50, 40, 30, 20, 10]

    Ejemplo:
    inicio_fin_paso([1, 2, 3, 4], 0, 4, 2) # [1, 3]
    """
    return arr[inicio:fin:paso]


# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------

def sin_el_ultimo(arr):
    """
    Devuelve la lista sin el último elemento.

    Parámetros:
    - arr: lista de elementos.

    Ejemplo:
    sin_el_ultimo([1, 2, 3]) # [1, 2]
    """
    return arr[:-1]


def sin_el_primero(arr):
    """
    Devuelve la lista sin el primer elemento.

    Parámetros:
    - arr: lista de elementos.

    Ejemplo:
    sin_el_primero([1, 2, 3]) # [2, 3]
    """
    return arr[1:]
