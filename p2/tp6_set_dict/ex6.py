# UTILIDAD
from p2.diccionario import Diccionario


def contador_apariciones(lista):
    res = Diccionario()

    for elemento in lista:
        if elemento in res:
            res[elemento] = res[elemento] + 1
        else:
            res.insert(elemento, 1)

    return res


inputList = [1, 3, 4, 2, 1, 3, 1, 4, 2, 5, 2]

print(contador_apariciones(inputList))
