from estructuras.cola import Cola
from utils.utils_colas import filtrar, obtener_ultimos_n_elementos, reducir


# Ejercicio 2
# En un trabajo estamos implementando el software de administración de ventas de la línea de cajas
# de un supermercado. Para esto tenemos que crear el TDA CajaDeSupermercado que contiene:

# - Una estructura de datos que contiene el historial de ventas que se cobraron en esa caja,
#   donde una venta consiste en un monto y el horario en el que fue realizada.
#   En esta estructura se accede primero solo a la primera venta que se hizo en el día.
#   La estructura debe ser dinámica. NO se puede usar una Lista.

# - El nombre de la persona que administra la caja
# - El número de la caja en la línea

# Implementar las siguientes operaciones en el TDA CajaDeSupermercado:

# agregarVenta(horario, montoDeVenta):
#     Operación que guarda la venta realizada. Por simplicidad asumir que el horario es un string.

# cantidadDeVentasGrandes(montoMinimo):
#     Operación que calcula la cantidad de ventas que se realizaron en la caja que sean mayores
#     al monto que se recibe como parámetro. El historial de ventas NO debe ser modificado.

# ultimasNVentas(N):
#     Operación que retorna un arreglo conteniendo los montos de las últimas N ventas que se cobraron
#     en la caja. El historial de ventas NO debe ser modificado.

# vaciarHistorial():
#     Operación que vacía el historial de ventas retornando la cantidad de ventas eliminadas.

# montoVentasHorario(horario):
#     Operación que retorna el importe de la venta realizada en ese horario.

# Ayuda: Modelar la venta con otro TDA.

class CajaDeSupermercado:

    def __init__(self, responsable, numero):
        self.__ventas = Cola()
        self.__responsable = responsable
        self.__numero = numero

    def agregar_venta(self, horario, monto_de_venta):
        venta = Venta(monto_de_venta, horario)
        self.__ventas.encolar(venta)

        print(f"Venta agregada. Monto: {monto_de_venta}, Horario: {horario}")

    def cantidad_ventas_grandes(self, monto_minimo):
        condicion = lambda venta: venta.get_monto_de_venta() > monto_minimo
        ventas_filtradas = filtrar(self.__ventas, condicion)

        print(f"Cantidad de ventas grandes: {ventas_filtradas.tamaño()}")

        return ventas_filtradas.tamaño()

    def ultimas_n_ventas(self, n):
        return obtener_ultimos_n_elementos(self.__ventas, n)

    def monto_ventas_horario(self, horario):
        condicion = lambda venta: venta.get_horario() == horario
        ventas_filtradas = filtrar(self.__ventas, condicion)

        cb = lambda acumulado, venta: acumulado + venta.get_monto_de_venta()
        print(f"Total de ventas para el horario {horario}: {reducir(ventas_filtradas, cb, 0)}")

        return reducir(ventas_filtradas, cb, 0)

    def vaciar_historial(self):
        cantidad = self.__ventas.tamaño()
        self.__ventas.limpiar()
        return cantidad


class Venta:

    def __init__(self, monto_de_venta, horario):
        self.__monto_de_venta = monto_de_venta
        self.__horario = horario

    def get_monto_de_venta(self):
        return self.__monto_de_venta

    def get_horario(self):
        return self.__horario


# Pruebas
caja = CajaDeSupermercado("Juan", 1)

# Agregar ventas
caja.agregar_venta("09:00", 100)
caja.agregar_venta("10:00", 200)
caja.agregar_venta("11:00", 300)

# Verificar ventas grandes
caja.cantidad_ventas_grandes(150)

# Obtener últimas 2 ventas
caja.ultimas_n_ventas(2)

# Ver monto de ventas por horario
caja.monto_ventas_horario("10:00")

# Vaciar historial de ventas
caja.vaciar_historial()
