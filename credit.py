
def credit():

    print("\n - Tarjeta de crédito" + "\n")

    cupo_total = 200 # <--- MAXIMO DE CUPO EN NUESTRA TARJETA DE CRÉDITO
    
    print(f"Cupo disponible = {cupo_total} dolares")

    nombre = input("\n Ingrese su nombre: ")
    compra = int(input(" Ingrese el valor de la compra: "))
    cuotas = int(input(" Ingrese número de cuotas: "))

    if compra <= cupo_total:

        deuda = compra
        separacion = compra / cuotas

        print(f"\n Detalle de pagos de {nombre} \n")
        i = 1

        while deuda > 1 and i <= cuotas:
            total = cuotas * compra
            if total == cuotas:
                cuota_actual = deuda
            else:
                cuota_actual = separacion
                deuda -= cuota_actual

            print(f" Cuota {i}: ${cuota_actual:.2f} - Deuda restante: ${deuda:.2f}")
            i += 1 

        print("\n")

    else:
        print("\n No se puede hacer la compra \n")
        
