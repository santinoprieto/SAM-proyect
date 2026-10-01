from commands.system import obtener_hora
from commands.apps import abrir_aplicacion


COMANDOS = {
    "hora": obtener_hora
}


def ejecutar_comando(comando):

    if comando in COMANDOS:
        return COMANDOS[comando]()

    partes = comando.split(" ", 1)

    if len(partes) == 2:

        accion = partes[0]
        objeto = partes[1]

        if accion == "abrir":
            return abrir_aplicacion(objeto)

    return "No entiendo ese comando."