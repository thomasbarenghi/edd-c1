import unittest

from utils.utils_listas import *


class TestListas(unittest.TestCase):

    def test_buscar(self):
        lista = ['manzana', 'banana', 'cereza']
        resultado = buscar(lista, lambda x: x == 'banana')
        self.assertEqual(resultado, 'banana')

        resultado_none = buscar(lista, lambda x: x == 'pera')
        self.assertIsNone(resultado_none)

    def test_todos(self):
        self.assertTrue(todos([2, 4, 6], lambda x: x % 2 == 0))
        self.assertFalse(todos([2, 3, 6], lambda x: x % 2 == 0))

    def test_alguno(self):
        self.assertTrue(alguno([1, 3, 4], lambda x: x % 2 == 0))
        self.assertFalse(alguno([1, 3, 5], lambda x: x % 2 == 0))

    def test_filtrar(self):
        lista = [1, 2, 3, 4, 5]
        filtrada = filtrar(lista, lambda x: x > 3)
        self.assertEqual(filtrada, [4, 5])

    def test_contar(self):
        lista = [1, 2, 3, 4, 5, 6]
        cantidad = contar(lista, lambda x: x % 2 == 0)
        self.assertEqual(cantidad, 3)

    def test_transformar(self):
        lista = [1, 2, 3]
        resultado = transformar(lista, lambda x: x * x)
        self.assertEqual(resultado, [1, 4, 9])

    def test_aplanar(self):
        lista_de_listas = [[1, 2], [3, 4], [5]]
        resultado = aplanar(lista_de_listas)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])

        # Caso con listas vacías
        resultado_vacio = aplanar([[], [], []])
        self.assertEqual(resultado_vacio, [])

    def test_unicos(self):
        lista = [1, 2, 2, 3, 1, 4]
        resultado = unicos(lista)
        self.assertEqual(resultado, [1, 2, 3, 4])

        # Lista vacía
        self.assertEqual(unicos([]), [])

    def test_reducir(self):
        suma = reducir([1, 2, 3], lambda acc, x: acc + x)
        self.assertEqual(suma, 6)
        # Con valor inicial
        suma_inicial = reducir([1, 2, 3], lambda acc, x: acc + x, 10)
        self.assertEqual(suma_inicial, 16)
        # Lista vacía sin valor inicial
        with self.assertRaises(Exception):
            reducir([], lambda a, b: a + b)

    def test_dividir_por(self):
        resultado = dividir_por([10, 20, 30], 10)
        self.assertEqual(resultado, [1.0, 2.0, 3.0])
        with self.assertRaises(ValueError):
            dividir_por([1, 2], 0)

    def test_rotar(self):
        lista = [1, 2, 3, 4]
        self.assertEqual(rotar(lista, 1), [4, 1, 2, 3])
        self.assertEqual(rotar(lista, -1), [2, 3, 4, 1])
        self.assertEqual(rotar(lista, 4), [1, 2, 3, 4])  # rotación completa

    def test_ordenar_por(self):
        lista = [{'nombre': 'Pedro'}, {'nombre': 'Ana'}]
        self.assertEqual(
            ordenar_por(lista, lambda x: x['nombre']),
            [{'nombre': 'Ana'}, {'nombre': 'Pedro'}]
        )
        self.assertEqual(
            ordenar_por(lista, lambda x: x['nombre'], descendente=True),
            [{'nombre': 'Pedro'}, {'nombre': 'Ana'}]
        )

    def test_invertir(self):
        lista = [1, 2, 3]
        resultado = invertir(lista)
        self.assertEqual(resultado, [3, 2, 1])

    def test_desde_hasta(self):
        lista = [10, 20, 30, 40, 50]
        self.assertEqual(desde_hasta(lista, 1, 4), [20, 30, 40])
        self.assertEqual(desde_hasta(lista, 0, 3), [10, 20, 30])

    def test_inicio_fin_paso(self):
        lista = [10, 20, 30, 40, 50, 60]
        self.assertEqual(inicio_fin_paso(lista, 0, 6, 2), [10, 30, 50])
        self.assertEqual(inicio_fin_paso(lista, 1, 5, 2), [20, 40])
        self.assertEqual(inicio_fin_paso(lista, 0, 6, 1), lista)

    def test_sin_el_ultimo(self):
        self.assertEqual(sin_el_ultimo([1, 2, 3]), [1, 2])
        self.assertEqual(sin_el_ultimo([1]), [])
        self.assertEqual(sin_el_ultimo([]), [])

    def test_sin_el_primero(self):
        self.assertEqual(sin_el_primero([1, 2, 3]), [2, 3])
        self.assertEqual(sin_el_primero([1]), [])
        self.assertEqual(sin_el_primero([]), [])


if __name__ == '__main__':
    unittest.main()
