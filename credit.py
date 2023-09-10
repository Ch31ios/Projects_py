
def credit():
    
    print("\n" + " - Tarjeta de crédito \n")
    
    cupo_total = 200 # <--- Cupo de la tarjeta de crédito
    cupo_restante = cupo_total
    
    print(f"Cupo disponible = {cupo_restante} dólares")
    
    nombre = input("\n" + "Ingrese su nombre: ")
    
    while cupo_restante > 0:
        
        compra = int(input("\n" + "Ingrese el valor de la compra: "))
        
        if compra > cupo_restante:
            
            print("\n" + "No tienes suficiente cupo en la tarjeta. Introduce otro valor de compra.")
            continue
        
        cuotas = int(input("Ingrese número de cuotas: "))
        
        deuda = compra
        separacion = compra / cuotas
        
        print("\n" + f"Detalle de pagos de {nombre} \n")
        
        i = 1
        
        while deuda > 1 and i <= cuotas:
            
            total = cuotas * compra
            
            if total == cuotas:
                cuota_actual = deuda
            else:
                cuota_actual = separacion
                deuda -= cuota_actual
                
            cupo_restante -= cuota_actual
            
            print(f"Cuota {i}: ${cuota_actual:.2f} - Deuda restante: ${deuda:.2f} - Cupo restante: ${int(cupo_restante)}")
            
            i += 1 
            
        respuesta = input("\n" + "¿Desea comprar otro producto? (s/n): ")  
        
        while respuesta != "s" and respuesta != "n":
            
            respuesta = input("\n" + "Ingrese una opción válida. ¿Desea comprar otro producto? (s/n): ")  
             
        if respuesta == "n":
            
            print("\n" + "Gracias por comprar, vuelve pronto! \n")
            break
        
        else:
            print("\n" + f"Cupo disponible actual = {int(cupo_restante)} dólares")

