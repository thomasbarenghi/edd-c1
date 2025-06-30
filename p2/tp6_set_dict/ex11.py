from p2.diccionario import Diccionario


def posibles_pares(dic: Diccionario):
    res = []
    for key_int in dic.keys():  # La clave del diccionario es un entero
        value_list_int = dic[key_int]

        for value_int in value_list_int:  # El valor del diccionario es una lista de enteros
            res.append((key_int, value_int))

    return res


# Probar

diccionario = Diccionario()
diccionario.insert(1, [2, 3])
diccionario.insert(2, [3, 4])
diccionario.insert(3, [4, 5])
diccionario.insert(4, [5, 6])
diccionario.insert(5, [6, 7])

print(posibles_pares(diccionario))
