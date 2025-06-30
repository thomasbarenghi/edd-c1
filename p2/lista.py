# -------------------------------------------------------
# CATEGORÍA: Acceso y Consulta
# -------------------------------------------------------
# obtener(posGet) -> any: Devuelve el dato en la posición indicada.
# tamaño() -> int: Devuelve la cantidad de elementos en la lista.
# estaVacia() -> bool: Verifica si la lista está vacía.
# __repr__() -> str: Devuelve una representación visual de la lista.

# -------------------------------------------------------
# CATEGORÍA: Inserción
# -------------------------------------------------------
# agregarAlFinal(dato) -> None: Agrega un nuevo nodo al final de la lista.
# insertar(dato, posIns) -> None: Inserta un nodo en una posición específica.
# insertarOrdenado(dato) -> None: Inserta el dato manteniendo orden ascendente.

# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------
# eliminar(posDel) -> any: Elimina el nodo en la posición dada.
# eliminarOcurrencias(dato) -> int: Elimina todas las ocurrencias del dato.

# -------------------------------------------------------
# CATEGORÍA: Búsqueda
# -------------------------------------------------------
# buscaElemento(buscado) -> Lista: Devuelve una lista con las posiciones del valor buscado.

# -------------------------------------------------------
# CATEGORÍA: Modificación
# -------------------------------------------------------
# reemplazaMayores(limite, multiplicador) -> None: Multiplica los mayores o iguales al límite.
# reemplazar(posicion, nuevoDato) -> None: Reemplaza el dato en una posición dada.

# -------------------------------------------------------
# CATEGORÍA: Movimiento de Elementos
# -------------------------------------------------------
# moverPrimeroAlFinal() -> None: Mueve el primer nodo al final.
# moverUltimoAlInicio() -> None: Mueve el último nodo al inicio.
# intercambiarLos2Primeros() -> None: Intercambia los dos primeros nodos.

# -------------------------------------------------------
# CATEGORÍA: Recorridos Personalizados
# -------------------------------------------------------
# recorridoSalteado() -> None: Imprime los nodos en posiciones pares (0, 2, 4, ...).
# recorridoParImpar() -> None: Imprime nodos con lógica par-impar en base al dato.

# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------
# duplicar() -> None: Duplica todos los elementos agregándolos al final.


