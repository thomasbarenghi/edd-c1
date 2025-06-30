# Escribir una función listaToDic que recibe una lista con chirimbolos y devuelve un diccionario con cada chirimbolo como clave y como significado una matriz de nxn donde n es la cantidad de veces que aparece el chirimbolo en la lista. La matriz se debe llenar con el chirimbolo de la clave. Se debe resolver usando las operaciones del TDA diccionario que vimos en clase, sin violar el encapsulamiento ni utilizando estructuras auxiliares. Si es necesario definir funciones auxiliar
# es.
from p1.utils.utils_listas import contar
from p2.diccionario import Diccionario


def lista_a_dic(lista):
    res = Diccionario()
    for elemento in lista:
        cantidad = contar(lista, lambda x, elem=elemento: x == elem)
        res.insert(elemento, [elemento] * cantidad)

    return res


listaTest = ["#", "*", "#", "*", "*", "#", "!", "!", "*", "#"]

diccionario = lista_a_dic(listaTest)
print(diccionario)
