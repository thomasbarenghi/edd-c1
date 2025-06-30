from p2.lista import Lista


def iterar_lista(lista: Lista):
    """
    Generador que itera sobre todos los elementos de la lista sin acceso a nodos privados.

    Args:
        lista (Lista): La lista a iterar.

    Yields:
        any: Cada elemento de la lista en orden.
    """
    for i in range(lista.tamaño()):
        yield lista.obtener(i)


def buscar(lista: Lista, condicion) -> any:
    """
    Busca el primer elemento en la lista que cumple con una condición dada.

    Args:
        lista (Lista): La lista en la cual se realizará la búsqueda.
        condicion (callable): Función que recibe un elemento y retorna True si cumple la condición.
            Ejemplo: lambda x: x > 5

    Returns:
        any: El primer elemento que cumple la condición. Si no existe ninguno, retorna None.

    Ejemplo:
        >>> buscar(lista, lambda x: x % 2 == 0)
        4
    """
    for dato in iterar_lista(lista):
        if condicion(dato):
            return dato
    return None


def todos(lista: Lista, condicion) -> bool:
    """
    Verifica si todos los elementos de la lista cumplen una condición.

    Args:
        lista (Lista): La lista a evaluar.
        condicion (callable): Función que recibe un elemento y retorna True si cumple la condición.
            Ejemplo: lambda x: x > 0

    Returns:
        bool: True si todos cumplen la condición, False en caso contrario.

    Ejemplo:
        >>> todos(lista, lambda x: x < 10)
        True
    """
    for dato in iterar_lista(lista):
        if not condicion(dato):
            return False
    return True


def alguno(lista: Lista, condicion) -> bool:
    """
    Verifica si al menos un elemento de la lista cumple una condición.

    Args:
        lista (Lista): La lista a evaluar.
        condicion (callable): Función que recibe un elemento y retorna True si cumple la condición.
            Ejemplo: lambda x: x == 3

    Returns:
        bool: True si al menos un elemento cumple la condición, False en caso contrario.

    Ejemplo:
        >>> alguno(lista, lambda x: x == 5)
        True
    """
    for dato in iterar_lista(lista):
        if condicion(dato):
            return True
    return False


def filtrar(lista: Lista, condicion) -> Lista:
    """
    Filtra los elementos de la lista que cumplen con una condición y retorna una nueva lista.

    Args:
        lista (Lista): La lista a filtrar.
        condicion (callable): Función que recibe un elemento y retorna True si debe incluirse.
            Ejemplo: lambda x: x % 2 == 0

    Returns:
        Lista: Nueva lista con los elementos que cumplen la condición.

    Ejemplo:
        >>> filtrar(lista, lambda x: x > 10)
        Lista con elementos mayores a 10
    """
    resultado = Lista()
    for dato in iterar_lista(lista):
        if condicion(dato):
            resultado.agregarAlFinal(dato)
    return resultado


def contar(lista: Lista, condicion) -> int:
    """
    Cuenta cuántos elementos de la lista cumplen con una condición dada.

    Args:
        lista (Lista): La lista a evaluar.
        condicion (callable): Función que recibe un elemento y retorna True si cumple la condición.
            Ejemplo: lambda x: x != 0

    Returns:
        int: Cantidad de elementos que cumplen la condición.

    Ejemplo:
        >>> contar(lista, lambda x: x > 5)
        3
    """
    contador = 0
    for dato in iterar_lista(lista):
        if condicion(dato):
            contador += 1
    return contador


def contiene(lista: Lista, valor: any) -> bool:
    """
    Verifica si la lista contiene un valor dado.

    Args:
        lista (Lista): La lista a evaluar.
        valor (any): Valor a buscar en la lista.

    Returns:
        bool: True si el valor está en la lista, False en caso contrario.

    Ejemplo:
        >>> contiene(lista, 7)
        True
    """
    return alguno(lista, lambda x: x == valor)


