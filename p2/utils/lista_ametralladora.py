from p2.lista import Lista


# linkedlist
class ListaEx1(Lista):
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
        # Caso lista vacía
        if self.estaVacia():
            return

        actual = self.__primero

        while actual is not None:
            if actual.dato == dato:
                # Crear duplicado
                nuevo = Lista.NodoLista(dato)
                # Enlazar duplicado después de 'actual'
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                # Saltar sobre el duplicado para no procesarlo otra vez
                actual = nuevo.siguiente
            else:
                # Continuar recorriendo la lista normalmente
                actual = actual.siguiente

    def eliminarSegmento(self, inicio: int, fin: int) -> None:
        """
        Borra los nodos cuyas posiciones estén entre 'inicio' y 'fin'
        inclusive.  Si 'fin' supera el tamaño de la lista, se borra hasta
        el último nodo disponible.  Se asume 0 ≤ inicio ≤ fin.

        • No usa Lista de Python
        • No usa la operación eliminar()
        • Solo recorre la lista una vez para encontrar 'inicio' y otra
          para saltar hasta 'fin'.
        """
        # Caso lista vacía
        if self.estaVacia():
            return

        # 1) ¿El borrado comienza en el primer nodo?
        if inicio == 0:
            actual = self.__primero
            pos = 0
            while actual is not None and pos <= fin:
                actual = actual.siguiente
                pos += 1
            self.__primero = actual
            return

        # 2) Localizar el nodo anterior a 'inicio'
        anterior = self.__primero
        pos = 0
        while anterior is not None and pos < inicio - 1:
            anterior = anterior.siguiente
            pos += 1

        # Si 'inicio' está fuera de rango, no hay nada que borrar
        if anterior is None or anterior.siguiente is None:
            return

        # 3) Avanzar desde 'inicio' hasta 'fin'
        actual = anterior.siguiente  # primer nodo a borrar
        pos = inicio
        while actual is not None and pos <= fin:
            actual = actual.siguiente
            pos += 1

        # 4) Puenteamos el segmento eliminado
        anterior.siguiente = actual

    def mergeOrdenado(self, lista2: 'Lista') -> None:
        """
        Fusiona (en orden ascendente) la lista 'lista2' dentro de la lista actual (self).
        Precondición: ambas listas ya están ordenadas.
        Al terminar, self contiene los elementos combinados y lista2 queda vacía.
        """
        # Si una de las dos listas está vacía, la otra ya es la respuesta
        if self.estaVacia():
            self.__primero = lista2._Lista__primero  # tomamos directamente la otra
            lista2._Lista__primero = None  # y la vaciamos
            return
        if lista2.estaVacia():
            return  # nada que hacer

        puntero1 = self.__primero  # cabeza de self
        puntero2 = lista2._Lista__primero  # cabeza de lista2 (acceso interno)

        # Nodo centinela para simplificar la lógica de encadenado
        centinela = Lista.NodoLista(None)
        cola = centinela  # último nodo ya colocado en la lista resultado

        # Se recorre mientras ambas listas tengan elementos
        while puntero1 is not None and puntero2 is not None:
            if puntero1.dato <= puntero2.dato:
                cola.siguiente = puntero1
                puntero1 = puntero1.siguiente
            else:
                cola.siguiente = puntero2
                puntero2 = puntero2.siguiente
            cola = cola.siguiente  # avanzar el final de la lista fusionada

        # Al salir, al menos una de las dos listas llegó a su fin.
        # Se encadena lo que reste (si queda algo) de la otra lista.
        cola.siguiente = puntero1 if puntero1 is not None else puntero2

        # El primer nodo real de la lista fusionada está después del centinela
        self.__primero = centinela.siguiente

        # Dejamos la segunda lista vacía (opcional pero prolijo)
        lista2._Lista__primero = None
    