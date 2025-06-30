from p2.diccionario import Diccionario


# Ejercicio 1
def maximoPorClave(dic: Diccionario) -> Diccionario:
    res = Diccionario()

    for key in dic.keys():
        value_list = dic[key]
        res.insert(key, el_mas_grande(value_list))

    return res


def el_mas_grande(list):
    maximo = 0

    for elemento in list:
        if elemento > maximo:
            maximo = elemento

    return maximo


# probar

dicP1 = Diccionario()
dicP1.insert("a", [1, 2, 3])
dicP1.insert("b", [4, 5, 6])
dicP1.insert("c", [7, 8, 9])

print(maximoPorClave(dicP1))

# Ejercicio 2
