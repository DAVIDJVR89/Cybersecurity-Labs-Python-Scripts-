usuario_correcto = "David"
contraseña_correcta = "1234"
max_intentos = 3
intentos_restantes = 3

while True:
    usuario_entrada = input(f"Introduzca su usuario:  ")
    if usuario_entrada != usuario_correcto:
        print("Usuario no válido, intente de nuevo.  ")
        continue
    else:
        print("Usuario correcto.")

    while intentos_restantes > 0:
        intentos_actuales = max_intentos - intentos_restantes + 1
        entrada_contraseña = input(f"Contraseña. Intento {intentos_actuales} / {max_intentos}:  ")
        if entrada_contraseña == contraseña_correcta:
            print("ACCESO AUTORIZADO")
            exit()
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos. ")

            else:
                print(f"Máximo de intentos superados. Cuenta bloqueada por seguridad.")
                exit()

    



    

            
                





