nombres = []
edades = []
print("************NOTA************")
print("####El programa se detendrá cuando se coloque como nombre un asterisco ####")
print()

while True:
    nombre = input("Ingresar el nombre del alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edad = int(input("Ingresar edad: "))
        edades.append(edad)
    elif nombre == "*": break

print("#####################################################")
print("Los alumnos mayores de edad son:")
for nombre, edad in zip(nombres, edades):  # zip para recorrer la lista y devolver un valor
    if edad >= 18:
        print(nombre, "con", edad, "años")
print("#####################################################")
alum_m = max(edades)
print("Los alumnos con mayor edad son:")
for nombre, edad in zip(nombres, edades):
    if edad == alum_m:
        print(nombre, "con", edad, "años")
print("#####################################################")


