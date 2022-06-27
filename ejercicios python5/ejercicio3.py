notas = []
for n in range(1, 6):
    while True:
        print("Ingrese la nota", n, ": ")
        nota = int(input())
        if nota >= 0 and nota <= 10: break
    notas.append(nota)
print(notas)
# sum para sumar los elementos de la lista y len para tener la cantidad de elementos en lista.
print(sum(notas)/len(notas), "Es la Nota media.")
# max para elegir el elemento con el máximo valor dentro de la lista.
print(max(notas), "Es la Nota máxima.")
# min para elegir el elemento con el minimo valor dentro de la lista.
print(min(notas), "Es la Nota mínima")