import math
from collections import deque

from p2.arboles import ABB20


# =======================================================
# ÍNDICE DE MÉTODOS EXTRA  (Ejercicios 21 – 40)
# Clase ABB40
# =======================================================

# -------------------------------------------------------
# CATEGORÍA: Forma / estructura global
# -------------------------------------------------------
# esDegenerado() -> bool
#    True si el ABB se comporta como una lista (cada nodo
#    tiene a lo sumo un hijo).
#
# diametro() -> int
#    Longitud (en aristas) del camino más largo entre dos hojas.
#
# anchoMaximo() -> int
#    Máximo número de nodos que existe simultáneamente en algún nivel.
#
# nivelDeAnchoMaximo() -> int | None
#    Nivel donde se alcanza el ancho máximo; None si el árbol está vacío.

# -------------------------------------------------------
# CATEGORÍA: Validación de propiedad ABB
# -------------------------------------------------------
# verificarPropiedadABB() -> bool
#    Recorre el árbol y comprueba que el in-orden esté ordenado
#    estrictamente (todos los nodos cumplen la regla ABB).

# -------------------------------------------------------
# CATEGORÍA: Selección de elementos (orden estadístico)
# -------------------------------------------------------
# kthMenor(k: int) -> int | None
#    Devuelve el k-ésimo menor (k empieza en 1).
#
# kthMayor(k: int) -> int | None
#    Devuelve el k-ésimo mayor.
#
# nodoMasCercano(objetivo: int) -> int | None
#    Valor almacenado con menor diferencia absoluta al objetivo.

# -------------------------------------------------------
# CATEGORÍA: Relaciones entre nodos
# -------------------------------------------------------
# lca(a: int, b: int) -> int | None
#    Lowest Common Ancestor de a y b (suponiendo que existen).
#
# distanciaEntre(a: int, b: int) -> int | None
#    Número de aristas del camino más corto entre los dos valores.
#
# caminoARaiz(dato: int) -> list[int] | None
#    Ruta dato → … → raíz.  None si el dato no está.
#
# caminoEntre(a: int, b: int) -> list[int] | None
#    Secuencia de valores que conecta a con b.  None si alguno no existe.

# -------------------------------------------------------
# CATEGORÍA: Profundidad mínima / primeras hojas
# -------------------------------------------------------
# profundidadMinima() -> int
#    Longitud del camino raíz-hoja más corto (−1 si vacío).

# -------------------------------------------------------
# CATEGORÍA: Niveles y estadísticas por nivel
# -------------------------------------------------------
# nivelesComoListas() -> list[list[int]]
#    Devuelve lista de niveles, cada nivel como lista de valores.
#
# sumaPorNivel() -> list[int]
#    Suma de los valores de cada nivel (posición i = nivel i).
#
# promedioPorNivel() -> list[float]
#    Promedio aritmético de cada nivel.
#
# anchoNivel(n: int) -> int
#    Cantidad de nodos ubicados exactamente en el nivel n.
#
# nodosEnNivel(n: int) -> list[int]
#    Lista de valores presentes en el nivel n (orden izquierda-derecha).

# -------------------------------------------------------
# CATEGORÍA: Recorridos especiales / impresión
# -------------------------------------------------------
# imprimirZigZag() -> None
#    Imprime los niveles alternando orientación: izquierda-derecha,
#    luego derecha-izquierda, y así sucesivamente.
#
# imprimirHojasDerechaIzquierda() -> None
#    Imprime la frontera (hojas) comenzando por la más derecha
#    y avanzando hacia la izquierda.

