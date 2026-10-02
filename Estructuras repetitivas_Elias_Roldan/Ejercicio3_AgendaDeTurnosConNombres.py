print("****************************************************")
print("***************** AGENDA ***********************")
print("****************************************************\n")
operador = input("Nombre del operador: ")

while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ")


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


cerrar = False


while cerrar == False:

    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")


    opcion_valida = False

    while opcion_valida == False:

        opcion_texto = input("Opción: ")

        if opcion_texto.isdigit():

            opcion = int(opcion_texto)

            if opcion >= 1 and opcion <= 5:
                opcion_valida = True
            else:
                print("Error: opción fuera de rango.")

        else:
            print("Error: ingrese un número válido.")


    # RESERVAR
    if opcion == 1:

        dia_valido = False

        while dia_valido == False:

            dia_texto = input("Día (1=Lunes, 2=Martes): ")

            if dia_texto.isdigit():

                dia = int(dia_texto)

                if dia == 1 or dia == 2:
                    dia_valido = True
                else:
                    print("Error: día fuera de rango.")

            else:
                print("Error: ingrese un número válido.")


        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente: ")


        if dia == 1:

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:

                print("Error: el paciente ya tiene un turno ese día.")

            elif lunes1 == "":

                lunes1 = paciente
                print("Turno reservado.")

            elif lunes2 == "":

                lunes2 = paciente
                print("Turno reservado.")

            elif lunes3 == "":

                lunes3 = paciente
                print("Turno reservado.")

            elif lunes4 == "":

                lunes4 = paciente
                print("Turno reservado.")

            else:

                print("No hay turnos disponibles para el lunes.")


        else:

            if paciente == martes1 or paciente == martes2 or paciente == martes3:

                print("Error: el paciente ya tiene un turno ese día.")

            elif martes1 == "":

                martes1 = paciente
                print("Turno reservado.")

            elif martes2 == "":

                martes2 = paciente
                print("Turno reservado.")

            elif martes3 == "":

                martes3 = paciente
                print("Turno reservado.")

            else:

                print("No hay turnos disponibles para el martes.")


    # CANCELAR
    elif opcion == 2:

        dia_valido = False

        while dia_valido == False:

            dia_texto = input("Día (1=Lunes, 2=Martes): ")

            if dia_texto.isdigit():

                dia = int(dia_texto)

                if dia == 1 or dia == 2:
                    dia_valido = True
                else:
                    print("Error: día fuera de rango.")

            else:
                print("Error: ingrese un número válido.")


        paciente = input("Nombre del paciente a cancelar: ")

        while not paciente.isalpha():
            print("Error: solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ")


        encontrado = False


        if dia == 1:

            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True

            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True

            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True

            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        else:

            if martes1 == paciente:
                martes1 = ""
                encontrado = True

            elif martes2 == paciente:
                martes2 = ""
                encontrado = True

            elif martes3 == paciente:
                martes3 = ""
                encontrado = True


        if encontrado:
            print("Turno cancelado.")
        else:
            print("No se encontró un turno con ese nombre.")


    # VER AGENDA
    elif opcion == 3:

        dia_valido = False

        while dia_valido == False:

            dia_texto = input("Día (1=Lunes, 2=Martes): ")

            if dia_texto.isdigit():

                dia = int(dia_texto)

                if dia == 1 or dia == 2:
                    dia_valido = True
                else:
                    print("Error: día fuera de rango.")

            else:
                print("Error: ingrese un número válido.")


        if dia == 1:

            print("Agenda del Lunes")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)


        else:

            print("Agenda del Martes")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)


    # RESUMEN GENERAL
    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0


        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1


        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1


        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes


        print("Lunes - Ocupados:", ocupados_lunes,
            "- Disponibles:", disponibles_lunes)

        print("Martes - Ocupados:", ocupados_martes,
            "- Disponibles:", disponibles_martes)


        if ocupados_lunes > ocupados_martes:

            print("Día con más turnos ocupados: Lunes")

        elif ocupados_martes > ocupados_lunes:

            print("Día con más turnos ocupados: Martes")

        else:

            print("Hay empate en turnos ocupados.")


    # CERRAR
    else:

        cerrar = True
        print("Sistema cerrado.")