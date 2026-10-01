from core.router import ejecutar_comando


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

        respuesta = ejecutar_comando(comando)

        print(respuesta)