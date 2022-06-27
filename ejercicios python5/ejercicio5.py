# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y
# posterior ordene los elementos de menor a mayor
import random
numeros =[]
for i in range(10):
    numeros.insert(i, random.randint(1, 20))
print("Lista de números aleatorios", numeros)
numeros.sort()
print("Lista ordenada de menor a mayor", numeros)
