import copy


class Cola:
    def __init__(self):
        self.__cola = []

    def __repr__(self) -> str:
        return f"<-{self.__cola}<-"

    def esta_vacia(self) -> bool:
        return len(self.__cola) == 0

    def encolar(self, valor) -> None:
        self.__cola.append(valor)

    def desencolar(self):
        if not self.esta_vacia():
            return self.__cola.pop(0)
        else:
            raise Exception("La cola está vacía")

    def frente(self):
        if not self.esta_vacia():
            return self.__cola[0]
        else:
            raise Exception("La cola está vacía")

    def limpiar(self) -> None:
        self.__cola = []

    def tamaño(self):
        return len(self.__cola)

    def clonar(self):
        return copy.deepcopy(self)
