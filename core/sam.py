from commands.system import obtener_hora


def iniciar_sam():

    print("================================")
    print("             SAM")
    print("  System Automated Management")
    print("================================")

    print("\nSAM iniciado.")
    print("Escribí 'salir' para cerrar.\n")

    while True:

        comando = input("SAM > ").lower().strip()

        if comando == "salir":
            print("SAM finalizado.")
            break

        elif comando == "hora":
            print(obtener_hora())

        else:
            print("No entiendo ese comando.")