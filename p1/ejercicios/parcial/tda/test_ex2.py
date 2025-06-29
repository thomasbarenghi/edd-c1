import unittest

from ex2 import CajaDeSupermercado, Venta  # Asegúrate de importar correctamente


class TestCajaDeSupermercado(unittest.TestCase):

    def setUp(self):
        """Configurar una caja con ventas de ejemplo."""
        self.caja = CajaDeSupermercado("Carlos", 5)

        # Agregar ventas de prueba
        self.caja.agregar_venta("08:00", 50)
        self.caja.agregar_venta("09:00", 150)
        self.caja.agregar_venta("09:00", 300)
        self.caja.agregar_venta("10:00", 200)
        self.caja.agregar_venta("11:00", 400)

    def test_agregar_venta(self):
        # Verificando que la venta fue agregada correctamente
        self.assertEqual(len(self.caja.ultimas_n_ventas(99)), 5)
        # Verificar que el primer elemento (la primera venta) tenga el monto correcto
        primera_venta = self.caja.ultimas_n_ventas(1)[0]
        self.assertIsInstance(primera_venta, Venta)
        self.assertEqual(primera_venta.get_monto_de_venta(), 50)

    def test_cantidad_ventas_grandes(self):
        # Filtrar ventas mayores a 200
        cantidad = self.caja.cantidad_ventas_grandes(200)
        self.assertEqual(cantidad, 2)  # Ventas de 300 y 400

    def test_ultimas_n_ventas(self):
        ultimas = self.caja.ultimas_n_ventas(2)
        montos = [venta.get_monto_de_venta() for venta in ultimas]
        self.assertEqual(montos, [200, 400])  # Los últimos 2 se hacen si hay solo 2, o 3 en total

    def test_monto_ventas_horario(self):
        monto = self.caja.monto_ventas_horario("09:00")
        # Ventas a las 09:00 suman 150 + 300 = 450
        self.assertEqual(monto, 450)

        monto_otro_horario = self.caja.monto_ventas_horario("12:00")
        # Ninguna venta a esa hora
        self.assertEqual(monto_otro_horario, 0)

    def test_vaciar_historial(self):
        cantidad_inicial = self.caja._CajaDeSupermercado__ventas.tamaño()
        cantidad_vaciada = self.caja.vaciar_historial()
        self.assertEqual(cantidad_vaciada, cantidad_inicial)
        # La cola debe estar vacía
        self.assertEqual(self.caja._CajaDeSupermercado__ventas.tamaño(), 0)

    def test_no_modifica_colas_internas(self):
        # Verificar que al obtener últimas N ventas, la cola original no cambie
        ventas_before = self.caja._CajaDeSupermercado__ventas.a_lista()
        self.caja.ultimas_n_ventas(2)
        ventas_after = self.caja._CajaDeSupermercado__ventas.a_lista()
        self.assertEqual(ventas_before, ventas_after)


if __name__ == '__main__':
    unittest.main()
