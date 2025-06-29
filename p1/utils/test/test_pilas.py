import unittest

from utils.utils_pilas import *


class TestFuncionesPila(unittest.TestCase):

    def setUp(self):
        """Inicializa una pila de ejemplo para las pruebas."""
        self.pila = Pila()
        self.pila.apilar(1)
        self.pila.apilar(2)
        self.pila.apilar(3)
        self.pila.apilar(4)
        self.pila.apilar(5)  # Base [1, 2, 3, 4, 5] Cima

    def test_buscar(self):
        resultado = buscar(self.pila, lambda x: x == 3)
        self.assertEqual(3, resultado)

        resultado = buscar(self.pila, lambda x: x == 6)
        self.assertIsNone(resultado)
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_contiene(self):
        self.assertTrue(contiene(self.pila, 3))
        self.assertFalse(contiene(self.pila, 6))
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_filtrar(self):
        resultado = filtrar(self.pila, lambda x: x % 2 == 0)
        lista_resultado = resultado.a_lista()
        self.assertEqual(lista_resultado, [2, 4])
        self.assertEqual([1, 2, 3, 4, 5], a_lista(self.pila))
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_obtener_primeros_n_elementos(self):
        """Prueba la función obtener_n_elementos."""
        resultado = obtener_primeros_n_elementos(self.pila, 3)
        self.assertEqual(resultado, [3, 4, 5])
        resultado = obtener_primeros_n_elementos(self.pila, 10)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_obtener_ultimos_n_elementos(self):
        """Prueba la función obtener_ultimos_n_elementos."""
        resultado = obtener_ultimos_n_elementos(self.pila, 3)
        self.assertEqual(resultado, [1, 2, 3])
        resultado = obtener_ultimos_n_elementos(self.pila, 10)
        self.assertEqual(resultado, [1, 2, 3, 4, 5])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_mapear(self):
        """Prueba la función mapear."""
        resultado = mapear(self.pila, lambda x: x * 2)
        lista_resultado = resultado.a_lista()
        self.assertEqual(lista_resultado, [10, 8, 6, 4, 2])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_reducir(self):
        """Prueba la función reducir."""
        resultado = reducir(self.pila, lambda x, y: x + y, 0)
        self.assertEqual(resultado, 15)
        resultado = reducir(self.pila, lambda x, y: x * y, 1)
        self.assertEqual(resultado, 120)
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_invertir(self):
        """Prueba la función invertir."""
        resultado = invertir(self.pila)
        lista_resultado = resultado.a_lista()
        self.assertEqual(lista_resultado, [5, 4, 3, 2, 1])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_a_lista(self):
        """Prueba la función a_lista."""
        lista_resultado = a_lista(self.pila)
        self.assertEqual(lista_resultado, [1, 2, 3, 4, 5])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_mover_base_a_cima(self):
        """Prueba la función mover_base_a_cima."""
        resultado = mover_base_a_cima(self.pila)
        lista_resultado = resultado.a_lista()
        self.assertEqual(lista_resultado, [2, 3, 4, 5, 1])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_mover_cima_a_base(self):
        """Prueba la función mover_cima_a_base."""
        resultado = mover_cima_a_base(self.pila)
        lista_resultado = resultado.a_lista()
        self.assertEqual(lista_resultado, [5, 1, 2, 3, 4])
        self.assertEqual(self.pila.a_lista(), [1, 2, 3, 4, 5])

    def test_eliminar_elemento(self):
        """Prueba la función eliminar_elemento."""
        resultado = eliminar_elemento(self.pila, 3)
        self.assertTrue(resultado)
        lista_resultado = self.pila.a_lista()
        self.assertEqual(lista_resultado, [1, 2, 4, 5])

        resultado = eliminar_elemento(self.pila, 6)
        self.assertFalse(resultado)

        self.assertEqual(self.pila.a_lista(), [1, 2, 4, 5])

    def test_eliminar_base(self):
        """Prueba la función eliminar_base."""
        resultado = eliminar_base(self.pila)
        lista_resultado = resultado.a_lista()
        self.assertEqual(lista_resultado, [2, 3, 4, 5])

    def test_insertar_ordenado(self):
        """Prueba la función insertar_ordenado."""
        insertar_ordenado(self.pila, 6)
        lista_resultado = self.pila.a_lista()
        self.assertEqual(lista_resultado, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
