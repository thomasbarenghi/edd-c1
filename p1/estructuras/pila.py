import copy


class Pila:
    def __init__(self):
        self.__pila = []

    def __repr__(self) -> str:
        return f"{self.__pila}<->"

    def esta_vacia(self) -> bool:
        return len(self.__pila) == 0

    def apilar(self, valor: int) -> None:
        self.__pila.append(valor)

    def desapilar(self) -> int:
        if not self.esta_vacia():
            return self.__pila.pop()
        else:
            raise Exception("La pila está vacía")

    def cima(self) -> int:
        if not self.esta_vacia():
            return self.__pila[-1]
        else:
            raise Exception("La pila está vacía")

    def limpiar(self) -> None:
        self.__pila = []

    def tamaño(self) -> int:
        return len(self.__pila)

    def clonar(self):
        return copy.deepcopy(self)

    def a_lista(self):
        return self.__pila.copy()
