print("****************************************************")
print("******* Escape Room: La Arena del Gladiador ********")
print("****************************************************\n")

print("--- BIENVENIDO A LA ARENA ---")


nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")


vida_jugador = 100
vida_enemigo = 100

pociones = 3

danio_pesado = 15
danio_enemigo = 12

turno_gladiador = True


print("=== INICIO DEL COMBATE ===")


while vida_jugador > 0 and vida_enemigo > 0:

    # TURNO DEL GLADIADOR
    if turno_gladiador:

        print()

        print(
            f"{nombre} (HP: {vida_jugador}) "
            f"vs Enemigo (HP: {vida_enemigo}) "
            f"| Pociones: {pociones}"
        )

        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")


        opcion_valida = False

        while opcion_valida == False:

            opcion_texto = input("Opción: ")

            if opcion_texto.isdigit():

                opcion = int(opcion_texto)

                if opcion >= 1 and opcion <= 3:
                    opcion_valida = True
                else:
                    print("Error: opción fuera de rango.")

            else:

                print("Error: Ingrese un número válido.")


        # ATAQUE PESADO
        if opcion == 1:

            if vida_enemigo < 20:

                danio_final = danio_pesado * 1.5

                print("¡Golpe Crítico!")

            else:

                danio_final = danio_pesado


            vida_enemigo -= danio_final

            print(
                f"¡Atacaste al enemigo por "
                f"{danio_final} puntos de daño!"
            )


        # RÁFAGA VELOZ
        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")


            for golpe in range(3):

                vida_enemigo -= 5

                print("> Golpe conectado por 5 de daño")


        # CURAR
        else:

            if pociones > 0:

                vida_jugador += 30
                pociones -= 1

                print("Te curaste 30 puntos de vida.")

            else:

                print("¡No quedan pociones!")


        turno_gladiador = False


    # TURNO DEL ENEMIGO
    if turno_gladiador == False and vida_enemigo > 0:

        vida_jugador -= danio_enemigo

        print("¡El enemigo te atacó por 12 puntos de daño!")

        turno_gladiador = True


# FIN DEL JUEGO
if vida_jugador > 0:

    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")

else:

    print("DERROTA. Has caído en combate.")