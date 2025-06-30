from p2.diccionario import Diccionario


def list_a_dic(list):
    res = Diccionario()

    for tupla in list:
        v1 = tupla[0]
        v2 = tupla[1]

        if v1 in res.keys():
            res[v1].append(v2)
        else:
            res.insert(v1, [v2])

    return res


# Probar

tuplas = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]

diccionario = list_a_dic(tuplas)

print(diccionario)
