from p2.lista import Lista


# -------------------------------------------------------
# CATEGORÍA: Inserción
# -------------------------------------------------------
# insertarSinRepetir(dato) -> None: Inserta el dato solo si no existe en la lista.
# insertarListaEnPosicion(lista, posIns) -> None: Inserta todos los nodos de otra lista en la posición dada.
# insertarCeros() -> None: Inserta un 0 entre cada par de valores pares consecutivos.

# -------------------------------------------------------
# CATEGORÍA: Eliminación
# -------------------------------------------------------
# eliminarImpares() -> None: Elimina todos los nodos impares. El primero siempre es par.
# eliminarSegmento(inicio, fin) -> None: Elimina los nodos entre las posiciones inicio y fin (inclusive).
# eliminarHastaElFinal(posDel) -> None: Elimina todos los nodos desde posDel hasta el final.
# sacarImpares() -> None: Elimina todos los impares a partir del segundo nodo.

# -------------------------------------------------------
# CATEGORÍA: Transformación
# -------------------------------------------------------
# duplicarElemento(dato) -> None: Duplica cada aparición del dato dado.
# arreglarOrden() -> None: Intercambia el primer par consecutivo que esté en orden creciente.

# -------------------------------------------------------
# CATEGORÍA: Búsqueda / Posicionamiento
# -------------------------------------------------------
# posicionCantImpares(cantImpares) -> int | None: Retorna la posición hasta donde hay exactamente 'cantImpares' impares.