def obtener_n_elementos(lista: Lista, n: int) -> list:
    """
    Obtiene los primeros n elementos de la lista como una lista de Python.

    Args:
        lista (Lista): La lista original.
        n (int): Cantidad de elementos a obtener.

    Returns:
        list: Lista con los primeros n elementos (o todos si n es mayor que el tamaño).

    Ejemplo:
        >>> obtener_n_elementos(lista, 3)
        [1, 2, 3]
    """
    resultado = []
    for i in range(min(n, lista.tamaño())):
        resultado.append(lista.obtener(i))
    return resultado


def transformar(lista: Lista, funcion) -> Lista:
    """
    Aplica una función a cada elemento de la lista y retorna una nueva lista con los resultados.

    Args:
        lista (Lista): La lista a transformar.
        funcion (callable): Función que recibe un elemento y retorna el elemento transformado.
            Ejemplo: lambda x: x * 2

    Returns:
        Lista: Nueva lista con los elementos transformados.

    Ejemplo:
        >>> transformar(lista, lambda x: x + 1)
        Lista con cada elemento incrementado en 1
    """
    resultado = Lista()
    for dato in iterar_lista(lista):
        resultado.agregarAlFinal(funcion(dato))
    return resultado


def unicos(lista: Lista) -> Lista:
    """
    Retorna una nueva lista con los elementos únicos de la lista original, preservando el orden.

    Args:
        lista (Lista): La lista original.

    Returns:
        Lista: Nueva lista con elementos únicos.

    Ejemplo:
        >>> unicos(lista)
        Lista sin elementos repetidos
    """
    resultado = Lista()
    vistos = set()
    for dato in iterar_lista(lista):
        if dato not in vistos:
            vistos.add(dato)
            resultado.agregarAlFinal(dato)
    return resultado


def reducir(lista: Lista, funcion, valor_inicial=None) -> any:
    """
    Reduce los elementos de la lista a un solo valor usando una función binaria acumulativa.

    Args:
        lista (Lista): La lista a reducir.
        funcion (callable): Función que recibe dos argumentos (acumulador, elemento) y retorna el nuevo acumulador.
            Ejemplo: lambda acc, x: acc + x
        valor_inicial (any, optional): Valor inicial del acumulador. Si es None, se usa el primer elemento.

    Returns:
        any: Resultado de la reducción.

    Raises:
        TypeError: Si la lista está vacía y no se proporciona valor_inicial.

    Ejemplo:
        >>> reducir(lista, lambda acc, x: acc + x, 0)
        Suma de todos los elementos
    """
    iterador = iterar_lista(lista)
    if valor_inicial is None:
        try:
            acumulador = next(iterador)
        except StopIteration:
            raise TypeError("Reducir de lista vacía sin valor inicial")
    else:
        acumulador = valor_inicial

    for dato in iterador:
        acumulador = funcion(acumulador, dato)
    return acumulador


def dividir_por(lista: Lista, valor) -> tuple:
    """
    Divide la lista en dos listas: elementos menores o iguales y elementos mayores que un valor dado.

    Args:
        lista (Lista): La lista a dividir.
        valor (any): Valor de comparación.

    Returns:
        tuple: Tupla con dos listas (menores_iguales, mayores).

    Ejemplo:
        >>> menores, mayores = dividir_por(lista, 10)
    """
    menores_iguales = Lista()
    mayores = Lista()
    for dato in iterar_lista(lista):
        if dato <= valor:
            menores_iguales.agregarAlFinal(dato)
        else:
            mayores.agregarAlFinal(dato)
    return menores_iguales, mayores


def desde_hasta(lista: Lista, desde: int, hasta: int) -> Lista:
    """
    Obtiene una sublista desde la posición 'desde' hasta 'hasta' (sin incluir 'hasta').

    Args:
        lista (Lista): La lista original.
        desde (int): Índice inicial (inclusive).
        hasta (int): Índice final (exclusivo).

    Returns:
        Lista: Sublista con elementos en el rango dado.

    Raises:
        IndexError: Si los índices son inválidos (fuera de rango o desde > hasta).

    Ejemplo:
        >>> desde_hasta(lista, 1, 4)
        Lista con elementos de índice 1, 2 y 3
    """
    if desde < 0 or hasta > lista.tamaño() or desde > hasta:
        raise IndexError("Indices inválidos")
    resultado = Lista()
    for i in range(desde, hasta):
        resultado.agregarAlFinal(lista.obtener(i))
    return resultado


