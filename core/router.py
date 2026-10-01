from commands.system import obtener_hora


COMANDOS = {
    "hora": obtener_hora
}


def ejecutar_comando(comando):

    if comando in COMANDOS:
        return COMANDOS[comando]()

    return "No entiendo ese comando."