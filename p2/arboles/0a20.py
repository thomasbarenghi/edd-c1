from collections import deque

from p2.abb import ABB


# =======================================================
# ÍNDICE DE MÉTODOS EXTRA  (Ejercicios 1 – 20)
# Clase ABB20
# =======================================================

# -------------------------------------------------------
# CATEGORÍA: Conteo según hijos / estructura
# -------------------------------------------------------
# contarNodosConUnSoloHijo() -> int
#    Devuelve cuántos nodos poseen exactamente un hijo.
#
# contarNodosConDosHijos() -> int
#    Devuelve cuántos nodos poseen los dos hijos.
#
# contarNodosSoloIzquierdo() -> int
#    Cantidad de nodos cuyo único hijo está a la izquierda.
#
# contarNodosSoloDerecho() -> int
#    Cantidad de nodos cuyo único hijo está a la derecha.

# -------------------------------------------------------
# CATEGORÍA: Estadísticas globales del árbol
# -------------------------------------------------------
# sumaValores() -> int
#    Suma de todos los datos almacenados.
#
# promedioValores() -> float | None
#    Promedio de los valores (None si el árbol está vacío).
#
# productoValores() -> int | None
#    Producto de todos los datos (None si el árbol está vacío).

# -------------------------------------------------------
# CATEGORÍA: Consultas por nivel
# -------------------------------------------------------
# maximoNivelPar() -> int | None
#    Valor máximo entre los nodos situados en niveles pares.
#
# minimoNivelImpar() -> int | None
#    Valor mínimo entre los nodos situados en niveles impares.

# -------------------------------------------------------
# CATEGORÍA: Consultas por rango de valores
# -------------------------------------------------------
# contarMayoresQue(x: int) -> int
#    Cantidad de valores estrictamente mayores que x.
#
# contarMenoresQue(x: int) -> int
#    Cantidad de valores estrictamente menores que x.
#
# contarEnRango(a: int, b: int) -> int
#    Número de valores ubicados en el intervalo cerrado [a, b].
#
# listaEnRango(a: int, b: int) -> list[int]
#    Lista ordenada ascendente con los valores en el rango.
#
# eliminarEnRango(a: int, b: int) -> int
#    Elimina todos los nodos dentro del rango y devuelve cuántos quitó.

# -------------------------------------------------------
# CATEGORÍA: Inserción masiva / construcción
# -------------------------------------------------------
# insertarLista(valores: list[int]) -> None
#    Inserta secuencialmente todos los enteros de la lista (sin repetidos).
#
# construirBalanceado(listaOrdenada: list[int]) -> None
#    Destruye el árbol actual y genera un ABB perfectamente balanceado
#    a partir de una lista ascendente.

# -------------------------------------------------------
# CATEGORÍA: Propiedades de balance / completitud
# -------------------------------------------------------
# esBalanceado() -> bool
#    True si para todo nodo |altura(izq) − altura(der)| ≤ 1.
#
# factorBalance(dato: int) -> int | None
#    Altura(izq) − Altura(der) del nodo cuyo dato se indica.
#
# esCompleto() -> bool
#    True si el árbol es completo (niveles llenos salvo quizá el último,
#    que se completa de izquierda a derecha).
#
# esPerfecto() -> bool
#    True si todas las hojas están al mismo nivel y cada nodo interno
#    tiene exactamente dos hijos.

