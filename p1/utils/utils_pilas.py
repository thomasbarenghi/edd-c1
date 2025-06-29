from estructuras.pila import Pila


# -------------------------------------------------------
# CATEGORÍA: Búsqueda
# -------------------------------------------------------
# buscar(pila, condicion) -> valor: Busca el primer elemento que cumpla con la condición proporcionada.
# contiene(pila, valor) -> bool: Verifica si un valor está presente en la pila.
# filtrar(pila, condicion) -> Pila: Devuelve una nueva pila con los elementos que cumplen una condición.
# obtener_n_elementos(pila, n) -> list: Devuelve una lista con los primeros n elementos desde la cima.

# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------
# mapear(pila, funcion) -> Pila: Aplica una función a cada elemento y devuelve una nueva pila con los resultados.
# reducir(pila, funcion_reduccion, valor_inicial=None): Reduce los elementos de la pila aplicando una función acumuladora.
# invertir(pila) -> Pila: Devuelve una nueva pila con los elementos en orden inverso.
# a_lista(pila) -> list: Convierte la pila en una lista desde la cima hasta la base.

# -------------------------------------------------------
# CATEGORÍA: Movimiento de Elementos
# -------------------------------------------------------
# mover_base_a_cima(pila) -> Pila: Devuelve una nueva pila con la base movida a la cima.
# mover_cima_a_base(pila) -> Pila: Devuelve una nueva pila con la cima movida a la base.

# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------
# eliminar_base(pila) -> Pila: Devuelve una nueva pila sin el elemento de la base.
# eliminar_elemento(pila, valor) -> bool: Elimina la primera aparición del valor indicado, empezando desde la cima.

# -------------------------------------------------------
# CATEGORÍA: Inserción
# -------------------------------------------------------
# insertar_ordenado(pila, elemento, clave=lambda x: x): Inserta un elemento en la pila en la posición ordenada según una clave.

# -------------------------------------------------------
# CATEGORÍA: Búsqueda
# -------------------------------------------------------

def buscar(pila: Pila, condicion) -> any:
    """
    Busca el primer elemento que cumpla con la condición proporcionada.

    Parámetros:
    - pila: Pila a analizar.
    - condicion: Función que recibe un valor y devuelve True o False. Ejemplos: lambda x: x > 5, lambda x: x == "a".

    Retorna:
    - El primer elemento que cumple la condición o None si no se encuentra.

    Nota:
    - No modifica la pila original.
    """
    copia = pila.clonar()

    while not copia.esta_vacia():
        valor = copia.desapilar()

        if condicion(valor):
            return valor

    return None


def contiene(pila: Pila, valor) -> bool:
    """
    Verifica si un valor está presente en la pila.

    Parámetros:
    - pila: Pila en la que se busca el valor.
    - valor: Elemento a buscar.

    Retorna:
    - True si el valor está en la pila, False en caso contrario.

    Nota:
    - No modifica la pila original.
    """
    copia = pila.clonar()

    while not copia.esta_vacia():
        if copia.desapilar() == valor:
            return True

    return False


def filtrar(pila: Pila, condicion) -> Pila:
    """
    Devuelve una nueva pila que contiene solo los elementos de la pila original
    que cumplen con la condición dada.

    Parámetros:
    - pila: Pila original a filtrar.
    - condicion: Función que recibe un valor y devuelve True o False. Ejemplos: lambda x: x > 5, lambda x: x == "a".

    Retorna:
    - Pila con los elementos que cumplen la condición, en el mismo orden que estaban en la pila original.
    """
    # Clonamos la pila original para no modificar la original
    copia = pila.clonar()

    # Lista auxiliar para mantener los elementos que cumplen la condición
    elementos_filtrados = []

    # Desapilamos y verificamos la condición para cada elemento
    while not copia.esta_vacia():
        valor = copia.desapilar()

        if condicion(valor):
            elementos_filtrados.append(valor)

    # Para mantener el orden original, apilamos en orden inverso
    for elemento in reversed(elementos_filtrados):
        copia.apilar(elemento)

    return copia


