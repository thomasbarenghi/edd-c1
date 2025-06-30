from p1.utils.utils_listas import reducir
from p2.diccionario import Diccionario


def promedios(materias, notas):
    dic_materia_notas = Diccionario()
    acumulados_dic = acumular_para_promedio(materias, notas)

    for materia_str in acumulados_dic.keys():
        acumulados_list_int = acumulados_dic[materia_str]
        reductor = lambda v1, v2: v1 / v2
        dic_materia_notas[materia_str] = reducir(acumulados_list_int, reductor)

    return dic_materia_notas


def acumular_para_promedio(lista1, lista2) -> Diccionario:
    acumulados_dic = Diccionario()

    for i, clave in enumerate(lista1):
        valor_actual_int = lista2[i]

        if clave in acumulados_dic:
            acumulados_dic[clave][0] += valor_actual_int
            acumulados_dic[clave][1] += 1
        else:
            acumulados_dic.insert(clave, [valor_actual_int, 1])

    return acumulados_dic


materias = ["Matemáticas", "Física", "Química", "Matemáticas", "Física"]
notas = [8, 7, 9, 6, 10]

dic_promedios = promedios(materias, notas)
print(dic_promedios)
