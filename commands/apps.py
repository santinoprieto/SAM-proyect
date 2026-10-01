import json
import subprocess


def cargar_aplicaciones():

    with open("config/applications.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def abrir_aplicacion(nombre):

    aplicaciones = cargar_aplicaciones()

    for aplicacion in aplicaciones:

        aliases = aplicaciones[aplicacion]["aliases"]

        if nombre in aliases:

            comando = aplicaciones[aplicacion]["command"]

            subprocess.Popen(comando)

            return f"Abriendo {aplicacion}."

    return f"No encontré la aplicación '{nombre}'."