class ListaAdicionales(Lista):
    # De la práctica 2.º parcial
    def duplicarElemento(self, dato: int) -> None:
        """
        Duplica cada ocurrencia de 'dato' en la lista.
        Por cada nodo cuyo valor sea 'dato' se inserta a continuación
        un nuevo nodo con el mismo valor.

        Args
        ----
        dato : int
            Valor a duplicar cada vez que aparezca.
        """
        if self.estaVacia():
            return

        actual = self.__primero

        while actual is not None:
            if actual.dato == dato:
                nuevo = Lista.NodoLista(actual)

                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo

                actual = nuevo.siguiente

            else:
                actual = actual.siguiente

    # Ejercicios de segundo parcial
    def insertarSinRepetir(self, dato):
        """
            Inserta el dato al final de la lista solo si no se encuentra ya presente.

            Args:
                dato (any): Valor a insertar si no está repetido.

            Returns:
                None
        """
        actual = self.__primero

        while actual is not None:
            if actual.dato == dato:
                return None
            actual = actual.siguiente

        self.agregarAlFinal(dato)
        return None

    # Ejercicios de segundo parcial
    # Primero siempre es par
    def eliminarImpares(self):
        """
            Elimina todos los nodos cuyo dato sea impar.
            No retorna una nueva lista.
            Se asume que el primer nodo es par.
        """
        actual = self.__primero
        anterior = None

        while actual is not None:
            if actual.dato % 2 != 0:
                anterior.siguiente = actual.siguiente
                actual = actual.siguiente
            else:
                anterior = actual
                actual = actual.siguiente

    # Ejercicios de segundo parcial
    def insertarListaEnPosicion(self, lista, posIns):
        """
        Inserta todos los nodos de otra lista en una posición dada.

         Args:
        lista (Lista): Lista cuyos nodos se insertarán.
        posIns (int): Posición en la que se deben insertar los nodos.

         Notas:
        - Si posIns es mayor que el tamaño, se inserta al final.
        - No se usan operaciones auxiliares como insertar() ni listas de Python.
        """

        # Caso: lista a insertar está vacía
        if lista.estaVacia():
            return

        # Obtener puntero al primer nodo de la lista a insertar
        primero_insertar = lista.__primero

        # Obtener puntero al último nodo de la lista a insertar
        ultimo_insertar = primero_insertar
        while ultimo_insertar.siguiente is not None:
            ultimo_insertar = ultimo_insertar.siguiente

        # Caso especial: insertar al inicio
        if posIns <= 0 or self.__primero is None:
            ultimo_insertar.siguiente = self.__primero
            self.__primero = primero_insertar
            return

        # Avanzar hasta el nodo anterior a posIns o al final
        actual = self.__primero
        posicion = 0

        while actual.siguiente is not None and posicion < posIns - 1:
            actual = actual.siguiente
            posicion += 1

        # Enlazar el último de la lista insertada con el siguiente de 'actual'
        ultimo_insertar.siguiente = actual.siguiente

        # Enlazar 'actual' con el primero de la lista insertada
        actual.siguiente = primero_insertar

    # Ejercicios de segundo parcial
    def insertarCeros(self):
        """
            Inserta un nodo con valor 0 entre cada par de nodos consecutivos que tengan ambos valores pares.

            Notas:
                - No usa listas auxiliares.
                - No modifica los nodos existentes, solo inserta nuevos.
        """
        actual = self.__primero
        es_par = lambda act, sig: act % 2 == 0 and sig % 2 == 0

        while actual.tieneSiguiente():
            if es_par(actual.dato, actual.siguiente.dato):
                nuevo = Lista.NodoLista(0)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo

                actual = nuevo.siguiente
            else:
                actual = actual.siguiente

    # Ejercicios de segundo parcial
    def eliminarSegmento(self, inicio: int, fin: int) -> None:
        """
        Borra los nodos cuyas posiciones estén entre 'inicio' y 'fin' inclusive.
        Si 'fin' supera el tamaño de la lista, se borra hasta el último nodo disponible.
        Se asume 0 ≤ inicio ≤ fin.

        • No usa Lista de Python
        • No usa la operación eliminar()
        • Solo recorre la lista una vez para encontrar 'inicio' y otra para saltar hasta 'fin'.
        """
        if self.__primero is None:
            return  # Lista vacía, no hay nada que borrar

        # Caso especial: borrar desde el principio
        if inicio == 0:
            actual = self.__primero
            posicion = 0

            while actual is not None and posicion <= fin:
                actual = actual.siguiente
                posicion += 1

            self.__primero = actual
            return

        # Primer recorrido: llegar al nodo anterior al inicio
        actual = self.__primero
        posicion = 0

        while actual is not None and posicion < inicio - 1:
            actual = actual.siguiente
            posicion += 1

        if actual is None or not actual.tieneSiguiente():
            return  # inicio está fuera de rango, nada que borrar

        anterior = actual
        actual = actual.siguiente
        posicion += 1

        # Segundo recorrido: avanzar hasta el nodo en posición fin
        while actual is not None and posicion <= fin:
            actual = actual.siguiente
            posicion += 1

        # Saltar los nodos desde 'inicio' hasta 'fin'
        anterior.siguiente = actual

    # Adicional
    def arreglarOrden(self):
        """
            Si encuentra un par de nodos consecutivos en orden creciente, los invierte.
            Solo realiza una inversión (la primera que detecta).

            Notas:
                - No usa estructuras auxiliares.
                - La modificación es in-place.
        """
        if self.__primero is None or self.__primero.siguiente is None:
            return None

        actual = self.__primero

        anterior = None

        while actual.tieneSiguiente():
            if actual.dato < actual.siguiente.dato:
                nodo_menor = actual
                nodo_mayor = actual.siguiente

                if anterior is None:
                    self.__primero = nodo_mayor
                else:
                    anterior.siguiente = nodo_mayor

                nodo_menor.siguiente = nodo_mayor.siguiente
                nodo_mayor.siguiente = nodo_menor

                return None

            else:
                anterior = actual
                actual = actual.siguiente

        return None

    def eliminarHastaElFinal(self, posDel):
        """
            Elimina todos los nodos desde la posición posDel hasta el final de la lista.

            Args:
                posDel (int): Índice desde donde se comenzará a eliminar (inclusive).

            Returns:
                None
        """
        if 0 <= posDel:
            self.__primero = None

        if posDel >= self.tamaño():
            return None

        actual = self.__primero
        posicion = 0

        while actual.tieneSiguiente():
            if posicion == posDel - 1:  # Anterior a borrar
                actual.siguiente = None
                return None

            actual = actual.siguiente
            posicion += 1

        return None

    def sacarImpares(self):
        """
        Elimina todos los nodos impares de la lista.
        No retorna una nueva lista.
        No usa la operación eliminar().
        El primer nodo siempre es par.
        """
        actual = self.__primero

        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.dato % 2 != 0:
                # El siguiente es impar, lo "salteamos"
                actual.siguiente = actual.siguiente.siguiente
            else:
                # El siguiente es par, avanzamos
                actual = actual.siguiente

    def posicionCantImpares(self, cantImpares: int):
        """
        Retorna la posición 'posHasta' tal que entre las posiciones 0 y posHasta
        haya exactamente 'cantImpares' números impares. Si no hay suficientes,
        retorna None.
        """
        actual = self.__primero
        posicion = 0
        contador = 0

        while actual is not None:
            if actual.dato % 2 != 0:
                contador += 1
                if contador == cantImpares:
                    return posicion
            actual = actual.siguiente
            posicion += 1

        return None