def obtener_primeros_n_elementos(pila: Pila, n: int) -> list:
    """
    Devuelve una lista con los primeros n elementos desde la cima.
    [1,2,3,4,5] -> [3,4,5]

    Parámetros:
    - pila: Pila de la cual extraer elementos.
    - n: Cantidad de elementos a obtener.

    Retorna:
    - Lista con los primeros n elementos o menos si la pila tiene menos.

    Nota:
    - No modifica la pila original.
    - Los elementos se devuelven en el mismo orden que están en la pila.
    """
    copia = pila.clonar()  # Clonamos la pila para no modificar la original
    elementos = []

    while not copia.esta_vacia() and len(elementos) < n:
        elementos.append(copia.desapilar())  # Extraemos los elementos de la pila clonada

    # Invertimos los elementos para que se devuelvan en el orden original
    return elementos[::-1]


def obtener_ultimos_n_elementos(pila: Pila, n: int) -> list:
    """
    Devuelve una lista con los últimos n elementos desde la base.
    [1,2,3,4,5] -> [1,2,3]

    Parámetros:
    - pila: Pila de la cual extraer elementos.
    - n: Cantidad de elementos a obtener.

    Retorna:
    - Lista con los últimos n elementos o menos si la pila tiene menos.

    Nota:
    - No modifica la pila original.
    - Los elementos se devuelven en el mismo orden que están en la pila.
    """
    copia = pila.clonar()  # Clonamos la pila para no modificar la original
    elementos = []

    while not copia.esta_vacia():
        elementos.append(copia.desapilar())

    return elementos[-n:][::-1]  # Devolvemos los últimos n elementos en el orden original


# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------

def mapear(pila: Pila, funcion) -> Pila:
    """
     Aplica una función a cada elemento y devuelve una nueva pila con los resultados.

     Parámetros:
     - pila: Pila original.
     - funcion: Función a aplicar a cada elemento. Ejemplo: lambda x: x * 2, lambda x: x + 1.

     Retorna:
     - Nueva pila con los elementos transformados.

     Nota:
     - La posición de los elementos se conserva.
     """
    copia = pila.clonar()
    temporal = []

    while not copia.esta_vacia():
        temporal.append(funcion(copia.desapilar()))

    nueva = Pila()

    for elemento in temporal:
        nueva.apilar(elemento)

    return nueva


def reducir(pila: Pila, funcion_reduccion, valor_inicial=None):
    """
    Reduce los elementos de la pila aplicando una función acumuladora.

    Parámetros:
    - pila: Pila a reducir.
    - funcion_reduccion: Función que recibe dos argumentos y devuelve uno. Ejemplo: lambda x, y: x + y, lambda x, y: x * y.
    - valor_inicial: Valor inicial opcional.

    Retorna:
    - Resultado de la reducción.

    Excepciones:
    - Lanza excepción si la pila está vacía y no se proporciona valor inicial.
    """
    copia = pila.clonar()

    if copia.esta_vacia() and valor_inicial is None:
        raise Exception("La pila está vacía y no se proporcionó valor inicial.")

    acumulador = valor_inicial

    if acumulador is None:
        acumulador = copia.desapilar()

    while not copia.esta_vacia():
        acumulador = funcion_reduccion(acumulador, copia.desapilar())

    return acumulador


def invertir(pila: Pila) -> Pila:
    """
    Devuelve una nueva pila con los elementos en orden inverso.

    Parámetros:
    - pila: Pila original.

    Retorna:
    - Nueva pila con los elementos invertidos.

    Nota:
    - No modifica la pila original.
    """
    copia = pila.clonar()
    invertida = Pila()

    # Extraemos los elementos de la pila clonada y los agregamos en el orden inverso
    for elem in copia.a_lista()[::-1]:  # Recorremos la lista clonada en orden inverso
        invertida.apilar(elem)

    return invertida


def a_lista(pila: Pila) -> list:
    """
    Convierte la pila en una lista desde la cima hasta la base.

    Parámetros:
    - pila: Pila a convertir.

    Retorna:
    - Lista de elementos, con el primero siendo la cima.

    Nota:
    - No modifica la pila original.
    """
    copia = pila.clonar()
    elementos = []

    while not copia.esta_vacia():
        elementos.append(copia.desapilar())

    return elementos[::-1]


# -------------------------------------------------------
# CATEGORÍA: Movimiento de Elementos
# -------------------------------------------------------

