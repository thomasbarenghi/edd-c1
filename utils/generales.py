def validar_valor(valor, opciones) -> bool:
    """
    Devuelve True si el valor está dentro de las opciones permitidas.

    Ejemplos:
    validar_valor("a", ["a", "b", "c"]) -> True
    validar_valor(2, {1, 2, 3}) -> True
    validar_valor("x", ("a", "b", "c")) -> False
    """
    return valor in opciones


def es_par(n):
    return n % 2 == 0


def uno_si_cero_sino(condicion):
    return 1 if condicion else 0
