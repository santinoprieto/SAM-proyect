from commands.system import obtener_hora
from commands.apps import abrir_calculadora


COMANDOS = {
    "hora": obtener_hora,
    "abrir calculadora": abrir_calculadora
}


def ejecutar_comando(comando):

    if comando in COMANDOS:
        return COMANDOS[comando]()

    return "No entiendo ese comando."