def mover_base_a_cima(pila: Pila) -> Pila:
    """
    Devuelve una nueva pila con la base movida a la cima.

    Parámetros:
    - pila: Pila original.

    Retorna:
    - Nueva pila con la base en la cima.

    Nota:
    - No modifica la pila original.
    """
    # [1,2,3] -> [2,3,1]
    if pila.esta_vacia() or pila.tamaño() == 1:
        return pila.clonar()

    original = pila.clonar()
    aux = Pila()

    # Desapilamos todos menos el de la base
    while original.tamaño() > 1:
        aux.apilar(original.desapilar())

    base = original.desapilar()  # Guardamos la base

    # Restauramos los elementos en orden original
    nueva = Pila()
    while not aux.esta_vacia():
        nueva.apilar(aux.desapilar())

    nueva.apilar(base)  # La base va a la cima

    return nueva


def mover_cima_a_base(pila: Pila) -> Pila:
    """
    Devuelve una nueva pila con la cima movida a la base.

    Esta operación no modifica la pila original.

    Parámetros:
    - pila: Pila original.

    Retorna:
    - Nueva pila con la cima en la base.

    Nota:
    - No modifica la pila original.
    """
    if pila.esta_vacia() or pila.tamaño() == 1:
        return pila.clonar()

    original = pila.clonar()
    cima = original.desapilar()  # Sacamos la cima

    aux = Pila()
    while not original.esta_vacia():
        aux.apilar(original.desapilar())  # Invertimos el resto

    nueva = Pila()
    nueva.apilar(cima)  # Agregamos la cima como base

    while not aux.esta_vacia():
        nueva.apilar(aux.desapilar())  # Restauramos el orden

    return nueva


# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------

def eliminar_elemento(pila: Pila, valor) -> bool:
    """
    Elimina la primera aparición del valor indicado, empezando desde la cima.

    Parámetros:
    - pila: Pila original (es modificada).
    - valor: Elemento a eliminar.

    Retorna:
    - True si el valor fue encontrado y eliminado, False si no estaba.

    Nota:
    - Modifica la pila original.
    """
    auxiliar = Pila()
    encontrado = False

    # Desapilamos elementos hasta encontrar el valor o vaciar la pila.
    while not pila.esta_vacia():
        actual = pila.desapilar()
        if actual == valor and not encontrado:
            encontrado = True
            continue  # Saltamos este valor sin apilarlo en la pila auxiliar
        auxiliar.apilar(actual)

    # Vaciamos la pila auxiliar de vuelta a la pila original.
    while not auxiliar.esta_vacia():
        pila.apilar(auxiliar.desapilar())

    return encontrado


def eliminar_base(pila: Pila) -> Pila:
    """
    Devuelve una nueva pila sin el elemento de la base.

    Parámetros:
    - pila: Pila original.

    Retorna:
    - Nueva pila sin el último elemento.
    """
    # Clonar la pila para no modificar la original
    copia = pila.clonar()

    # Extraer todos los elementos en una lista (el orden se invierte)
    elementos = []
    while not copia.esta_vacia():
        elementos.append(copia.desapilar())

    # La base es el último elemento en la lista
    if elementos:
        elementos.pop()  # Eliminar la base

    # Reconstruir la pila en orden original
    nueva_pila = Pila()
    for e in reversed(elementos):
        nueva_pila.apilar(e)

    return nueva_pila


# -------------------------------------------------------
# CATEGORÍA: Inserción
# -------------------------------------------------------

def insertar_ordenado(pila, elemento, clave=lambda x: x):
    """
    Inserta un elemento en la pila en la posición ordenada según una clave.

    Parámetros:
    - pila: Pila original (modificada).
    - elemento: Elemento a insertar.
    - clave: Función que determina el criterio de orden (por defecto, el valor mismo). Ejemplo lambda x: x.

    Retorna:
    - None (modifica la pila original).
    """
    aux = Pila()

    # Desapilamos elementos hasta encontrar la posición correcta para el elemento
    while not pila.esta_vacia() and clave(pila.cima()) > clave(elemento):
        aux.apilar(pila.desapilar())

    # Insertamos el nuevo elemento
    pila.apilar(elemento)

    # Vaciamos la pila auxiliar, devolviendo los elementos a la pila original
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
