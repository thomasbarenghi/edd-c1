from p2.lista import Lista
from p2.utils.linkedlist_utils import intercambiar_posiciones

l1 = Lista((10, 20, 30, 40, 60, 70))  # <- Lista ya creada con esos datos
print(l1)

intercambiar_posiciones(l1, 0, 5)

print(l1)
