from estructuras.cola import Cola
from estructuras.pila import Pila


# -------------------------------------------------------
# CATEGORÍA: Búsqueda
# -------------------------------------------------------
# buscar(cola, valor) -> valor: Busca un valor en la cola y devuelve el primer elemento que lo cumple.
# contiene(cola, valor) -> bool: Verifica si un valor está presente en la cola.
# filtrar(cola, condicion) -> Cola: Devuelve una nueva cola con los elementos que cumplen una condición.
# obtener_primeros_n_elementos(cola, n) -> list: Devuelve una lista con los primeros n elementos de la cola.
# obtener_ultimos_n_elementos(cola, n) -> list: Devuelve una lista con los últimos n elementos de la cola.

# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------
# mapear(cola, funcion) -> Cola: Aplica una función a cada elemento y devuelve una nueva cola con los resultados.
# reducir(cola, funcion_reduccion, valor_inicial=None): Reduce los elementos de la cola aplicando una función acumuladora.
# invertir(cola): Invierte el orden de los elementos de la cola (modifica la original).
# a_lista(cola) -> list: Convierte la cola en una lista desde el frente hasta el final.

# -------------------------------------------------------
# CATEGORÍA: Movimiento de Elementos
# -------------------------------------------------------
# mover_base_al_final(cola) -> Cola: Devuelve una nueva cola con el primer elemento movido al final.
# mover_final_al_frente(cola) -> Cola: Devuelve una nueva cola con el último elemento movido al frente.

# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------
# eliminar_elemento(cola, valor) -> bool: Elimina la primera aparición del valor indicado (modifica la original).


# -------------------------------------------------------
# CATEGORÍA: Búsqueda
# -------------------------------------------------------

def buscar(cola: Cola, valor):
    """
    Busca un valor en la cola y devuelve el primer elemento que lo cumple.

    Parámetros:
        cola (Cola): La cola original.
        valor: Valor a buscar.

    Retorna:
        El primer elemento que cumple la condición o None si no se encuentra.
    """
    copia = cola.clonar()

    while not copia.esta_vacia():
        actual = copia.desencolar()

        if actual == valor:
            return actual

    return None


def contiene(cola: Cola, valor) -> bool:
    """
    Devuelve True si el valor está en la cola, sin modificarla.

    Parámetros:
        cola (Cola): La cola original.
        valor: Valor a buscar.

    Retorna:
        bool: True si está, False si no.
    """
    copia = cola.clonar()

    while not copia.esta_vacia():
        if copia.desencolar() == valor:
            return True

    return False


def filtrar(cola: Cola, condicion):
    """
    Devuelve una nueva cola con los elementos que cumplen una condición.

    Parámetros:
        cola (Cola): La cola original.
        condicion (func): Función booleana que filtra los elementos. Ej: lambda x: x > 5

    Retorna:
        Cola: Nueva cola con elementos filtrados.
    """
    copia = cola.clonar()
    nueva = Cola()

    while not copia.esta_vacia():
        valor = copia.desencolar()

        if condicion(valor):
            nueva.encolar(valor)

    return nueva


def obtener_ultimos_n_elementos(cola: Cola, n: int):
    """
    Devuelve una lista con los últimos n elementos de la cola sin modificarla.
    Los elementos se obtienen desde el final hacia el frente.
    [1, 2, 3, 4, 5] -> [3, 4, 5]

    Parámetros:
        cola (Cola): La cola original.
        n (int): Cantidad de elementos a obtener.

    Retorna:
        list: Lista con los últimos n elementos.
    """
    if n <= 0:
        return []

    elementos = []
    copia = cola.clonar()

    while not copia.esta_vacia():
        elementos.append(copia.desencolar())

    return elementos[-n:]


def obtener_primeros_n_elementos(cola: Cola, n: int):
    """
    Devuelve una lista con los primeros n elementos de la cola sin modificarla.
    Los elementos se obtienen desde el frente hasta el final.
    [1, 2, 3, 4, 5] -> [1, 2, 3]

    Parámetros:
        cola (Cola): La cola original.
        n (int): Cantidad de elementos a obtener.

    Retorna:
        list: Lista con los primeros n elementos.
    """
    if n <= 0:
        return []

    elementos = []
    copia = cola.clonar()

    while not copia.esta_vacia():
        elementos.append(copia.desencolar())

    return elementos[:n]


# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------

def mapear(cola: Cola, funcion):
    """
    Devuelve una nueva cola con los elementos transformados por una función.

    Parámetros:
        cola (Cola): La cola original.
        funcion (func): Función que transforma cada elemento. Ej: lambda x: x * 2

    Retorna:
        Cola: Nueva cola con los elementos transformados.
    """
    copia = cola.clonar()
    nueva = Cola()

    while not copia.esta_vacia():
        nueva.encolar(funcion(copia.desencolar()))

    return nueva


def reducir(cola: Cola, funcion_reduccion, valor_inicial=None):
    """
    Aplica una función de reducción sobre los elementos de la cola.

    Parámetros:
        cola (Cola): La cola original.
        funcion_reduccion (func): Función que combina dos valores. Ej: lambda acc, x: acc + x.
        valor_inicial (opcional): Valor inicial del acumulador. Por defecto es elemento al frente.

    Retorna:
        Resultado acumulado.

    Lanza:
        Exception: Si la cola está vacía y no se da valor_inicial.
    """
    copia = cola.clonar()
    acumulador = valor_inicial

    if acumulador is None:
        if copia.esta_vacia():
            raise Exception("La cola está vacía y no se proporcionó un valor inicial.")
        acumulador = copia.desencolar()

    while not copia.esta_vacia():
        acumulador = funcion_reduccion(acumulador, copia.desencolar())

    return acumulador


def invertir(cola: Cola):
    """
    Invierte el orden de los elementos de la cola usando solo colas y listas.

    Parámetros:
        cola (Cola): La cola a invertir.

    Retorna: Una nueva cola invertida, sin modificar la original.
    """
    copia = cola.clonar()
    pila = Pila()

    while not copia.esta_vacia():
        pila.apilar(copia.desencolar())

    while not pila.esta_vacia():
        copia.encolar(pila.desapilar())

    return copia


def a_lista(cola: Cola):
    """
    Devuelve una lista con todos los elementos de la cola sin modificarla.

    Parámetros:
        cola (Cola): La cola original.

    Retorna:
        list: Lista con los elementos de la cola.
    """
    copia = cola.clonar()
    lista = []

    while not copia.esta_vacia():
        lista.append(copia.desencolar())

    return lista


# -------------------------------------------------------
# CATEGORÍA: Movimiento de Elementos
# -------------------------------------------------------

def mover_primero_al_ultimo(cola: Cola) -> Cola:
    """
    Devuelve una nueva cola con el primer elemento movido al final.

    Parámetros:
        cola (Cola): La cola original.

    Retorna:
        Cola: Nueva cola con el primer elemento al final.
    """
    copia = cola.clonar()

    if copia.esta_vacia():
        return copia

    primero = copia.desencolar()
    copia.encolar(primero)

    return copia


def mover_ultimo_al_primero(cola: Cola) -> Cola:
    """
    Devuelve una nueva cola con el último elemento movido al frente.

    Parámetros:
        cola (Cola): La cola original.

    Retorna:
        Cola: Nueva cola con el último elemento al frente.
    """
    copia = cola.clonar()
    elementos = []

    if copia.esta_vacia():
        return copia

    while not copia.esta_vacia():
        elementos.append(copia.desencolar())

    copia.encolar(elementos.pop())

    for e in elementos:
        copia.encolar(e)

    return copia


# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------

def eliminar_elemento(cola: Cola, valor):
    """
    Elimina la primera aparición del valor en la cola. Modifica la cola original.

    Parámetros:
        cola (Cola): La cola a modificar.
        valor: Valor a eliminar.

    Retorna:
        bool: True si se eliminó, False si no estaba.
    """
    copia = Cola()
    eliminado = False

    while not cola.esta_vacia():
        actual = cola.desencolar()

        if not eliminado and actual == valor:
            eliminado = True
            continue

        copia.encolar(actual)

    # Devolvemos los elementos a la cola original
    while not copia.esta_vacia():
        cola.encolar(copia.desencolar())

    return eliminado
