from utils.generales import validar_valor
from utils.utils_listas import reducir


# Ejercicio 4
# Un chef está intentando organizar sus recetas y necesita ayuda mediante algún registro de datos.
# Para esto decide crear una aplicación, para la que se deben modelar este tipo de datos.

# Crear el TDA "Receta", que contiene:
# - un arreglo con los ingredientes de una receta
# - el nombre de la receta
# - el tipo (Puede ser “omnivora”, “vegetariana” o “vegana”)

# Los ingredientes se definen con los siguientes componentes:
# - Nombre
# - Cantidad (valor entero)
# - Calorías que aporta a la receta

# Una Receta puede tener a lo sumo 20 ingredientes

# Implementar las siguientes operaciones:

# cantidadDeIngredientes():
#     Retorna la cantidad de ingredientes de la receta

# registrarIngrediente(ingrediente):
#     Agrega un ingrediente a la receta

# totalCalorias():
#     Retorna el total de las calorías de la receta

# ingredienteMasCalorico():
#     Retorna el ingrediente con mayor cantidad de calorías de la receta

class Receta:

    def __init__(self, nombre: str, tipo: str):
        self.__ingredientes = []
        self.__nombre = nombre
        self.__tipo = self.validar_tipo(tipo)

    def cantidad_de_ingredientes(self):
        print(f"Cantidad de ingredientes: {len(self.__ingredientes)}")
        return len(self.__ingredientes)

    def registrar_ingrediente(self, ingrediente: "Ingrediente"):
        self.__ingredientes.append(ingrediente)

    def total_calorias(self):
        cb = lambda acu, act: acu + act.get_calorias()
        return reducir(self.__ingredientes, cb, 0)

    def ingrediente_mas_calorico(self):
        cb = lambda max, act: act if act.get_calorias() > max.get_calorias() else max
        return reducir(self.__ingredientes, cb, self.__ingredientes[0])

    def validar_tipo(self, tipo: str):
        es_valido = validar_valor(tipo, ["omnivora", "vegetariana", "vegana"])

        if not es_valido:
            raise Exception("Tipo invalido")

        return tipo


class Ingrediente:

    def __init__(self, nombre: str, cantidad: int, calorias: int):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__calorias = calorias

    def get_calorias(self):
        return self.__calorias


# Creamos algunos ingredientes
ingrediente1 = Ingrediente("Tomate", 2, 20)
ingrediente2 = Ingrediente("Lechuga", 1, 5)
ingrediente3 = Ingrediente("Pollo", 3, 300)
ingrediente4 = Ingrediente("Queso", 1, 100)

# Creamos la receta
receta = Receta("Ensalada de Pollo", "omnivora")

# Registramos los ingredientes en la receta
receta.registrar_ingrediente(ingrediente1)
receta.registrar_ingrediente(ingrediente2)
receta.registrar_ingrediente(ingrediente3)
receta.registrar_ingrediente(ingrediente4)

# Probamos los métodos

# Verificamos la cantidad de ingredientes
receta.cantidad_de_ingredientes()

# Verificamos el total de calorías
total_calorias = receta.total_calorias()
print(f"Total de calorías: {total_calorias}")

# Verificamos el ingrediente más calórico
ingrediente_mas_calorico = receta.ingrediente_mas_calorico()
print(f"Ingrediente más calórico: {ingrediente_mas_calorico}")
