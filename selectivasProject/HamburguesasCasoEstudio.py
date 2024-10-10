#definir las constantes
PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE = 28000
IMPUESTO_TARJETA = 0.07

#FUNCION para calcular el precio
def calculcar_precio(tipo_hamburgusa,medio_pago, cantidad):
    #definir los precios segun el tipo de hamburguesa
    if tipo_hamburgusa == 1:
        precio = PRECIO_SENCILLA
        descripcion = "sencilla"

    elif tipo_hamburgusa == 2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"
    elif tipo_hamburgusa == 3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"
    else:
        return None #tipo de hamburguesa invalido

    #calcular el total sin cargos
    total_sin_cargo =precio * cantidad

    # Aplicar impuestos si el medio de pago es tarjeta
    if medio_pago == 1:
        impuesto = round(total_sin_cargo * IMPUESTO_TARJETA)
    else:
        impuesto = 0

    total = round(total_sin_cargo + impuesto)
    #Retornar datos relevantes
    return descripcion, precio,cantidad, impuesto, total

def generar_mensaje(descripcion, precio,cantidad,impuesto,total):
    return (f"Tipo de Hamburguesa: {descripcion}\n"
            f"Preci: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: ${total}")

#Funcion para validar los datos
def validar_datos(tipo_hamburguesa,medio_pago, cantidad):
    if 1 <= tipo_hamburguesa <= 3 and 1 <= medio_pago <= 2 and cantidad > 0:
        resultado = calculcar_precio(tipo_hamburguesa,medio_pago,cantidad)
        #print(resultado: ", resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio, cantidad, impuesto, total)
        print("----------\n" + mensaje)
    else:
        print("verifique las opciones ingresadas")

#entradas 
tipo_hamburguesa = int(input("ingrese tipo de hamburguesa \n1. sencilla \n2. doble \n3. triple \n"))
medio_pago = int(input("ingrese medio de pago \n1. tarjeta \n2. otro  \n"))
#salidas
validar_datos(tipo_hamburguesa, medio_pago,cantidad)

