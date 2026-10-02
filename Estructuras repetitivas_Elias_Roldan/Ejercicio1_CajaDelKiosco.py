print("****************************************************")
print("**************** Tu Kiosco **********************")
print("****************************************************\n")
nombre = input("Nombre del cliente: ")

while not nombre.isalpha():
    print("Error: ingrese un nombre válido.")
    nombre = input("Nombre del cliente: ")


cantidad_texto = input("Cantidad de productos: ")

while not cantidad_texto.isdigit() or int(cantidad_texto) <= 0:
    print("Error: ingrese una cantidad entera mayor que 0.")
    cantidad_texto = input("Cantidad de productos: ")

cantidad = int(cantidad_texto)


total_sin_descuentos = 0
total_con_descuentos = 0.0


for producto in range(1, cantidad + 1):

    precio_texto = input(f"Producto {producto} - Precio: ")

    while not precio_texto.isdigit():
        print("Error: ingrese un precio entero válido.")
        precio_texto = input(f"Producto {producto} - Precio: ")

    precio = int(precio_texto)


    descuento = input("Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ").lower()


    total_sin_descuentos += precio

    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuentos += precio_final


ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad


print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")