# -------------------------------------------------------
# BLOQUE DE EJERCICIOS 21 – 40
# -------------------------------------------------------
class ABB40(ABB20):
    """
    Extensión de ABB20 con los ejercicios 21‒40.
    """

    # ---------- Nodo con utilidades extra -----------------------
    class __NodoArbol(ABB20.__NodoArbol):
        # 21  (degenerado = lista)
        def _esDegenerado(self) -> bool:
            hijos = int(self.tieneIzquierdo()) + int(self.tieneDerecho())
            if hijos == 2:
                return False
            ok_izq = self.izquierdo._esDegenerado() if self.tieneIzquierdo() else True
            ok_der = self.derecho._esDegenerado() if self.tieneDerecho() else True
            return ok_izq and ok_der

        # 22  (altura, diámetro)  – diámetro en aristas
        def _alturaDiametro(self) -> tuple[int, int]:
            h_izq = h_der = -1
            d_izq = d_der = 0
            if self.tieneIzquierdo():
                h_izq, d_izq = self.izquierdo._alturaDiametro()
            if self.tieneDerecho():
                h_der, d_der = self.derecho._alturaDiametro()
            altura = 1 + max(h_izq, h_der)
            diam_pasa = (h_izq + 2 + h_der) if (h_izq >= 0 and h_der >= 0) else max(h_izq + 1, h_der + 1)
            diam = max(diam_pasa, d_izq, d_der)
            return altura, diam

        # 25  – validar propiedad ABB usando rango permitido
        def _esABB(self, minimo: int, maximo: int) -> bool:
            if not (minimo < self.dato < maximo):
                return False
            izq_ok = self.izquierdo._esABB(minimo, self.dato) if self.tieneIzquierdo() else True
            der_ok = self.derecho._esABB(self.dato, maximo) if self.tieneDerecho() else True
            return izq_ok and der_ok

        # 39  – recorrido ZigZag colector por niveles
        def _recoZigZag(self) -> list[list[int]]:
            resultado: list[list[int]] = []
            cola = deque([self])
            izquierda = True
            while cola:
                nivel_len = len(cola)
                linea: list[int] = []
                for _ in range(nivel_len):
                    nodo = cola.popleft()
                    linea.append(nodo.dato)
                    if nodo.tieneIzquierdo():
                        cola.append(nodo.izquierdo)
                    if nodo.tieneDerecho():
                        cola.append(nodo.derecho)
                if not izquierda:
                    linea.reverse()
                resultado.append(linea)
                izquierda = not izquierda
            return resultado

        # 40 – frontera derecha-izquierda
        def _fronteraDerIzq(self, destino: list) -> None:
            if self.esHoja():
                destino.append(self.dato)
            else:
                if self.tieneDerecho():
                    self.derecho._fronteraDerIzq(destino)
                if self.tieneIzquierdo():
                    self.izquierdo._fronteraDerIzq(destino)

    # ======================================================
    #  MÉTODOS PÚBLICOS  ejercicios 21 ‒ 40
    # ======================================================

    # 21
    def esDegenerado(self) -> bool:
        return True if self.estaVacio() else self.__raiz._esDegenerado()

    # 22
    def diametro(self) -> int:
        return 0 if self.estaVacio() else self.__raiz._alturaDiametro()[1]

    # 23
    def anchoMaximo(self) -> int:
        if self.estaVacio():
            return 0
        maxi = 0
        cola = deque([self.__raiz])
        while cola:
            maxi = max(maxi, len(cola))
            for _ in range(len(cola)):
                nodo = cola.popleft()
                if nodo.tieneIzquierdo():
                    cola.append(nodo.izquierdo)
                if nodo.tieneDerecho():
                    cola.append(nodo.derecho)
        return maxi

    # 24
    def nivelDeAnchoMaximo(self) -> int | None:
        if self.estaVacio():
            return None
        cola = deque([(self.__raiz, 0)])
        max_ancho = 0
        nivel_max = 0
        while cola:
            nivel_actual = cola[0][1]
            ancho = sum(1 for n, niv in cola if niv == nivel_actual)
            if ancho > max_ancho:
                max_ancho, nivel_max = ancho, nivel_actual
            nodo, niv = cola.popleft()
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))
        return nivel_max

    # 25
    def verificarPropiedadABB(self) -> bool:
        if self.estaVacio():
            return True
        return self.__raiz._esABB(-math.inf, math.inf)

    # 26
    def kthMenor(self, k: int) -> int | None:
        if self.estaVacio() or k <= 0 or k > self.peso():
            return None
        pila = []
        actual = self.__raiz
        contador = 0
        # in-orden iterativo
        while pila or actual:
            while actual:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            contador += 1
            if contador == k:
                return actual.dato
            actual = actual.derecho
        return None

    # 27
    def kthMayor(self, k: int) -> int | None:
        if self.estaVacio() or k <= 0 or k > self.peso():
            return None
        pila = []
        actual = self.__raiz
        contador = 0
        # reverse-in-orden iterativo
        while pila or actual:
            while actual:
                pila.append(actual)
                actual = actual.derecho
            actual = pila.pop()
            contador += 1
            if contador == k:
                return actual.dato
            actual = actual.izquierdo
        return None

    # 28
    def nodoMasCercano(self, objetivo: int) -> int | None:
        if self.estaVacio():
            return None
        actual = self.__raiz
        mas_cerca = actual.dato
        while actual:
            if abs(actual.dato - objetivo) < abs(mas_cerca - objetivo):
                mas_cerca = actual.dato
            actual = actual.izquierdo if objetivo < actual.dato else actual.derecho
        return mas_cerca

    # 29
    def lca(self, a: int, b: int) -> int | None:
        """
        Devuelve el Lowest Common Ancestor (valor) de a y b
        suponiendo que ambos existen.
        """
        if self.estaVacio():
            return None
        actual = self.__raiz
        while actual:
            if a < actual.dato and b < actual.dato:
                actual = actual.izquierdo
            elif a > actual.dato and b > actual.dato:
                actual = actual.derecho
            else:
                return actual.dato
        return None

    # 30
    def distanciaEntre(self, a: int, b: int) -> int | None:
        lca_val = self.lca(a, b)
        if lca_val is None:
            return None
        return self.__distanciaDesde(lca_val, a) + self.__distanciaDesde(lca_val, b)

    def __distanciaDesde(self, origen: int, destino: int) -> int:
        nodo = self.__raiz
        dist = 0
        while nodo and nodo.dato != destino:
            nodo = nodo.izquierdo if destino < nodo.dato else nodo.derecho
            dist += 1
        return dist

    # 31
    def caminoARaiz(self, dato: int) -> list[int] | None:
        camino: list[int] = []
        actual = self.__raiz
        while actual:
            camino.append(actual.dato)
            if dato == actual.dato:
                return camino
            actual = actual.izquierdo if dato < actual.dato else actual.derecho
        return None

    # 32
    def caminoEntre(self, a: int, b: int) -> list[int] | None:
        path_a = self.caminoARaiz(a)
        path_b = self.caminoARaiz(b)
        if path_a is None or path_b is None:
            return None
        # quitar ruta común al final de ambas
        while path_a and path_b and path_a[-1] == path_b[-1]:
            comun = path_a.pop()
            path_b.pop()
        resultado = path_a + [comun] + path_b[::-1]
        return resultado

    # 33
    def profundidadMinima(self) -> int:
        if self.estaVacio():
            return -1
        cola = deque([(self.__raiz, 0)])
        while cola:
            nodo, niv = cola.popleft()
            if nodo.esHoja():
                return niv
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))

    # 34
    def nivelesComoListas(self) -> list[list[int]]:
        if self.estaVacio():
            return []
        resultado: list[list[int]] = []
        cola = deque([(self.__raiz, 0)])
        while cola:
            nodo, niv = cola.popleft()
            if niv == len(resultado):
                resultado.append([])
            resultado[niv].append(nodo.dato)
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))
        return resultado

    # 35
    def sumaPorNivel(self) -> list[int]:
        return [sum(nivel) for nivel in self.nivelesComoListas()]

    # 36
    def promedioPorNivel(self) -> list[float]:
        listas = self.nivelesComoListas()
        return [sum(nivel) / len(nivel) for nivel in listas]

    # 37
    def anchoNivel(self, n: int) -> int:
        if self.estaVacio():
            return 0
        ancho = 0
        cola = deque([(self.__raiz, 0)])
        while cola:
            nodo, niv = cola.popleft()
            if niv == n:
                ancho += 1
            if niv > n:
                break
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))
        return ancho

    # 38
    def nodosEnNivel(self, n: int) -> list[int]:
        if self.estaVacio():
            return []
        lista: list[int] = []
        cola = deque([(self.__raiz, 0)])
        while cola:
            nodo, niv = cola.popleft()
            if niv == n:
                lista.append(nodo.dato)
            if niv > n:
                break
            if nodo.tieneIzquierdo():
                cola.append((nodo.izquierdo, niv + 1))
            if nodo.tieneDerecho():
                cola.append((nodo.derecho, niv + 1))
        return lista

    # 39
    def imprimirZigZag(self) -> None:
        if self.estaVacio():
            return
        for linea in self.__raiz._recoZigZag():
            print(*linea)

    # 40
    def imprimirHojasDerechaIzquierda(self) -> None:
        if self.estaVacio():
            return
        lista: list[int] = []
        self.__raiz._fronteraDerIzq(lista)
        for v in lista:
            print(v)

    # -------------------------------------------------------
    #  Sobrecarga de insertar para usar nuevo nodo
    # -------------------------------------------------------
    def insertar(self, dato: int) -> None:
        nuevo = ABB40.__NodoArbol(dato)
        if self.estaVacio():
            self._ABB40__raiz = nuevo
        else:
            self._ABB40__raiz.insertarNodo(nuevo)

    __raiz: '__NodoArbol | None'
