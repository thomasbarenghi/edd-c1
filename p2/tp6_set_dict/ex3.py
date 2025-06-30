# Escribir un diccionario con sinónimos.
from p2.diccionario import Diccionario

sinonimosDic = Diccionario(["feliz", "contento", "alegre"], ["happy", "joyful", "cheerful"])

sinonimosDic.insert("alegre", "cheerful")
sinonimosDic.insert("feliz", "happy")

print(sinonimosDic)
