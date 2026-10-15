from core.security import confirmar_accion
from commands.files import abrir_archivo

from commands.system import (
    obtener_hora,
    cambiar_volumen,
    silenciar,
    desilenciar,
    bloquear_pc,
    apagar_pc,
    reiniciar_pc,
    suspender_pc,
    sacar_captura
)

from commands.apps import abrir_aplicacion


def ejecutar_con_confirmacion(funcion, mensaje):

    if confirmar_accion(mensaje):
        return funcion()

    return "Acción cancelada."


COMANDOS = {

    "hora": {
        "funcion": obtener_hora,
        "aliases": [
            "hora",
            "qué hora es"
        ]
    },

    "subir volumen": {
        "funcion": lambda: cambiar_volumen(0.10),
        "aliases": [
            "subir volumen",
            "aumentar volumen",
            "más volumen"
        ]
    },

    "bajar volumen": {
        "funcion": lambda: cambiar_volumen(-0.10),
        "aliases": [
            "bajar volumen",
            "disminuir volumen",
            "menos volumen"
        ]
    },

    "silenciar": {
        "funcion": silenciar,
        "aliases": [
            "silenciar",
            "mute",
            "poner mute"
        ]
    },

    "desilenciar": {
        "funcion": desilenciar,
        "aliases": [
            "desilenciar",
            "quitar mute",
            "activar sonido"
        ]
    },

    "bloquear pc": {
        "funcion": bloquear_pc,
        "aliases": [
            "bloquear pc",
            "bloquear computadora",
            "bloquear"
        ]
    },

    "apagar pc": {
        "funcion": lambda: ejecutar_con_confirmacion(
            apagar_pc,
            "¿Querés apagar la PC?"
        ),
        "aliases": [
            "apagar pc",
            "apagar computadora",
            "apagar"
        ]
    },

    "reiniciar pc": {
        "funcion": lambda: ejecutar_con_confirmacion(
            reiniciar_pc,
            "¿Querés reiniciar la PC?"
        ),
        "aliases": [
            "reiniciar pc",
            "reiniciar computadora",
            "reiniciar"
        ]
    },

    "suspender pc": {
        "funcion": lambda: ejecutar_con_confirmacion(
            suspender_pc,
            "¿Querés suspender la PC?"
        ),
        "aliases": [
            "suspender pc",
            "suspender computadora",
            "suspender"
        ]
    },

    "sacar captura": {
        "funcion": sacar_captura,
        "aliases": [
            "sacar captura",
            "captura de pantalla",
            "hacer captura",
            "capturar pantalla"
        ]
    }
}


def ejecutar_comando(comando):

    for comando_configurado in COMANDOS:

        aliases = COMANDOS[comando_configurado]["aliases"]

        if comando in aliases:
            return COMANDOS[comando_configurado]["funcion"]()

    if comando.startswith("abrir archivo "):
        ruta = comando[len("abrir archivo "):]
        return abrir_archivo(ruta)

    if comando.startswith("abrir carpeta "):
        ruta = comando[len("abrir carpeta "):]
        return abrir_archivo(ruta)

    partes = comando.split(" ", 1)

    if len(partes) == 2:
        accion = partes[0]
        objeto = partes[1]

        if accion == "abrir":
            return abrir_aplicacion(objeto)

    return "No entiendo ese comando."