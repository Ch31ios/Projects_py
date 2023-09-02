
def bank():

    def mostrar_menu():   
        print("\n \n" + " ----- Administrador de Finanzas ------ ")
        print("|                                      |")
        print("|  1. Registrar Ingreso                |")
        print("|  2. Registrar Deducción              |")
        print("|  3. Mostrar Balance                  |")
        print("|  4. Salir                            |")
        print("|                                      |")
        print(" ---------------- ---- ---------------- \n")

    ingresos = []
    deducciones = []

    while True:
        
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            
            try:
                ingreso = float(input("\n" + "Ingrese el monto del ingreso: "))
                
                ingresos.append(ingreso) # <-- AGREGA CADA DATO INGRESADO EN LA LISTA DE "ingresos"
                
                print("\n" + f"Ingreso registrado: ${ingreso:.2f} \n")
                
            except ValueError:
                print("\n" + "Entrada inválida. Introduzca un número válido.")

        elif opcion == "2":
            
            try:
                deduccion = float(input("\n" + "Ingrese el monto de la deducción: "))
                
                deducciones.append(deduccion) # <-- AGREGA CADA DATO INGRESADO EN LA LISTA DE "deducciones"
                
                print("\n" + f"Deducción registrada: ${deduccion:.2f} \n")
                
            except ValueError:
                print("\n" + "Entrada inválida. Introduzca un número válido.")

        elif opcion == "3":
            
            total_ingresos = sum(ingresos) # <-- SUMA TODOS LOS DATOS DE LA LISTA DE "ingresos"
            total_deducciones = sum(deducciones) # <-- SUMA TODOS LOS DATOS DE LA LISTA DE "deducciones"
            saldo = total_ingresos - total_deducciones # <-- RESTA EL TOTAL DE LAS deducciones DEL TOTAL DE LOS ingresos
            
            if saldo > 0:
                print("\n" + f"Balance total: ${saldo:.2f} (Ganancias)")
                
            elif saldo < 0:
                print("\n" + f"Balance total: ${saldo:.2f} (Pérdidas)")
                
            else:
                print("\n" + f"Balance total: $0.00 (Sin cambios en el saldo)")

        elif opcion == "4":
            break

        else:
            print("\n" + "Opción no válida. Por favor, seleccione una opción del menú.")
            
