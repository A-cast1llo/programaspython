def palabra(cadena1):
    cambio = cadena1.lower()
    cont = cambio.count("a")
    return cont


cade = input("Ingresar la palabra: ")
print("La cadena de texto: ", "'", cade, "'", ", Tiene ", palabra(cade), "a")



