from p1.estructuras.pila import Pila
from p1.utils.generales import validar_tipo
from p1.utils.utils_colas import eliminar_elemento
from p1.utils.utils_listas import reducir, buscar


class Juzgado:
    def __init__(self, numero, max_criticos=50):
        self.__urgentes = Pila()
        self.__normales = Pila()
        self.__numero = numero
        self.__max_criticos = max_criticos

    def ingresar_expediente(self, expediente):
        if expediente.get_prioridad() == "Urgente":
            self.__urgentes.apilar(expediente)
        else:
            self.__normales.apilar(expediente)

    def primer_expediente_a_tratar(self):
        if not self.__urgentes.esta_vacia():
            return self.__urgentes.cima()
        elif not self.__normales.esta_vacia():
            return self.__normales.cima()
        return None

    def es_critico(self):
        return self.__urgentes.tamaño() > self.__max_criticos or self.__normales.tamaño() > self.__max_criticos

    def en_juicio(self):
        cb = lambda acu, act: acu + 1 if act.get_estado() == "Juicio" else acu
        cantidad_normales = reducir(self.__normales, cb, 0)
        cantidad_urgentes = reducir(self.__urgentes, cb, 0)
        return cantidad_normales + cantidad_urgentes

    def sacar_expediente(self, id):
        cb = lambda x: x.get_id() == id
        exp_normal = buscar(self.__normales, cb)
        exp_urgente = buscar(self.__urgentes, cb)

        if exp_urgente != None:
            eliminar_elemento(self.__urgentes, exp_urgente)
            return exp_urgente
        elif exp_normal != None:
            eliminar_elemento(self.__normales, exp_normal)
            return exp_normal

        return None


class Expediente:
    def __init__(self, id, prioridad, estado):
        self.__id = id
        self.__prioridad = validar_tipo(prioridad, ["Urgente", "Normal"])
        self.__estado = validar_tipo(estado, ["Juicio", "Investigacion"])

    def __str__(self):
        return f"Expediente({self.__id}, {self.__prioridad}, {self.__estado})"

    def get_estado(self):
        return self.__estado

    def get_id(self):
        return self.__id

    def get_prioridad(self):
        return self.__prioridad


j = Juzgado(1, 1)

e1 = Expediente(101, "Urgente", "Juicio")
e2 = Expediente(102, "Normal", "Investigacion")
e3 = Expediente(103, "Urgente", "Juicio")

j.ingresar_expediente(e1)
j.ingresar_expediente(e2)
j.ingresar_expediente(e3)

print("Primer expediente a tratar:", j.primer_expediente_a_tratar())
print("¿Es crítico?:", j.es_critico())
print("Cantidad en Juicio:", j.en_juicio())

print("Sacando expediente 101:", j.sacar_expediente(101))
print("Primer expediente a tratar ahora:", j.primer_expediente_a_tratar())
