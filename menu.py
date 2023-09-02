import random
import os
import sys
import keyboard # pip install keyboard, en la terminal para descargar el import

# Importar los diferentes proyectos

import bill as pagar_y_agregar_servicio
import login as login_con_registro_y_captcha
import chances as juego_de_azar
import credit as tarjeta_de_credito
import bank as administrador_de_finanzas

# --------------- Limpiar consola ---------------

def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    
limpiar_consola()

# ---------- Finalizar cada proyecto ------------

def finalizar_programa():
    
    print("\n \n" + "Gracias por jugar.")
    print("\n" + "Presiona (Ctrl) para mostrar el menú o (Shift) para salir del programa. \n")
    
    while True:
        
        if keyboard.is_pressed("ctrl"):
            limpiar_consola()
            break
            mostrar_menu()
            
        elif keyboard.is_pressed("shift"):
            limpiar_consola()
            print("\n" + "Saliendo del programa...\n")
            sys.exit()

# ---------------- ------------- ----------------

def mostrar_menu():

    print("\n" + " --------- MENÚ DE PROYECTOS ---------- ")
    print("|                                      |")
    print("|  1. Pagar y agregar servicio         |")
    print("|  2. Login con registro y captcha     |")
    print("|  3. Juego de azar                    |")
    print("|  4. Tarjeta de credito               |")
    print("|  5. Administrador de finanzas        |")
    print("|  6. Salir                            |")
    print("|                                      |")
    print(" ---------------- ---- ---------------- \n")
    
opcion = "0"

while opcion != "6":

    mostrar_menu()
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
    
        limpiar_consola()

        print("Has seleccionado la Opción 1. (Pagar y agregar servicio) \n")
        print("Preciona enter para ejecutar... \n")
        input()

        # ---------- Pagar y agregar servicio ----------
        
        pagar_y_agregar_servicio.bill()
        finalizar_programa()
            
        # ---------------- Fin opción 1. ---------------- 
        
    elif opcion == "2":
        
        limpiar_consola()
        
        print("Has seleccionado la Opción 2. (Login con registro y captcha) \n")
        print("Preciona enter para ejecutar... \n")
        input()

        # ------- Login con registro y captcha ----------
        
        login_con_registro_y_captcha.login() 
        finalizar_programa()

        # ---------------- Fin opción 2. ----------------   
        
    elif opcion == "3":
        
        limpiar_consola()
        
        print("Has seleccionado la Opción 3. (Juego de azar) \n")
        print("Preciona enter para ejecutar... \n")
        input()
        
        # ---------------- Juego de azar ----------------
    
        juego_de_azar.chances()   
        finalizar_programa()
            
        # ---------------- Fin opción 3. ----------------   
        
    elif opcion == "4":
    
        limpiar_consola()
        
        print("Has seleccionado la Opción 4. (Tarjeta de credito) \n")
        print("Preciona enter para ejecutar... \n")
        input()
        
        # ------------ Tarjeta de credito ---------------
        
        tarjeta_de_credito.credit()
        finalizar_programa()
            
        # ---------------- Fin opción 4. ----------------   
        
    elif opcion == "5":
    
        limpiar_consola()
        
        print("Has seleccionado la Opción 5. (Administrador de finanzas) \n")
        print("Preciona enter para ejecutar...")
        input()
        
        # ------------ Administrador de finanzas ---------------
        
        administrador_de_finanzas.bank()
        finalizar_programa()
            
        # ---------------- Fin opción 5. ----------------   
    
    elif opcion == "6":
        
        limpiar_consola()
        
        print("\n" + "Saliendo del programa... \n \n")
        sys.exit()
    
        # ---------------- Fin opción 6. ----------------  

    else:
        
        limpiar_consola()
        
        print("\n" + "Opción no válida. Por favor, selecciona una opción del menú. \n")
    
# ---------------- ------------- ----------------
