def confirmar_accion(mensaje):

    respuesta = input(
        f"{mensaje} (s/n): "
    ).lower().strip()

    return respuesta == "s"