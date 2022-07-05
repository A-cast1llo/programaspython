from random import randint
puntaje_jugador = 0
puntaje_pc = 0
while True:
    jugador =(input("Escribir tu jugada: Piedra, Papel o Tijera :  "))
    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]

    print("La computadora elige: ", computadora)
    if computadora == jugador:
        print("Hay un empate")
    elif computadora == "piedra" and jugador == "papel":
        print("Gana jugador")
        puntaje_jugador +=1
    elif computadora == "piedra" and jugador == "tijera":
        print("Gana computadora")
        puntaje_pc += 1

    elif computadora == "papel" and jugador == "piedra":
        print("Gana computadora ")
        puntaje_pc += 1

    elif computadora == "papel" and jugador == "tijera":
        print("Gana jugador")
        puntaje_jugador += 1

    elif computadora == "tijera" and jugador == "piedra":
        print("Gana jugador")
        puntaje_jugador += 1

    elif computadora == "tijera" and jugador == "papel":
        print("Gana Computadora")
        puntaje_pc += 1
    print()
    print("PUNTAJE")
    print()
    print("usuario: ", puntaje_jugador)
    print("Computadora", puntaje_pc)
    print("¿Quieres continuar jugando?")
    resp = input()
    if resp == "no":
        break
