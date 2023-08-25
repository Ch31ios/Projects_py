import random

def login():

    usuarios_registrados = []

    def registrar_usuario():
        nombre = input("Ingresa tu nombre: ")
        email = input("Ingresa tu correo electrónico: ")
        password = input("Ingresa tu contraseña: ")
        telefono = input("Ingresa tu número de teléfono: ")
        
        usuario = {
            "nombre": nombre,
            "email": email,
            "password": password,
            "telefono": telefono
        }
        usuarios_registrados.append(usuario)
        
        print("\n" + "Registro exitoso. Ahora puedes iniciar sesión.")
        
        iniciar_sesion()

    def iniciar_sesion():
        opcion = input("\n" + "¿Deseas ingresar con correo o teléfono? correo(1) telefono(2) : ")
        
        if opcion.lower() == "1":
            email = input("\n" + "Ingresa tu correo electrónico: ")
            usuario = next((u for u in usuarios_registrados if u["email"] == email), None)
            
        elif opcion.lower() == "2":
            telefono = input("\n" + "Ingresa tu número de teléfono: ")
            usuario = next((u for u in usuarios_registrados if u["telefono"] == telefono), None)
            
        else:
            print("\n" + "Opción inválida. Por favor, intenta de nuevo.")
            iniciar_sesion()
            return
        
        if usuario:
            contraseña = input("Ingresa tu contraseña: ")
            
            if contraseña == usuario["password"]:
                captcha_resultado = generar_captcha()
                captcha_respuesta = int(input("\n" + f"Por favor, resuelve la siguiente operación (CAPTCHA): {captcha_resultado['operacion']} = "))
                
                if captcha_respuesta == captcha_resultado['resultado']:
                    print("\n" + f"Bienvenido/a, {usuario['nombre']}!" + "\n")
                else:
                    print("\n" + "Captcha incorrecto. Por favor, intenta de nuevo." + "\n")
                    ingresar_contraseña(usuario)
                    return
            else:
                print("\n" + "Contraseña incorrecta. Por favor, intenta de nuevo.")
                iniciar_sesion()
                return
        else:
            print("\n" + "Usuario no encontrado. Por favor, intenta de nuevo.")
            iniciar_sesion()
            return

    def generar_captcha():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        resultado = num1 + num2
        
        return {"operacion": f"{num1} + {num2}", "resultado": resultado}

    def ingresar_contraseña(usuario):
        contraseña = input("\n" + "Ingresa tu contraseña: ")
        
        if contraseña == usuario["password"]:
            captcha_resultado = generar_captcha()
            captcha_respuesta = int(input("\n" + f"Por favor, resuelve la siguiente operación (CAPTCHA): {captcha_resultado['operacion']} = "))
            
            if captcha_respuesta == captcha_resultado['resultado']:
                print("\n" + f"Bienvenido/a, {usuario['nombre']}!" + "\n")
            else:
                print("\n" + "Captcha incorrecto. Por favor, intenta de nuevo.")
                ingresar_contraseña(usuario)
                return
        else:
            print("\n" + "Contraseña incorrecta. Por favor, intenta de nuevo.")
            iniciar_sesion()
            return

    registrar_usuario()