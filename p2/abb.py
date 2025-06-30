import copy


# -------------------------------------------------------
# CATEGORÍA: Construcción y utilidades generales
# -------------------------------------------------------
# __init__() -> None
#    Crea un ABB vacío.
#
# clonar() -> ABB
#    Devuelve una copia profunda e independiente del árbol.
#
# vaciar() -> None
#    Elimina todos los nodos, dejando el árbol vacío.
#
# estaVacio() -> bool
#    Indica si el ABB no contiene nodos.


# -------------------------------------------------------
# CATEGORÍA: Inserción
# -------------------------------------------------------
# insertar(dato: int) -> None
#    Inserta un entero (sin repetición) en la ubicación correcta.


# -------------------------------------------------------
# CATEGORÍA: Búsqueda y acceso puntual
# -------------------------------------------------------
# buscar(dato: int) -> bool
#    Verifica si el dato existe en el árbol.
#
# buscarNivel(dato: int) -> int | None
#    Retorna la profundidad en la que se halla un dato (None si no existe).
#
# minimo() -> int | None
#    Devuelve el valor mínimo almacenado.
#
# maximo() -> int | None
#    Devuelve el valor máximo almacenado.
#
# buscaPadreYlado(datoBusc: int) -> tuple[int | None, str | None]
#    Entrega el dato del padre y el lado ('izq' / 'der') del hijo buscado.


# -------------------------------------------------------
# CATEGORÍA: Métricas globales
# -------------------------------------------------------
# peso() -> int
#    Cantidad total de nodos del árbol.
#
# altura() -> int
#    Altura de la raíz (–1 si el árbol está vacío).
#
# cantidadHojas() -> int
#    Número total de hojas.
#
# cantidadNodosEnNivel(n: int) -> int
#    Cantidad de nodos ubicados exactamente en el nivel n.


# -------------------------------------------------------
# CATEGORÍA: Recorridos / impresión
# -------------------------------------------------------
# imprimirPreOrden() -> None
#    Muestra los datos en recorrido Pre-Orden (N–Izq–Der).
#
# imprimirInOrden() -> None
#    Muestra los datos en recorrido In-Orden (orden natural ascendente).
#
# imprimirPostOrden() -> None
#    Muestra los datos en recorrido Post-Orden (Izq–Der–N).
#
# mostrarNivel(n: int) -> None
#    Imprime los valores que se encuentran en el nivel n.
#
# imprimirFrontera() -> None
#    Imprime de izquierda a derecha los valores de todas las hojas.
#
# listaOrdenadaPares() -> list[int]
#    Retorna una lista ascendente con todos los valores pares del ABB.


# -------------------------------------------------------
# CATEGORÍA: Eliminación y reestructuración
# -------------------------------------------------------
# eliminar(datoDel: int) -> None
#    Suprime el nodo cuyo dato coincide con datoDel.
#
# rotar() -> None
#    Intercambia recursivamente los subárboles izquierdo y derecho,
#    “invirtiendo” el ABB.
#
# testPredSuc() -> None
#    Imprime el predecesor y sucesor de la raíz (método de prueba).


