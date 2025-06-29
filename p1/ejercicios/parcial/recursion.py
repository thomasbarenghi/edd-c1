from utils.generales import uno_si_cero_sino, es_par
from utils.utils_listas import sin_el_primero, invertir


# Ejercicio 1

# Escribir la función recursiva posicionCima(arreglo), que retorna la posición de la cima de un arreglo
# que tiene los números ordenados de manera creciente hasta la cima (el número más grande) 
# y luego de forma decreciente.
# Asumir que no hay números repetidos y que el arreglo no está vacío.

# arr1 = [1, 3, 4, 5, 7, 18, 21, 23, 22, 19]
# posicionCima(arr1) debe devolver la posición de 23, que es 7.

def posicion_clima(arr):
    if len(arr) <= 1 or arr[0] > arr[1]:
        return 0

    return 1 + posicion_clima(arr[1:])


print(posicion_clima([1, 3, 4, 5, 7, 18, 21, 23, 22, 19]))


# Ejercicio 3
# Implementar la función recursiva "inversionRecursiva" que recibe por parámetro un string
# y retorna un nuevo string conteniendo el string de entrada invertido.

# Por ejemplo:
# Si str1 = "hola"
# str2 = inversionRecursiva(str1)
# Entonces, str2 = "aloh"

def inversion_recursiva(txt: str):
    if len(txt) <= 1:
        return txt

    return txt[-1] + inversion_recursiva(txt[:-1])


print(inversion_recursiva("HOLA"))


# Ejercicio 5
# Escribir la función recursiva "sonIguales" que recibe dos strings del mismo tamaño (no vacías)
# y retorna True si son iguales y False en caso contrario.

def son_iguales(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    if len(str1) == 0 or len(str2) == 0:
        return True

    equals = str1[0] == str2[0]

    return equals and son_iguales(str1[1:], str2[1:])


print(son_iguales("HOLA", "HOLA"))


# Ejercicio 7
# Escribir las funciones que considere necesarias para implementar un algoritmo recursivo
# que cuente la cantidad de números pares y otro algoritmo recursivo para contar la cantidad
# de números mayores que 10 en un arreglo de números enteros.
# Por último, implementar la función masParesQue10(arreglo), que devuelve True cuando el arreglo
# tiene más números pares que números mayores que 10. Esta última función no necesita ser recursiva.

# Las soluciones que NO sean recursivas no serán tomadas en cuenta.

# Ejemplo:
# Si arr1 = [5, 10, 9, 8, 13, 21] => masParesQue10(arr1) devuelve False,
# porque arr1 tiene 2 números mayores que 10 y 2 números pares.
# Si arr2 = [5, 10, 24, 9, 8, 6, 21] => masParesQue10(arr2) devuelve True,
# porque arr2 tiene 4 números pares y solamente 2 números mayores que 10.

# Ayuda: Se puede asumir que ya se tiene la función esPar(n) que devuelve verdadero cuando n es par.

# Función esPar(n) que devuelve True si n es par, de lo contrario devuelve False.

def cantidad_pares(nums):
    if len(nums) <= 1:
        return uno_si_cero_sino(es_par(nums[0]))

    val = uno_si_cero_sino(es_par(nums[0]))

    return val + cantidad_pares(nums[1:])


def es_mayor_que_diez(num):
    return num > 10


def cantidad_mayores_que_diez(nums):
    if len(nums) <= 1:
        return uno_si_cero_sino(es_mayor_que_diez(nums[0]))

    val = uno_si_cero_sino(es_mayor_que_diez(nums[0]))

    return val + cantidad_mayores_que_diez(nums[1:])


def mas_pares_que_diez(arr):
    return cantidad_pares(arr) > cantidad_mayores_que_diez(arr)


print(cantidad_pares([1, 1, 1, 1, 2, 2, 2, 1]))
print(cantidad_mayores_que_diez([11, 11, 11, 8, 8, 11]))
print(mas_pares_que_diez([11, 11, 11, 8, 8, 8, 8, 8]))


# Ejercicio 9
# Escribir la función recursiva estaIncluido(arreglo1, arreglo2), que retorna verdadero si el arreglo1
# está incluido al inicio o al final del arreglo2.
# Tener en cuenta que un arreglo vacío siempre está incluido en otro (vacío o no) y que un arreglo vacío
# solo puede incluir a otro vacío.
# Soluciones que NO sean recursivas NO serán tenidas en cuenta.

# Ejemplo:
# Si:
# arr1 = [2, 5, 1], arr2 = [1, 9, 3, 4, 2, 5, 1] , arr3 = [2, 5, 1, 6 ,1, 8, 5] , arr4 = [4, 3, 2, 5, 1, 8, 2]
# estaIncluido(arr1, arr2) => True
# estaIncluido(arr1, arr3) => True
# estaIncluido(arr1, arr4) => False

# Ayuda: Pueden utilizar dos funciones auxiliares, al menos una tiene que ser recursiva.

def empieza_con(arr, prefix):
    if len(prefix) <= 1:
        return prefix[0] == arr[0]

    val = prefix[0] == arr[0]

    return val and empieza_con(sin_el_primero(arr), sin_el_primero(prefix))


def termina_con(arr, subfix):
    return empieza_con(invertir(arr), invertir(subfix))


def esta_incluido(arr1, arr2):
    if len(arr1) > len(arr2):
        return False

    if len(arr1) == 0:
        return True

    return empieza_con(arr2, arr1) or termina_con(arr2, arr1)


arr1 = [2, 5, 1]
arr2 = [1, 9, 3, 4, 2, 5, 1]
arr3 = [2, 5, 1, 6, 1, 8, 5]
arr4 = [4, 3, 2, 5, 1, 8, 2]

print(esta_incluido(arr1, arr2))
print(esta_incluido(arr1, arr3))
print(esta_incluido(arr1, arr4))
