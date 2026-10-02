print("****************************************************")
print("************** Escape Room: La Bóveda **************")
print("****************************************************\n")

agente = input("Nombre del agente: ")

while not agente.isalpha():
    print("Error: solo se permiten letras.")
    agente = input("Nombre del agente: ")


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0
bloqueado = False


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False:

    print()
    print("Agente:", agente)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)

    if alarma:
        print("Alarma: ACTIVADA")
    else:
        print("Alarma: DESACTIVADA")


    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")


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
            print("Error: ingrese un número válido.")


    # FORZAR CERRADURA
    if opcion == 1:

        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1


        # Tercera vez consecutiva
        if forzar_seguidas == 3:

            alarma = True

            print("La cerradura se trabó. Se activó la alarma.")


        else:

            if energia < 40 and alarma == False:

                riesgo_valido = False

                while riesgo_valido == False:

                    riesgo_texto = input(
                        "Riesgo de alarma. Elegí un número del 1 al 3: "
                    )

                    if riesgo_texto.isdigit():

                        riesgo = int(riesgo_texto)

                        if riesgo >= 1 and riesgo <= 3:
                            riesgo_valido = True
                        else:
                            print("Error: número fuera de rango.")

                    else:
                        print("Error: ingrese un número válido.")


                if riesgo == 3:

                    alarma = True

                    print("¡Se activó la alarma!")


            if alarma == False:

                cerraduras_abiertas += 1

                print("Abriste una cerradura.")


    # HACKEAR PANEL
    elif opcion == 2:

        energia -= 10
        tiempo -= 3

        # Se corta la racha de forzar
        forzar_seguidas = 0


        print("Hackeando panel...")


        for paso in range(1, 5):

            codigo_parcial += "A"

            print(f"Paso {paso}/4 - Código parcial: {codigo_parcial}")


        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas += 1

            print("El código alcanzó la longitud necesaria. Se abrió una cerradura.")


    # DESCANSAR
    else:

        tiempo -= 1
        energia += 15

        # Se corta la racha de forzar
        forzar_seguidas = 0


        if energia > 100:
            energia = 100


        if alarma:

            energia -= 10

            print("La alarma está activa: perdés 10 puntos extra de energía.")


        print("Descansaste.")


    # BLOQUEO POR ALARMA
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:

        bloqueado = True

        print("El sistema se bloqueó por la alarma.")


print()


if cerraduras_abiertas == 3:

    print("VICTORIA: abriste las 3 cerraduras.")

elif bloqueado:

    print("DERROTA: la bóveda quedó bloqueada por la alarma.")

else:

    print("DERROTA: te quedaste sin energía o sin tiempo.")