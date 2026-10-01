from commands.system import *
from commands.apps import abrir_aplicacion


COMANDOS = {
    "hora": obtener_hora,
    "subir volumen": lambda: cambiar_volumen(0.10),
    "bajar volumen": lambda: cambiar_volumen(-0.10),
    "silenciar": silenciar,
    "desilenciar": desilenciar,
    "bloquear pc": bloquear_pc
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