class Lista:
    class NodoLista:
        """
        Representa un nodo individual de una lista enlazada.

        Attributes:
            dato (any): El dato almacenado en el nodo.
            siguiente (NodoLista): Referencia al siguiente nodo.
        """

        def __init__(self, dato: any):
            """
            Inicializa un nuevo nodo con el dato dado.

            Args:
                dato (any): Valor que se desea almacenar en el nodo.
            """
            self.dato = dato
            self.siguiente = None

        def tieneSiguiente(self) -> bool:
            """
            Indica si el nodo tiene un nodo siguiente.

            Returns:
                bool: True si tiene siguiente, False si es el último nodo.
            """
            return self.siguiente is not None

    def __init__(self, inicial: tuple = None):
        """
        Inicializa la lista enlazada. Si se pasa una tupla, carga los elementos al final de la lista.

        Args:
            inicial (tuple, optional): Tupla con los datos iniciales. Default es None.
        """
        self.__primero = None

        if inicial is not None:
            for dato in inicial:
                self.agregarAlFinal(dato)

    def __repr__(self) -> str:
        """
        Devuelve una representación en string de la lista enlazada.

        Returns:
            str: Cadena que representa visualmente la lista.
        """
        salida = "primero"
        nodo_actual = self.__primero

        while nodo_actual is not None:
            salida += f" -> {nodo_actual.dato}"
            nodo_actual = nodo_actual.siguiente

        salida += " -|"
        return salida

    def estaVacia(self) -> bool:
        """
        Verifica si la lista está vacía.

        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        return self.__primero is None

    def estaVacia(self) -> bool:
        """
        Verifica si la lista está vacía.

        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        return self.__primero is None

    def agregarAlFinal(self, dato: any) -> None:
        """
        Agrega un nuevo nodo con el dato dado al final de la lista.

        Args:
            dato (any): Valor a insertar al final de la lista.
        """
        actual = self.__primero

        while actual.tieneSiguiente():
            actual = actual.siguiente

        actual.siguiente = dato

    def tamaño(self) -> int:
        """
        Calcula la cantidad de nodos en la lista.

        Returns:
            int: Número de elementos en la lista.
        """
        actual = self.__primero
        contador = 0

        if actual is None:
            return contador

        actual += 1

        while actual.tieneSiguiente():
            actual += 1
            actual = actual.siguiente

        return contador

    def obtener(self, posGet: int) -> any:
        """
        Devuelve el dato almacenado en una posición específica.

        Args:
            posGet (int): Índice del nodo del que se quiere obtener el dato.

        Returns:
            any: El dato almacenado en la posición indicada.

        Raises:
            IndexError: Si la posición es inválida.
        """
        if not (0 <= posGet < self.tamaño()):
            raise IndexError("Posición incorrecta")

        actual = self.__primero

        for _ in range(posGet):
            actual = actual.siguiente

        return actual.dato

    def insertar(self, dato: any, posIns: int) -> None:
        """
        Inserta un nuevo nodo en la posición indicada.

        Args:
            dato (any): El dato a insertar.
            posIns (int): La posición donde insertar el dato.

        Raises:
            IndexError: Si la posición es negativa o mayor que el tamaño de la lista.
        """
        if not (0 <= posIns <= self.tamaño()):
            raise IndexError("Posición incorrecta")

        nuevo = Lista.NodoLista(dato)
        actual = self.__primero

        # Al principio
        if posIns == 0:
            self.__primero = nuevo
            nuevo.siguiente = actual
            return

        # En otra parte
        for _ in range(posIns - 1):
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def eliminar(self, posDel: int) -> any:
        """
        Elimina el nodo en la posición dada y retorna su dato.

        Args:
            posDel (int): Posición del nodo a eliminar.

        Returns:
            any: El dato del nodo eliminado.

        Raises:
            IndexError: Si la posición es inválida.
        """
        if not (0 <= posDel < self.tamaño()):
            raise IndexError("Posición incorrecta")

        if posDel == 0:
            eliminado = self.__primero
            self.__primero = self.__primero.siguiente
            return eliminado.dato

        actual = self.__primero

        for _ in range(posDel - 1):
            actual = actual.siguiente

        eliminado = actual.siguiente
        actual.siguiente = eliminado.siguiente

        return eliminado.dato

    def intercambiarLos2Primeros(self) -> None:
        """
        Intercambia los dos primeros nodos de la lista si existen.
        """
        if self.__primero is not None and self.__primero.siguiente is not None:
            primero = self.__primero
            segundo = self.__primero.siguiente
            tercero = segundo.siguiente

            # Cambiar punteros
            self.__primero = segundo
            segundo.siguiente = primero
            primero.siguiete = tercero

    def buscaElemento(self, buscado: any) -> 'Lista':
        """
        Devuelve una nueva lista con las posiciones donde aparece un valor.

        Args:
            buscado (any): Valor a buscar en la lista.

        Returns:
            Lista: Lista con las posiciones (enteros) donde se encuentra el valor.
        """
        posiciones = Lista()
        actual = self.__primero
        posActual = 0
        while actual is not None:
            if actual.dato == buscado:
                posiciones.agregarAlFinal(posActual)

            actual = actual.siguiente
            posActual += 1

        return posiciones

    def eliminarOcurrencias(self, dato: any) -> int:
        """
        Elimina todas las ocurrencias del dato en la lista.

        Args:
            dato (any): El dato a eliminar.

        Returns:
            int: Cantidad de veces que se eliminó el dato.
        """
        actual = self.__primero
        anterior = None
        contador = 0

        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.__primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                contador += 1

            else:
                anterior = actual
                actual = actual.siguiente

        return contador

    def moverPrimeroAlFinal(self) -> None:
        """
          Mueve el primer nodo al final de la lista.
          No hace nada si la lista tiene 0 o 1 elementos.
        """
        if self.estaVacia() or self.tamaño() <= 1:
            return None

        primero = self.__primero
        self.__primero = primero.siguiente
        actual = self.__primero

        while actual.tieneSiguiente():
            actual = actual.siguiente

        actual.siguiente = primero
        primero.siguiente = None

        return None

    def moverUltimoAlInicio(self) -> None:
        """
        Mueve el último nodo al comienzo de la lista.
        No hace nada si la lista tiene 0 o 1 elementos.
        """
        if self.estaVacia() or self.tamaño() <= 1:
            return None

        actual = self.__primero
        anterior = None

        while actual.tieneSiguiente():
            anterior = actual
            actual = actual.siguiente

        anterior.siguiente = None
        actual.siguiente = self.__primero
        self.__primero = actual

        return None

    def duplicar(self) -> None:
        """
        Duplica todos los elementos actuales agregándolos al final de la lista.
        Es decir, si la lista es [1, 2, 3], pasará a ser [1, 2, 3, 1, 2, 3].
        """
        if self.estaVacia():
            return None

        a_duplicar = []
        actual = self.__primero

        while actual is not None:
            a_duplicar.append(actual.dato)
            actual = actual.siguiente

        for item in a_duplicar:
            self.agregarAlFinal(item)

        return None

    def recorridoSalteado(self) -> None:
        """
        Imprime los elementos de la lista saltando de a uno.
        Es decir, imprime el primer nodo, luego el tercero, el quinto, etc.
        """
        actual = self.__primero

        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente.siguiente if actual.siguiente else None

        return None

    def recorridoParImpar(self) -> None:
        """
        Recorre la lista imprimiendo:
            - El dato actual.
            - Si el dato es par: avanza al siguiente nodo.
            - Si el dato es impar: salta un nodo (avanza dos posiciones).
        """
        actual = self.__primero

        while actual is not None:
            print(actual.dato)

            if actual.dato % 2 == 0:
                actual = actual.siguiente
            elif actual.siguiente is not None:
                actual = actual.siguiente.siguiente
            else:
                break

        return None

    def reemplazaMayores(self, limite: int, multiplicador: int) -> None:
        """
        Multiplica por un valor todos los nodos cuyo dato sea mayor o igual al límite dado.

        Args:
            limite (int): Valor a partir del cual un dato se considera "mayor o igual".
            multiplicador (int): Valor por el que se multiplicará el dato si cumple la condición.
        """
        actual = self.__primero

        # Recorre toda la lista verificando y actualizando según el criterio
        while actual is not None:
            if actual.dato >= limite:
                actual.dato *= multiplicador

            actual = actual.siguiente

        return None

    def reemplazar(self, posicion: int, nuevoDato: any) -> None:
        """
        Reemplaza el dato en la posición dada con un nuevo dato.

        Args:
            posicion (int): Índice del elemento a reemplazar (0-based).
            nuevoDato (any): Nuevo valor que reemplazará al actual.

        Raises:
            IndexError: Si la posición está fuera del rango de la lista.
        """
        actual = self.__primero
        indice = 0

        while actual is not None:
            if indice == posicion:
                actual.dato = nuevoDato
            else:
                actual = actual.siguiente
                indice += 1

        raise IndexError("La posición está fuera del rango de la lista.")

    def insertarOrdenado(self, dato: any) -> None:
        """
        Inserta un dato en la lista de manera ordenada (de menor a mayor).

        Args:
            dato (any): El dato a insertar manteniendo el orden ascendente.
        """
        nuevo = Lista.NodoLista(dato)

        if self.estaVacia() or dato <= self.__primero.dato:
            nuevo.siguiente = self.__primero
            self.__primero = nuevo
            return None

        actual = self.__primero
        while actual.tieneSiguiente() and actual.siguiente.dato < dato:
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

        return None
