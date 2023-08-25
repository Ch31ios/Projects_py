
def bill():

    def calcular_total(cantidad):
        servicio = cantidad * 0.10
        total = cantidad + servicio
        return total

    def realizar_pedido():
        total = 0

        while True:
            cantidad = float(input("\n" + "Ingrese la cantidad a pagar: ")) 
            total += cantidad

            otro_producto = input("\n" + "¿Desea agregar otro producto? (s/n): ") 
            if otro_producto.lower() == "n":
                break

        agregar_servicio = input("\n" + "¿Desea agregar el servicio? (s/n): ") 
        if agregar_servicio.lower() == "s":
            total = calcular_total(total)

        print("\n" + f"El total a pagar es: {total}" + "\n") 

    realizar_pedido()