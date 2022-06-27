import random
numeros = []
for i in range(10):
    numeros.insert(i, random.randint(1, 10))
print("Números generados aleatoriamente: ", numeros)
cuadrado = [n**2 for n in numeros]
print("Elevados al cuadrado: ", cuadrado)
cubo = [n**3 for n in numeros]
print("Elevados al cubo: ", cubo)
