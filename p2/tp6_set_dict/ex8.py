# UTILIDAD
from p2.diccionario import Diccionario

alumnos_materias = Diccionario()


def administrar_materias(alumnos_materias_dic: Diccionario, alumno: str, materia: str):
    if not contains_value(alumnos_materias_dic, alumno):
        alumnos_materias_dic.insert(alumno, [materia])
    else:
        agregar_si_lista(alumnos_materias_dic[alumno], materia, materia not in alumnos_materias_dic[alumno])


def agregar_si_lista(lista: list, elemento: any, condicion: any):
    if condicion:
        lista.append(elemento)


def contains_value(dic, value):
    return value in dic.values()


# Probar

alumnos_materias.insert("Juan", ["Matemáticas"])
administrar_materias(alumnos_materias, "Juan", "Física")
administrar_materias(alumnos_materias, "Ana", "Química")
print(alumnos_materias)
