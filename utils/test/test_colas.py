import unittest

from utils.utils_colas import *  # Asumiendo que tus funciones están en este módulo


class TestFuncionesCola(unittest.TestCase):

    def setUp(self):
        """Inicializa una cola de ejemplo para las pruebas."""
        self.cola = Cola()
        self.cola.encolar(1)
        self.cola.encolar(2)
        self.cola.encolar(3)
        self.cola.encolar(4)
        self.cola.encolar(5)  # Frente [1, 2, 3, 4, 5] Último

    # -----------------------------------------------
    # Categoría: Búsqueda
    # -----------------------------------------------
    def test_buscar(self):
        resultado = buscar(self.cola, 3)
        self.assertEqual(resultado, 3)

        resultado = buscar(self.cola, 6)
        self.assertIsNone(resultado)
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_contiene(self):
        self.assertTrue(contiene(self.cola, 3))
        self.assertFalse(contiene(self.cola, 6))
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_filtrar(self):
        cola_filtrada = filtrar(self.cola, lambda x: x > 2)
        self.assertEqual(a_lista(cola_filtrada), [3, 4, 5])
        # La cola original no debe modificarse
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_obtener_primeros_n_elementos(self):
        lista = obtener_primeros_n_elementos(self.cola, 3)
        self.assertEqual(lista, [1, 2, 3])
        # La cola no se modifica
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_obtener_ultimos_n_elementos(self):
        lista = obtener_ultimos_n_elementos(self.cola, 3)
        self.assertEqual(lista, [3, 4, 5])
        # La cola no se modifica
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    # -----------------------------------------------
    # Categoría: Transformación
    # -----------------------------------------------
    def test_mapear(self):
        cola_mapeada = mapear(self.cola, lambda x: x * 10)
        self.assertEqual(a_lista(cola_mapeada), [10, 20, 30, 40, 50])
        # La cola original no debe modificarse
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_reducir(self):
        suma = reducir(self.cola, lambda acc, x: acc + x, 0)
        self.assertEqual(suma, 15)
        # Sin valor inicial
        suma2 = reducir(self.cola, lambda acc, x: acc + x)
        self.assertEqual(suma2, 15)
        # Sin valor inicial y cola vacía (debe lanzar excepción)
        vacia = Cola()
        with self.assertRaises(Exception):
            reducir(vacia, lambda a, b: a + b)

    def test_invertir(self):
        cola_invertida = invertir(self.cola)
        self.assertEqual(a_lista(cola_invertida), [5, 4, 3, 2, 1])
        # La cola original no debe modificarse
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_a_lista(self):
        lista = a_lista(self.cola)
        self.assertEqual(lista, [1, 2, 3, 4, 5])
        # La cola original no debe modificarse
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    # -----------------------------------------------
    # Categoría: Movimiento de Elementos
    # -----------------------------------------------
    def test_mover_base_al_final(self):
        cola_nueva = mover_primero_al_ultimo(self.cola)
        self.assertEqual(a_lista(cola_nueva), [2, 3, 4, 5, 1])
        # La original no debe modificarse
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    def test_mover_final_al_frente(self):
        cola_nueva = mover_ultimo_al_primero(self.cola)
        self.assertEqual(a_lista(cola_nueva), [5, 1, 2, 3, 4])
        # La original no debe modificarse
        self.assertEqual(a_lista(self.cola), [1, 2, 3, 4, 5])

    # -----------------------------------------------
    # Categoría: Eliminación
    # -----------------------------------------------
    def test_eliminar_elemento(self):
        cola_copy = Cola()
        for x in [1, 2, 3, 2, 4]:
            cola_copy.encolar(x)
        resultado = eliminar_elemento(cola_copy, 2)
        self.assertTrue(resultado)
        self.assertEqual(a_lista(cola_copy), [1, 3, 2, 4])
        # Eliminar un valor que no está
        resultado2 = eliminar_elemento(cola_copy, 10)
        self.assertFalse(resultado2)
        self.assertEqual(a_lista(cola_copy), [1, 3, 2, 4])

    # -----------------------------------------------
    # Test de funciones adicionales (Opcional)
    # -----------------------------------------------
    def test_mover_final_al_frente_y_base_al_final(self):
        cola1 = Cola()
        cola1.encolar('a')
        cola1.encolar('b')
        cola1.encolar('c')

        # Mover base al final
        cola2 = mover_primero_al_ultimo(cola1)
        self.assertEqual(a_lista(cola2), ['b', 'c', 'a'])
        # Mover final al frente
        cola3 = mover_ultimo_al_primero(cola1)
        self.assertEqual(a_lista(cola3), ['c', 'a', 'b'])


if __name__ == '__main__':
    unittest.main()