# =======================================================
#  MÉTODOS INTERNOS (clase __NodoArbol) – para referencia
# =======================================================
#
# -------------------------------------------------------
# Estructura básica
# -------------------------------------------------------
# __init__(dato: int) -> None
#    Crea un nodo hoja con el dato indicado.
#
# tieneIzquierdo() -> bool
# tieneDerecho()  -> bool
#    Indican la existencia de hijos.
#
# grado() -> int
#    Devuelve 0, 1 o 2 según la cantidad de hijos.
#
# esHoja() -> bool
#    True si el nodo no posee hijos.
#
# -------------------------------------------------------
# Recorridos impresos
# -------------------------------------------------------
# imprimirPreOrdenNodo()  -> None
# imprimirInOrdenNodo()   -> None
# imprimirPostOrdenNodo() -> None
#
# -------------------------------------------------------
# Inserción / búsqueda
# -------------------------------------------------------
# insertarNodo(nuevo: __NodoArbol)   -> None
# buscarNodo(datoBusc: int)          -> bool
# buscarNivelNodo(datoBusc: int, nivelActual=0) -> int | None
#
# -------------------------------------------------------
# Métricas locales
# -------------------------------------------------------
# pesoNodo()           -> int
# alturaNodo()         -> int
# cantidadHojasNodo()  -> int
# cantidadNodosEnNivelNodo(buscado: int, actual=0) -> int
#
# -------------------------------------------------------
# Mínimo / máximo y vecinos ordenados
# -------------------------------------------------------
# minimoNodo()      -> __NodoArbol
# maximoNodo()      -> __NodoArbol
# predecesorNodo()  -> __NodoArbol | None
# sucesorNodo()     -> __NodoArbol | None
#
# -------------------------------------------------------
# Eliminación y utilidades
# -------------------------------------------------------
# buscaPadreYladoNodo(datoBusc: int) -> tuple[__NodoArbol | None, str | None]
# eliminarNodo(datoDel: int)        -> None
#
# -------------------------------------------------------
# Recorridos especiales / reordenamiento
# -------------------------------------------------------
# listaOrdenadaParesNodos() -> list[int]
# mostrarNivelNodo(buscado: int, actual=0) -> None
# imprimirFrontera() -> None
# rotarNodo()        -> None


