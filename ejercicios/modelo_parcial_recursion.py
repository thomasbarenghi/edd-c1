def igual_al_proximo(actual, proximo):
    return actual == proximo


def tiene_repetidos(lista):
    if len(lista) <= 2:
        return igual_al_proximo(lista[0], lista[1])

    condicion = igual_al_proximo(lista[0], lista[1])

    return condicion or tiene_repetidos(lista[1:])


print(tiene_repetidos([1, 2, 2, 3, 4, 5, 5]))
print(tiene_repetidos([1, 2, 3, 4, 5]))
