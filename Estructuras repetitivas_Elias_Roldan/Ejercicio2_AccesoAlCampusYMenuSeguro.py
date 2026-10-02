print("****************************************************")
print("****************** CAMPUS ************************")
print("****************************************************\n")
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False


while intentos < 3 and acceso == False:

    intentos += 1

    print(f"Intento {intentos}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")


if acceso == False:

    print("Cuenta bloqueada")

else:

    salir = False

    while salir == False:

        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion_valida = False

        while opcion_valida == False:

            opcion_texto = input("Opción: ")

            if opcion_texto.isdigit():

                opcion = int(opcion_texto)

                if opcion >= 1 and opcion <= 4:
                    opcion_valida = True
                else:
                    print("Error: opción fuera de rango.")

            else:
                print("Error: ingrese un número válido.")


        if opcion == 1:

            print("Inscripto")


        elif opcion == 2:

            clave_cambiada = False

            while clave_cambiada == False:

                nueva_clave = input("Nueva clave: ")

                if len(nueva_clave) < 6:

                    print("Error: mínimo 6 caracteres.")

                else:

                    confirmacion = input("Confirmar nueva clave: ")

                    if nueva_clave == confirmacion:

                        clave_correcta = nueva_clave
                        clave_cambiada = True

                        print("Clave cambiada correctamente.")

                    else:

                        print("Error: las claves no coinciden.")


        elif opcion == 3:

            print("¡De los errores se aprende!.")


        else:

            salir = True