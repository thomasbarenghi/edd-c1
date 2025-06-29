# Ejercicio 6

# El Correo Argentino nos pidió ayuda para organizar los paquetes de cada sucursal.
# Todos los días llegan paquetes con diferente peso que son apilados para luego ser distribuidos.
# Para que no se aplasten, siempre se pone el más pesado debajo y así,
# queda ordenado de manera que el paquete más liviano siempre esté en el tope.
# Pero atención, cuando llega un paquete nuevo, este debe ser intercalado de manera de respetar el orden del peso.

# Modelar el TDA ElCorreoNoSeCierra con las siguientes operaciones:

# agregarPaquete(contenido, peso):
#     Que recibe un contenido (String) y el peso de ese contenido, arma un paquete
#     y lo apila de manera que el resto de los paquetes no se aplasten.
#     Se puede asumir que en las pilas auxiliares los paquetes no se aplastan.

# pilaPaquetes() → Pila:
#     Que devuelve una copia de la pila de paquetes sin destruir los paquetes internos.

# juntarCorreos(otroCorreo):
#     Que recibe otra instancia del TDA, y “apila en self” los “paquetes de self”
#     combinados con los del otroCorreo, de manera que no se aplasten.
#     otroCorreo debe quedar intacto luego de la operación.
#     Se recomienda usar pilaPaquetes().
#     Aprovechar que “otroCorreo” ya viene ordenado.

# Notas:

# - Se recomienda primero generar el TDA Paquete, conteniendo el nombre y el peso.
# - Se pueden agregar todas las funciones auxiliares y/o operaciones de los TDAs que consideren necesarias además de las pedidas.
# - NO se puede usar el TDA Lista en la solución.

# Las soluciones correctas deben funcionar en términos del siguiente ejemplo:

# correo1 = ElCorreoNoSeCierra()
# correo2 = ElCorreoNoSeCierra()

# correo1.agregarPaquete("a", 10)
# correo1.agregarPaquete("b", 1)
# correo1.agregarPaquete("c", 5)

# correo2.agregarPaquete("d", 2)
# correo2.agregarPaquete("e", 10)
# correo2.agregarPaquete("f", 6)

# correo1 debería tener [Paquete("a", 10), Paquete("c", 5), Paquete("b", 1)]
# correo2 debería tener [Paquete("e", 10), Paquete("f", 6), Paquete("d", 2)]

# correo1.juntarCorreos(correo2)

# correo1 podría tener:
#     [Paquete("a",10), Paquete("e",10), Paquete("f",6), Paquete("c",5), Paquete("d",2), Paquete("b",1)]
# o bien:
#     [Paquete("e",10), Paquete("a",10), Paquete("f",6), Paquete("c",5), Paquete("d",2), Paquete("b",1)]

# Puede haber paquetes “repetidos” y no importa el orden para paquetes de igual peso.


class Paquete:

    def __init__(self, nombre: str, peso: int):
        self.__nombre = nombre
        self.__peso = peso
