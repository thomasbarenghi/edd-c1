# UTILIDAD

def sin_los_repetidos(lista):
    """
    Retorna una lista sin los elementos repetidos.
    """
    return list(set(lista))


print(sin_los_repetidos(["feliz", "contento", "alegre", "feliz", "alegre"]))
