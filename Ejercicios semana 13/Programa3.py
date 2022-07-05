def superf_retangulo(v1, v2):
    area = v1 * v2
    return area


# Principal
print("Area de un rectángulo")
print("****Primero Rectángulo****")
largo = int(input("Ingresar la largo: "))
ancho = int(input("Ingresar la ancho: "))
print("El area es: ", superf_retangulo(largo, ancho))
print()
print("**** Segundo Rectángulo ****")
largo2 = int(input("Ingresar la largo: "))
ancho2 = int(input("Ingresar la ancho: "))
print("El area es: ", superf_retangulo(largo2, ancho2))
print()
print("*"*50)
if superf_retangulo(largo, ancho) > superf_retangulo(largo2, ancho2):
    print("El Primer Rectángulo tiene una superficie mayor con: ", superf_retangulo(largo, ancho), "cm")
elif superf_retangulo(largo, ancho) < superf_retangulo(largo2, ancho2):
    print("El Segundo Rectángulo tiene una superficie mayor", superf_retangulo(largo2, ancho2), "cm")
else:
    print("Ambos tienen la misma superficie")