class ABB:
    """Árbol Binario de Búsqueda (ABB) que almacena enteros sin repetición."""

    # ──────────────────────────────────────────────────────────────
    # NODO INTERNO  (no debe usarse de manera directa por el usuario)
    # ──────────────────────────────────────────────────────────────
    class __NodoArbol:
        """Nodo interno del ABB."""

        # --------------- 1. Estructura básica --------------------
        def __init__(self, dato: int) -> None:
            """
            Crea un nodo hoja con el dato especificado.

            Args:
                dato (int): Valor entero a guardar en el nodo.
            """
            self.dato: int = dato
            self.izquierdo: 'ABB.__NodoArbol | None' = None
            self.derecho: 'ABB.__NodoArbol | None' = None

        def tieneIzquierdo(self) -> bool:
            """
            Indica si el nodo posee subárbol izquierdo.

            Returns:
                bool: True si existe hijo izquierdo, False en caso contrario.
            """
            return self.izquierdo is not None

        def tieneDerecho(self) -> bool:
            """
            Indica si el nodo posee subárbol derecho.

            Returns:
                bool: True si existe hijo derecho, False en caso contrario.
            """
            return self.derecho is not None

        def grado(self) -> int:
            """
            Retorna la cantidad de hijos (0, 1 o 2).

            Returns:
                int: número de hijos del nodo.
            """
            return int(self.tieneIzquierdo()) + int(self.tieneDerecho())

        def esHoja(self) -> bool:
            """
            Comprueba si el nodo es hoja.

            Returns:
                bool: True si no posee hijos; False en otro caso.
            """
            return not self.tieneIzquierdo() and not self.tieneDerecho()

        # ---------------- 2. Recorridos -------------------------
        def imprimirPreOrdenNodo(self) -> None:
            """
            Imprime el subárbol en Pre-Orden (N–Izq–Der),
            comenzando por este nodo.
            """
            print(self.dato)
            if self.tieneIzquierdo():
                self.izquierdo.imprimirPreOrdenNodo()
            if self.tieneDerecho():
                self.derecho.imprimirPreOrdenNodo()

        def imprimirInOrdenNodo(self) -> None:
            """
            Imprime el subárbol en In-Orden (Izq–N–Der),
            comenzando por este nodo.  Para un ABB produce
            los valores ordenados de menor a mayor.
            """
            if self.tieneIzquierdo():
                self.izquierdo.imprimirInOrdenNodo()
            print(self.dato)
            if self.tieneDerecho():
                self.derecho.imprimirInOrdenNodo()

        def imprimirPostOrdenNodo(self) -> None:
            """
            Imprime el subárbol en Post-Orden (Izq–Der–N),
            comenzando por este nodo.
            """
            if self.tieneIzquierdo():
                self.izquierdo.imprimirPostOrdenNodo()
            if self.tieneDerecho():
                self.derecho.imprimirPostOrdenNodo()
            print(self.dato)

        # ---------------- 3. Inserción --------------------------
        def insertarNodo(self, nuevo: 'ABB.__NodoArbol') -> None:
            """
            Inserta un nodo en el subárbol que cuelga de este nodo.

            Args:
                nuevo (ABB.__NodoArbol): nodo previamente creado.
            """
            # Descendemos por la rama correspondiente
            if nuevo.dato < self.dato:
                if self.tieneIzquierdo():
                    self.izquierdo.insertarNodo(nuevo)
                else:
                    self.izquierdo = nuevo
            elif nuevo.dato > self.dato:
                if self.tieneDerecho():
                    self.derecho.insertarNodo(nuevo)
                else:
                    self.derecho = nuevo
            # Si son iguales no se inserta (no se permiten duplicados).

        # ---------------- 4. Búsqueda ---------------------------
        def buscarNodo(self, datoBusc: int) -> bool:
            """
            Busca la presencia de un valor en el subárbol.

            Args:
                datoBusc (int): valor a ubicar.

            Returns:
                bool: True si el dato se encuentra, False en otro caso.
            """
            if datoBusc == self.dato:
                return True
            if datoBusc < self.dato and self.tieneIzquierdo():
                return self.izquierdo.buscarNodo(datoBusc)
            if datoBusc > self.dato and self.tieneDerecho():
                return self.derecho.buscarNodo(datoBusc)
            return False

        # ---------------- 5. Peso -------------------------------
        def pesoNodo(self) -> int:
            """
            Calcula la cantidad de nodos en el subárbol.

            Returns:
                int: número de nodos incluido este.
            """
            cant = 1
            if self.tieneIzquierdo():
                cant += self.izquierdo.pesoNodo()
            if self.tieneDerecho():
                cant += self.derecho.pesoNodo()
            return cant

        # ---------------- 6. Altura -----------------------------
        def alturaNodo(self) -> int:
            """
            Altura del subárbol cuya raíz es este nodo.

            Returns:
                int: número de aristas hasta la hoja más lejana
                     (una hoja tiene altura 0).
            """
            if self.esHoja():
                return 0
            izq = self.izquierdo.alturaNodo() if self.tieneIzquierdo() else 0
            der = self.derecho.alturaNodo() if self.tieneDerecho() else 0
            return 1 + max(izq, der)

        # -------------- 7. Nivel de un dato ---------------------
        def buscarNivelNodo(self, datoBusc: int, nivelActual: int = 0) -> int | None:
            """
            Devuelve la profundidad a la que se halla un dato.

            Args:
                datoBusc (int): valor buscado.
                nivelActual (int): parámetro recursivo (no usar).

            Returns:
                int | None: nivel (0 = raíz del subárbol) o None si no existe.
            """
            if datoBusc == self.dato:
                return nivelActual
            if datoBusc < self.dato and self.tieneIzquierdo():
                return self.izquierdo.buscarNivelNodo(datoBusc, nivelActual + 1)
            if datoBusc > self.dato and self.tieneDerecho():
                return self.derecho.buscarNivelNodo(datoBusc, nivelActual + 1)
            return None

        # -------------- 8. Mínimo y máximo ----------------------
        def minimoNodo(self) -> 'ABB.__NodoArbol':
            """
            Nodo con el valor mínimo del subárbol.

            Returns:
                ABB.__NodoArbol: referencia al nodo mínimo.
            """
            return self.izquierdo.minimoNodo() if self.tieneIzquierdo() else self

        def maximoNodo(self) -> 'ABB.__NodoArbol':
            """
            Nodo con el valor máximo del subárbol.

            Returns:
                ABB.__NodoArbol: referencia al nodo máximo.
            """
            return self.derecho.maximoNodo() if self.tieneDerecho() else self

        # -------------- 9. Predecesor / Sucesor -----------------
        def predecesorNodo(self) -> 'ABB.__NodoArbol | None':
            """
            Devuelve el nodo con el mayor valor menor que self.dato.

            Returns:
                ABB.__NodoArbol | None: nodo predecesor o None si no existe.
            """
            return self.izquierdo.maximoNodo() if self.tieneIzquierdo() else None

        def sucesorNodo(self) -> 'ABB.__NodoArbol | None':
            """
            Devuelve el nodo con el menor valor mayor que self.dato.

            Returns:
                ABB.__NodoArbol | None: nodo sucesor o None si no existe.
            """
            return self.derecho.minimoNodo() if self.tieneDerecho() else None

        # ------------- 10. Buscar padre y lado -----------------
        def buscaPadreYladoNodo(
                self, datoBusc: int
        ) -> tuple['ABB.__NodoArbol | None', str | None]:
            """
            Localiza el padre inmediato de un dato y el lado correspondiente.

            Args:
                datoBusc (int): valor del hijo buscado.

            Returns:
                tuple[ABB.__NodoArbol | None, str | None]:
                    (padre, "izq"/"der") o (None, None) si no se encontró.
            """
            if datoBusc < self.dato and self.tieneIzquierdo():
                if self.izquierdo.dato == datoBusc:
                    return self, "izq"
                return self.izquierdo.buscaPadreYladoNodo(datoBusc)
            if datoBusc > self.dato and self.tieneDerecho():
                if self.derecho.dato == datoBusc:
                    return self, "der"
                return self.derecho.buscaPadreYladoNodo(datoBusc)
            return None, None

        # ------------- 11. Eliminación --------------------------
        def eliminarNodo(self, datoDel: int) -> None:
            """
            Elimina un nodo (no la raíz del ABB completo) del subárbol.

            Args:
                datoDel (int): dato a eliminar (se asume existe).
            """
            nodoPadre, ladoHijo = self.buscaPadreYladoNodo(datoDel)
            if nodoPadre is None:
                return  # no se encontró (caso de seguridad)

            # Nodo que se quitará del árbol
            nodoAeliminar = (
                nodoPadre.izquierdo if ladoHijo == "izq" else nodoPadre.derecho
            )

            # Reemplazo: predecesor o sucesor
            reemplazo = nodoAeliminar.predecesorNodo() or nodoAeliminar.sucesorNodo()

            # Si hay reemplazo, también hay que quitarlo de su posición anterior
            if reemplazo is not None:
                nodoPadre.eliminarNodo(reemplazo.dato)
                reemplazo.izquierdo = nodoAeliminar.izquierdo
                reemplazo.derecho = nodoAeliminar.derecho

            # Conectar el padre con el reemplazo
            if ladoHijo == "izq":
                nodoPadre.izquierdo = reemplazo
            else:
                nodoPadre.derecho = reemplazo

        # ------------- 12. Cantidad de hojas --------------------
        def cantidadHojasNodo(self) -> int:
            """
            Cuenta las hojas (nodos sin hijos) en el subárbol.

            Returns:
                int: número de hojas.
            """
            if self.esHoja():
                return 1
            cant = 0
            if self.tieneIzquierdo():
                cant += self.izquierdo.cantidadHojasNodo()
            if self.tieneDerecho():
                cant += self.derecho.cantidadHojasNodo()
            return cant

        # ------------- 13. Mostrar nivel N ----------------------
        def mostrarNivelNodo(self, buscado: int, actual: int = 0) -> None:
            """
            Imprime los valores que se encuentran en el nivel `buscado`
            dentro del subárbol.

            Args:
                buscado (int): nivel objetivo (raíz = 0).
                actual  (int): nivel actual (parámetro recursivo).
            """
            if actual == buscado:
                print(self.dato)
                return
            if self.tieneIzquierdo():
                self.izquierdo.mostrarNivelNodo(buscado, actual + 1)
            if self.tieneDerecho():
                self.derecho.mostrarNivelNodo(buscado, actual + 1)

        # ------------- 14. Frontera -----------------------------
        def imprimirFrontera(self) -> None:
            """
            Imprime de izquierda a derecha los valores de todas las hojas
            del subárbol.
            """
            if self.esHoja():
                print(self.dato)
            else:
                if self.tieneIzquierdo():
                    self.izquierdo.imprimirFrontera()
                if self.tieneDerecho():
                    self.derecho.imprimirFrontera()

        # ------------- 15. Lista pares ordenada -----------------
        def listaOrdenadaParesNodos(self) -> list[int]:
            """
            Devuelve los datos pares del subárbol en orden creciente.

            Returns:
                list[int]: lista (orden in-orden) de valores pares.
            """
            lista = []
            if self.tieneIzquierdo():
                lista += self.izquierdo.listaOrdenadaParesNodos()
            if self.dato % 2 == 0:
                lista.append(self.dato)
            if self.tieneDerecho():
                lista += self.derecho.listaOrdenadaParesNodos()
            return lista

        # ------------- 16. Rotar árbol --------------------------
        def rotarNodo(self) -> None:
            """
            Intercambia recursivamente los subárboles izquierdo y derecho,
            dejando el ABB “invertido”.
            """
            self.izquierdo, self.derecho = self.derecho, self.izquierdo
            if self.tieneIzquierdo():
                self.izquierdo.rotarNodo()
            if self.tieneDerecho():
                self.derecho.rotarNodo()

        # ------------- 17. Cantidad nodos en nivel --------------
        def cantidadNodosEnNivelNodo(self, buscado: int, actual: int = 0) -> int:
            """
            Cuenta los nodos ubicados exactamente en el nivel `buscado`.

            Args:
                buscado (int): nivel deseado.
                actual  (int): nivel actual (parámetro recursivo).

            Returns:
                int: cantidad de nodos en ese nivel.
            """
            if actual == buscado:
                return 1
            cant = 0
            if self.tieneIzquierdo():
                cant += self.izquierdo.cantidadNodosEnNivelNodo(buscado, actual + 1)
            if self.tieneDerecho():
                cant += self.derecho.cantidadNodosEnNivelNodo(buscado, actual + 1)
            return cant

    # ─────────────────────────────────────────────────────────
    # MÉTODOS PÚBLICOS DE ABB  (visible para el usuario final)
    # ─────────────────────────────────────────────────────────
    # Constructor y utilitarios
    def __init__(self) -> None:
        """Crea un ABB vacío."""
        self.__raiz: 'ABB.__NodoArbol | None' = None

    def estaVacio(self) -> bool:
        """
        Indica si el árbol está vacío.

        Returns:
            bool: True cuando no hay nodos; False si contiene al menos uno.
        """
        return self.__raiz is None

    def vaciar(self) -> None:
        """Elimina todos los elementos del ABB."""
        self.__raiz = None

    def clonar(self) -> 'ABB':
        """
        Crea una copia profunda del árbol.

        Returns:
            ABB: nuevo ABB independiente.
        """
        return copy.deepcopy(self)

    # Inserción y búsqueda
    def insertar(self, dato: int) -> None:
        """
        Inserta un entero en el árbol.

        Args:
            dato (int): valor a agregar.  Si ya existe, no se inserta.
        """
        nuevo = ABB.__NodoArbol(dato)
        if self.estaVacio():
            self.__raiz = nuevo
        else:
            self.__raiz.insertarNodo(nuevo)

    def buscar(self, dato: int) -> bool:
        """
        Verifica la existencia de un valor.

        Args:
            dato (int): dato buscado.

        Returns:
            bool: True si está presente, False si no.
        """
        return False if self.estaVacio() else self.__raiz.buscarNodo(dato)

    # Métricas generales
    def peso(self) -> int:
        """
        Número total de nodos del árbol.

        Returns:
            int: cardinalidad del ABB.
        """
        return 0 if self.estaVacio() else self.__raiz.pesoNodo()

    def altura(self) -> int:
        """
        Altura del árbol (altura de la raíz).

        Returns:
            int: 0 para un árbol de un solo nodo; -1 si está vacío.
        """
        if self.estaVacio():
            return -1
        return self.__raiz.alturaNodo()

    # Recorridos (salida por pantalla)
    def imprimirPreOrden(self) -> None:
        """Imprime todos los valores en recorrido Pre-Orden."""
        if not self.estaVacio():
            self.__raiz.imprimirPreOrdenNodo()

    def imprimirInOrden(self) -> None:
        """Imprime todos los valores en recorrido In-Orden (ordenados)."""
        if not self.estaVacio():
            self.__raiz.imprimirInOrdenNodo()

    def imprimirPostOrden(self) -> None:
        """Imprime todos los valores en recorrido Post-Orden."""
        if not self.estaVacio():
            self.__raiz.imprimirPostOrdenNodo()

    # Otras consultas
    def buscarNivel(self, dato: int) -> int | None:
        """
        Devuelve la profundidad a la que se halla un valor.

        Args:
            dato (int): valor buscado.

        Returns:
            int | None: nivel (0 = raíz) o None si no existe.
        """
        return None if self.estaVacio() else self.__raiz.buscarNivelNodo(dato)

    def minimo(self) -> int | None:
        """
        Valor mínimo del ABB.

        Returns:
            int | None: dato mínimo o None si el árbol está vacío.
        """
        return None if self.estaVacio() else self.__raiz.minimoNodo().dato

    def maximo(self) -> int | None:
        """
        Valor máximo del ABB.

        Returns:
            int | None: dato máximo o None si el árbol está vacío.
        """
        return None if self.estaVacio() else self.__raiz.maximoNodo().dato

    # Eliminación
    def eliminar(self, datoDel: int) -> None:
        """
        Elimina un nodo que contenga el dato indicado.

        Args:
            datoDel (int): valor a eliminar.  Si no existe, no hace nada.
        """
        if self.estaVacio():
            return

        # Caso especial: eliminar la raíz
        if self.__raiz.dato == datoDel:
            reemplazo = self.__raiz.predecesorNodo() or self.__raiz.sucesorNodo()
            if reemplazo is not None:
                self.__raiz.eliminarNodo(reemplazo.dato)
                reemplazo.izquierdo = self.__raiz.izquierdo
                reemplazo.derecho = self.__raiz.derecho
            self.__raiz = reemplazo
        else:
            self.__raiz.eliminarNodo(datoDel)

    # Métodos de apoyo / depuración
    def buscaPadreYlado(self, datoBusc: int) -> tuple[int | None, str | None]:
        """
        Devuelve el dato del padre y el lado ("izq"/"der") de un hijo buscado.

        Args:
            datoBusc (int): dato del hijo objetivo.

        Returns:
            tuple[int | None, str | None]:
                (datoPadre, lado) o (None, None) si no se encuentra.
        """
        if self.estaVacio():
            return None, None
        nodo, lado = self.__raiz.buscaPadreYladoNodo(datoBusc)
        return (nodo.dato if nodo else None, lado)

    def testPredSuc(self) -> None:
        """
        Muestra en pantalla el predecesor y sucesor de la raíz.
        Útil para pruebas manuales.
        """
        if self.estaVacio():
            print("Árbol vacío")
            return
        pred = self.__raiz.predecesorNodo()
        suc = self.__raiz.sucesorNodo()
        print("Predecesor:", pred.dato if pred else None)
        print("Sucesor   :", suc.dato if suc else None)

    # ----------------- Ejercicios extra ------------------------
    def cantidadHojas(self) -> int:
        """
        Cuenta la cantidad de hojas del ABB.

        Returns:
            int: número de hojas.
        """
        return 0 if self.estaVacio() else self.__raiz.cantidadHojasNodo()

    def mostrarNivel(self, n: int) -> None:
        """
        Imprime todos los valores ubicados en el nivel `n`.

        Args:
            n (int): nivel deseado (0 = raíz).
        """
        if not self.estaVacio():
            self.__raiz.mostrarNivelNodo(n)

    def imprimirFrontera(self) -> None:
        """Imprime la secuencia de hojas, de izquierda a derecha."""
        if not self.estaVacio():
            self.__raiz.imprimirFrontera()

    def listaOrdenadaPares(self) -> list[int]:
        """
        Obtiene los datos pares existentes en el árbol, ordenados de menor a mayor.

        Returns:
            list[int]: lista ascendente de valores pares.
        """
        return [] if self.estaVacio() else self.__raiz.listaOrdenadaParesNodos()

    def rotar(self) -> None:
        """
        Rota (invierte) recursivamente todo el árbol, de modo que los valores
        menores queden a la derecha y los mayores a la izquierda.
        """
        if not self.estaVacio():
            self.__raiz.rotarNodo()

    def cantidadNodosEnNivel(self, n: int) -> int:
        """
        Cantidad de nodos que existen exactamente en el nivel `n`.

        Args:
            n (int): nivel sobre el que se quiere contar.

        Returns:
            int: número de nodos en ese nivel.
        """
        return 0 if self.estaVacio() else self.__raiz.cantidadNodosEnNivelNodo(n)