def inicio_fin_paso(lista: Lista, inicio: int, fin: int, paso: int) -> Lista:
    """
    Obtiene una sublista desde 'inicio' hasta 'fin' con un paso definido.

    Args:
        lista (Lista): La lista original.
        inicio (int): Índice inicial.
        fin (int): Índice final (exclusivo).
        paso (int): Paso entre índices (no puede ser 0).

    Returns:
        Lista: Sublista con elementos en el rango y paso indicados.

    Raises:
        ValueError: Si paso es 0.
        IndexError: Si los índices son inválidos.

    Ejemplo:
        >>> inicio_fin_paso(lista, 0, 6, 2)
        Lista con elementos en posiciones 0, 2, 4
    """
    if paso == 0:
        raise ValueError("Paso no puede ser cero")
    tam = lista.tamaño()
    if not (0 <= inicio < tam) or not (0 < fin <= tam):
        raise IndexError("Indices inválidos")
    resultado = Lista()
    for i in range(inicio, fin, paso):
        resultado.agregarAlFinal(lista.obtener(i))
    return resultado


def sin_el_ultimo(lista: Lista) -> Lista:
    """
    Retorna una nueva lista con todos los elementos excepto el último.

    Args:
        lista (Lista): La lista original.

    Returns:
        Lista: Sublista sin el último elemento.

    Ejemplo:
        >>> sin_el_ultimo(lista)
        Lista sin el último elemento
    """
    tam = lista.tamaño()
    if tam == 0:
        return Lista()
    return desde_hasta(lista, 0, tam - 1)


def sin_el_primero(lista: Lista) -> Lista:
    """
    Retorna una nueva lista con todos los elementos excepto el primero.

    Args:
        lista (Lista): La lista original.

    Returns:
        Lista: Sublista sin el primer elemento.

    Ejemplo:
        >>> sin_el_primero(lista)
        Lista sin el primer elemento
    """
    tam = lista.tamaño()
    if tam == 0:
        return Lista()
    return desde_hasta(lista, 1, tam)


def intercambiar_posiciones(lista: Lista, pos_a: int, pos_b: int) -> None:
    """
    Intercambia los elementos en las posiciones pos_a y pos_b de la lista.

    Args:
        lista (Lista): La lista en la que se intercambian los elementos.
        pos_a (int): Primera posición a intercambiar.
        pos_b (int): Segunda posición a intercambiar.

    Raises:
        IndexError: Si alguna posición es inválida.

    Ejemplo:
        >>> intercambiar_posiciones(lista, 1, 3)
    """
    if not es_posicion_valida(lista, pos_a) or not es_posicion_valida(lista, pos_b):
        raise IndexError("Posiciones inválidas")
    if pos_a == pos_b:
        return

    dato_pos_a = lista.obtener(pos_a)
    dato_pos_b = lista.obtener(pos_b)

    indice_mayor = max(pos_a, pos_b)
    indice_menor = min(pos_a, pos_b)

    lista.eliminar(indice_mayor)
    lista.eliminar(indice_menor)

    lista.insertar(dato_pos_b, indice_menor)
    lista.insertar(dato_pos_a, indice_mayor)


def es_posicion_valida(lista: Lista, pos: int) -> bool:
    """
    Verifica si una posición es válida dentro de la lista.

    Args:
        lista (Lista): La lista en la que se verifica la posición.
        pos (int): La posición a verificar.

    Returns:
        bool: True si la posición es válida, False en caso contrario.

    Ejemplo:
        >>> es_posicion_valida(lista, 3)
        True
    """
    return 0 <= pos < lista.tamaño()