# -------------------------------------------------------
# BLOQUE DE EJERCICIOS 1 – 20
# -------------------------------------------------------
class ABB20(ABB):
    """
    Extensión de ABB que incorpora los 20 primeros ejercicios
    solicitados.
    """

    # ------------- N O D O   interno con extras -----------------
    class __NodoArbol(ABB.__NodoArbol):
        # ---- Ej.1: nodos con un solo hijo --------------------
        def _contarUnSoloHijo(self) -> int:
            cant = 1 if self.tieneIzquierdo() ^ self.tieneDerecho() else 0
            if self.tieneIzquierdo():
                cant += self.izquierdo._contarUnSoloHijo()
            if self.tieneDerecho():
                cant += self.derecho._contarUnSoloHijo()
            return cant

        # ---- Ej.2: nodos con dos hijos -----------------------
        def _contarDosHijos(self) -> int:
            cant = 1 if self.tieneIzquierdo() and self.tieneDerecho() else 0
            if self.tieneIzquierdo():
                cant += self.izquierdo._contarDosHijos()
            if self.tieneDerecho():
                cant += self.derecho._contarDosHijos()
            return cant

        # ---- Ej.3 / 4: solo hijo izq / solo hijo der ----------
        def _contarSoloIzq(self) -> int:
            cant = 1 if self.tieneIzquierdo() and not self.tieneDerecho() else 0
            if self.tieneIzquierdo():
                cant += self.izquierdo._contarSoloIzq()
            if self.tieneDerecho():
                cant += self.derecho._contarSoloIzq()
            return cant

        def _contarSoloDer(self) -> int:
            cant = 1 if self.tieneDerecho() and not self.tieneIzquierdo() else 0
            if self.tieneIzquierdo():
                cant += self.izquierdo._contarSoloDer()
            if self.tieneDerecho():
                cant += self.derecho._contarSoloDer()
            return cant

        # ---- Ej.5 suma de valores ----------------------------
        def _sumaValores(self) -> int:
            total = self.dato
            if self.tieneIzquierdo():
                total += self.izquierdo._sumaValores()
            if self.tieneDerecho():
                total += self.derecho._sumaValores()
            return total

        # ---- Ej.7 producto de valores ------------------------
        def _productoValores(self) -> int:
            prod = self.dato
            if self.tieneIzquierdo():
                prod *= self.izquierdo._productoValores()
            if self.tieneDerecho():
                prod *= self.derecho._productoValores()
            return prod

        # ---- Ej.10 / 11 / 12  conteos con condiciones --------
        def _contarMayoresQue(self, x: int) -> int:
            cant = 1 if self.dato > x else 0
            if self.tieneIzquierdo():
                cant += self.izquierdo._contarMayoresQue(x)
            if self.tieneDerecho():
                cant += self.derecho._contarMayoresQue(x)
            return cant

        def _contarMenoresQue(self, x: int) -> int:
            cant = 1 if self.dato < x else 0
            if self.tieneIzquierdo():
                cant += self.izquierdo._contarMenoresQue(x)
            if self.tieneDerecho():
                cant += self.derecho._contarMenoresQue(x)
            return cant

        def _contarEnRango(self, a: int, b: int) -> int:
            cant = 1 if a <= self.dato <= b else 0
            if self.tieneIzquierdo() and self.dato >= a:
                cant += self.izquierdo._contarEnRango(a, b)
            if self.tieneDerecho() and self.dato <= b:
                cant += self.derecho._contarEnRango(a, b)
            return cant

        def _listaEnRango(self, a: int, b: int, destino: list) -> None:
            if self.tieneIzquierdo() and self.dato >= a:
                self.izquierdo._listaEnRango(a, b, destino)
            if a <= self.dato <= b:
                destino.append(self.dato)
            if self.tieneDerecho() and self.dato <= b:
                self.derecho._listaEnRango(a, b, destino)

        # ---- Ej.17 ver si subárbol está balanceado -----------
        #    retorna (altura, balanced?)
        def _alturaYBalance(self) -> tuple[int, bool]:
            izq_alt = der_alt = 0
            izq_ok = der_ok = True
            if self.tieneIzquierdo():
                izq_alt, izq_ok = self.izquierdo._alturaYBalance()
            if self.tieneDerecho():
                der_alt, der_ok = self.derecho._alturaYBalance()
            ok = izq_ok and der_ok and abs(izq_alt - der_alt) <= 1
            return 1 + max(izq_alt, der_alt), ok

        # ---- Ej.18 factor de balance del nodo ----------------
        def _factorBalance(self) -> int:
            alt_izq = self.izquierdo.alturaNodo() if self.tieneIzquierdo() else -1
            alt_der = self.derecho.alturaNodo() if self.tieneDerecho() else -1
            return alt_izq - alt_der

        # ---- Ej.19 / 20 para completo y perfecto -------------
        def _alturaYCompletoPerfecto(self) -> tuple[int, bool, bool]:
            """
            Devuelve (altura, esCompleto, esPerfecto) para el subárbol.
            """
            if self.esHoja():
                return 0, True, True
            alt_izq, comp_izq, perf_izq = (-1, True, True)
            alt_der, comp_der, perf_der = (-1, True, True)
            if self.tieneIzquierdo():
                alt_izq, comp_izq, perf_izq = self.izquierdo._alturaYCompletoPerfecto()
            if self.tieneDerecho():
                alt_der, comp_der, perf_der = self.derecho._alturaYCompletoPerfecto()

            altura = 1 + max(alt_izq, alt_der)

            # perfecto: ambos subárboles perfectos y misma altura
            es_perfecto = (
                    perf_izq
                    and perf_der
                    and alt_izq == alt_der
                    and self.tieneIzquierdo()
                    and self.tieneDerecho()
            )

            # completo: condiciones típicas
            if alt_izq == alt_der:
                es_completo = comp_izq and self.tieneIzquierdo() and comp_der
            elif alt_izq == alt_der + 1:
                es_completo = comp_izq and perf_der
            else:
                es_completo = False

            return altura, es_completo, es_perfecto

    # ===========================================================
    #  Métodos públicos ejercicios 1‒20
    # ===========================================================

    # 1
    def contarNodosConUnSoloHijo(self) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarUnSoloHijo()

    # 2
    def contarNodosConDosHijos(self) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarDosHijos()

    # 3
    def contarNodosSoloIzquierdo(self) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarSoloIzq()

    # 4
    def contarNodosSoloDerecho(self) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarSoloDer()

    # 5
    def sumaValores(self) -> int:
        return 0 if self.estaVacio() else self.__raiz._sumaValores()

    # 6
    def promedioValores(self) -> float | None:
        if self.estaVacio():
            return None
        return self.sumaValores() / self.peso()

    # 7
    def productoValores(self) -> int | None:
        return None if self.estaVacio() else self.__raiz._productoValores()

    # 8
    def maximoNivelPar(self) -> int | None:
        if self.estaVacio():
            return None
        max_par = None
        cola = deque([(self.__raiz, 0)])
        while cola:
            nodo, niv = cola.popleft()
            if niv % 2 == 0:
                max_par = nodo.dato if max_par is None else max(max_par, nodo.dato)
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))
        return max_par

    # 9
    def minimoNivelImpar(self) -> int | None:
        if self.estaVacio():
            return None
        min_imp = None
        cola = deque([(self.__raiz, 0)])
        while cola:
            nodo, niv = cola.popleft()
            if niv % 2 == 1:
                min_imp = nodo.dato if min_imp is None else min(min_imp, nodo.dato)
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))
        return min_imp

    # 10
    def contarMayoresQue(self, x: int) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarMayoresQue(x)

    # 11
    def contarMenoresQue(self, x: int) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarMenoresQue(x)

    # 12
    def contarEnRango(self, a: int, b: int) -> int:
        return 0 if self.estaVacio() else self.__raiz._contarEnRango(a, b)

    # 13
    def listaEnRango(self, a: int, b: int) -> list[int]:
        lst: list[int] = []
        if not self.estaVacio():
            self.__raiz._listaEnRango(a, b, lst)
        return lst

    # 14
    def eliminarEnRango(self, a: int, b: int) -> int:
        """
        Elimina y cuenta cuántos valores estaban en el intervalo [a, b].
        """
        aLista = self.listaEnRango(a, b)
        for v in aLista:
            self.eliminar(v)
        return len(aLista)

    # 15
    def insertarLista(self, valores: list[int]) -> None:
        for v in valores:
            self.insertar(v)

    # 16
    def construirBalanceado(self, listaOrdenada: list[int]) -> None:
        """
        Destruye el contenido actual y arma un ABB perfectamente
        balanceado a partir de la lista ascendente provista.
        """

        def _construir(l: int, r: int) -> 'ABB20.__NodoArbol | None':
            if l > r:
                return None
            m = (l + r) // 2
            nodo = ABB20.__NodoArbol(listaOrdenada[m])
            nodo.izquierdo = _construir(l, m - 1)
            nodo.derecho = _construir(m + 1, r)
            return nodo

        self.vaciar()
        if listaOrdenada:
            self.__raiz = _construir(0, len(listaOrdenada) - 1)

    # 17
    def esBalanceado(self) -> bool:
        return True if self.estaVacio() else self.__raiz._alturaYBalance()[1]

    # 18
    def factorBalance(self, dato: int) -> int | None:
        """
        Devuelve altura(izq) - altura(der) del nodo cuyo dato se indica.
        """
        nodo = self.__buscarNodo(dato)
        return None if nodo is None else nodo._factorBalance()

    def __buscarNodo(self, dato: int) -> 'ABB20.__NodoArbol | None':
        # búsqueda interna (iterativa)
        actual = self.__raiz
        while actual is not None:
            if dato == actual.dato:
                return actual
            actual = actual.izquierdo if dato < actual.dato else actual.derecho
        return None

    # 19
    def esCompleto(self) -> bool:
        if self.estaVacio():
            return True
        return self.__raiz._alturaYCompletoPerfecto()[1]

    # 20
    def esPerfecto(self) -> bool:
        if self.estaVacio():
            return True
        return self.__raiz._alturaYCompletoPerfecto()[2]

    # -------------------------------------------------------
    #  Sobrecarga de insertar para usar nuestro nuevo Nodo
    # -------------------------------------------------------
    def insertar(self, dato: int) -> None:
        nuevo = ABB20.__NodoArbol(dato)
        if self.estaVacio():
            self._ABB20__raiz = nuevo  # evita name-mangling externo
        else:
            self._ABB20__raiz.insertarNodo(nuevo)

    # Re‐alias raíz para el nombre mangled correcto
    __raiz: '__NodoArbol | None'
