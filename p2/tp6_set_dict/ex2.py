from p2.diccionario import Diccionario

# Ejercicio 2

dic1 = Diccionario([1,2], [3,4])

print(dic1)

dic2 = Diccionario()
dic2.insert(1, 3)
dic2.insert(2, 4)

dic3 = Diccionario()
dic3[1] = 3
dic3[2] = 4

print(dic1)
print(dic2)
print(dic3)

# Modificar un valor

dic1[1] = 5

print(dic1)
print(dic1[1])

print(dic1.get(1))

dic1.insert(8, 9)
dic1.insert(8, 9)
print(dic1)

dic1[8] = 10

print(dic1)