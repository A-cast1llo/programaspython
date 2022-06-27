lista1 = []
lista2 = []
lista3 = []
for n in range(1, 6):
    print("Ingresar el valor numero %d" % n, "de la lista 1")
    lista1.append(int(input()))
print("#################################")
for n in range(1,6):
    print("Ingresar el valor numero %d" % n, "de la lista 2")
    lista2.append(int(input()))
for n in range(0, 5):
    lista3.append(lista1[n] + lista2[n])
print(lista1, "+")
print(lista2)
print("__________________")
print(lista3)
