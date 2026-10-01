import json
import subprocess


def cargar_aplicaciones():

    with open("config/applications.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def abrir_aplicacion(nombre):

    aplicaciones = cargar_aplicaciones()

    if nombre not in aplicaciones:
        return f"No encontré la aplicación '{nombre}'."

    comando = aplicaciones[nombre]["command"]

    subprocess.Popen(comando)

    return f"Abriendo {nombre}."