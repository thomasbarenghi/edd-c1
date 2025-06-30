import copy as cp

class Diccionario:
    """
    Representa un diccionario personalizado que almacena pares clave-valor usando un conjunto de tuplas internas.
    Permite operaciones similares a un diccionario de Python: inserción, eliminación, acceso, clonación, etc.
    """

    class __TuplaDic:
        """
        Tupla privada que representa un par clave-valor.
        """
        def __init__(self, key, value):
            self.__data = (key, value)

        def __repr__(self):
            return str(self.__data)

        def __eq__(self, key):
            return self.__data[0] == key

        def __hash__(self):
            return hash(self.__data[0])

        def get_key(self):
            """
            Retorna la clave del par.
            """
            return self.__data[0]

        def get_value(self):
            """
            Retorna el valor del par.
            """
            return self.__data[1]

    def __init__(self, keys=None, values=None):
        """
        Inicializa un diccionario opcionalmente con listas de claves y valores.
        Lanza una excepción si las listas no tienen la misma longitud.
        """
        self.__diccionario = set()
        if keys is not None:
            if len(keys) == len(values):
                for i in range(len(keys)):
                    self[keys[i]] = values[i]
            else:
                raise Exception("Las listas de pares clave-significado deben tener la misma cantidad")

    def __repr__(self):
        """
        Representación del diccionario como string.
        """
        return str(self.__diccionario)

    def __setitem__(self, key=None, value=None):
        """
        Asigna un valor a una clave. Si la clave ya existe, la reemplaza.
        """
        if key is not None:
            if key in self:
                self.__diccionario.remove(key)
            self.__diccionario.add(Diccionario.__TuplaDic(key, value))

    def insert(self, key=None, value=None):
        """
        Inserta un nuevo par clave-valor. No modifica el valor si la clave ya existe.
        """
        if key is not None:
            self.__diccionario.add(Diccionario.__TuplaDic(key, value))

    def remove(self, key):
        """
        Elimina un par clave-valor por clave. Si la clave no existe, no hace nada.
        Retorna el valor eliminado o None si no existía.
        """
        if key in self:
            valor = self[key]
            self.__diccionario.remove(key)
            return valor
        return None

    def clear(self):
        """
        Elimina todos los elementos del diccionario.
        """
        self.__diccionario = set()

    def clone(self):
        """
        Retorna una copia profunda del diccionario.
        """
        return cp.deepcopy(self)

    def __getitem__(self, key):
        """
        Accede al valor asociado a una clave usando la sintaxis de corchetes.
        Lanza una excepción si la clave no existe.
        """
        value = None
        flag = False
        for par_clave_valor in self.__diccionario:
            if par_clave_valor.get_key() == key:
                value = par_clave_valor.get_value()
                flag = True
        if flag:
            return value
        else:
            raise Exception("No existe la clave %s en el diccionario" % key)

    def get(self, key):
        """
        Retorna el valor asociado a una clave.
        Lanza una excepción si la clave no existe.
        """
        for par_clave_valor in self.__diccionario:
            if par_clave_valor.get_key() == key:
                return par_clave_valor.get_value()
        raise Exception(f"No existe la clave {key} en el diccionario")

    def keys(self):
        """
        Retorna una lista con todas las claves del diccionario.
        """
        return [x.get_key() for x in self.__diccionario]

    def values(self):
        """
        Retorna una lista con todos los valores del diccionario.
        """
        return [x.get_value() for x in self.__diccionario]

    def __contains__(self, key):
        """
        Permite usar el operador `in` para verificar si una clave está en el diccionario.
        """
        return key in self.__diccionario

    def len(self):
        """
        Retorna la cantidad de pares clave-valor almacenados en el diccionario.
        """
        return len(self.__diccionario)
