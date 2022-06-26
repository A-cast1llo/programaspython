elementos = []
i = 1
while i < 6:
    print("Ingresar la cadena número", i, ":")
    elemento = input()
    i += 1
    elementos.append(elemento)
print("Lista original", elementos)
elementos.reverse()
print("Lista con elementos invertidos: ", elementos)