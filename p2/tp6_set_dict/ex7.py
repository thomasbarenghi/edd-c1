# UTILIDAD
from p2.diccionario import Diccionario


def mezclar_diccionarios(dic1: Diccionario, dic2: Diccionario):
    """
    Devuelve un nuevo Diccionario que mezcla d1 y d2.
    Si una clave está en ambos, se conserva el valor de d1.
    """
    res = dic1.clone()

    for clave in dic2.keys():
        res.insert(clave, dic2[clave])

    return res
