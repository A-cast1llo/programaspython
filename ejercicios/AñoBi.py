a = int(input("Ingresar año: "))
if a % 4 == 0 and a % 100 != 0:
    print("El año es bisiesto")
elif a % 100 == 0 and a % 400 == 0:
    print("El año es bisiesto")
else:
    print("Es un año común")