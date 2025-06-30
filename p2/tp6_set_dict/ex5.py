# UTILIDAD
from p2.diccionario import Diccionario


def sin_los_repetidos_dic(lista):
    """
    Retorna un diccionario sin los elementos repetidos.
    Las claves son los elementos únicos y los valores son None.
    """
    return Diccionario(lista, [None] * len(lista))


print(sin_los_repetidos_dic(["feliz", "contento", "alegre", "feliz", "alegre"]))
