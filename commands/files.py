
import os
from pathlib import Path


def abrir_archivo(ruta):

    ruta = os.path.expandvars(
        os.path.expanduser(ruta.strip().strip('"'))
    )

    if not os.path.exists(ruta):
        return f"No encontré el archivo o carpeta: {ruta}"

    try:
        os.startfile(ruta)

        return f"Abriendo: {os.path.basename(ruta)}"

    except OSError as error:
        return f"No se pudo abrir: {error}"


def buscar_archivo(nombre):

    nombre = nombre.strip().strip('"').casefold()

    if not nombre:
        return "Tenés que indicar el nombre del archivo."

    usuario = Path.home()

    carpetas = [
        usuario / "Desktop",
        usuario / "Documents",
        usuario / "Downloads",
        usuario / "Pictures",
        usuario / "OneDrive" / "Desktop",
        usuario / "OneDrive" / "Documents",
        usuario / "OneDrive" / "Downloads"
    ]

    resultados = []

    for carpeta in carpetas:

        if not carpeta.is_dir():
            continue

        for raiz, directorios, archivos in os.walk(carpeta):

            directorios[:] = [
                directorio for directorio in directorios
                if not directorio.startswith(".")
            ]

            for archivo in archivos:

                if nombre in archivo.casefold():

                    ruta = Path(raiz) / archivo

                    if ruta not in resultados:
                        resultados.append(ruta)

    if len(resultados) == 0:
        return f"No encontré ningún archivo que coincida con '{nombre}'."

    if len(resultados) == 1:
        return abrir_archivo(str(resultados[0]))

    respuesta = f"Encontré {len(resultados)} archivos:\n"

    for resultado in resultados[:10]:
        respuesta += f"\n- {resultado}"

    if len(resultados) > 10:
        respuesta += "\nHay más resultados; mostrando solo los primeros 10."

    return respuesta


def crear_archivo_texto(nombre):

    nombre = nombre.strip().strip('"')

    if not nombre:
        return "Tenés que indicar el nombre del archivo."

    if not nombre.lower().endswith(".txt"):
        nombre += ".txt"

    carpeta = Path.home() / "Documents"
    carpeta.mkdir(exist_ok=True)

    ruta = carpeta / nombre

    if ruta.exists():
        return f"Ya existe un archivo llamado '{nombre}'."

    try:
        contenido = input("Escribí el contenido del archivo: ")

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

        return f"Archivo creado correctamente: {ruta}"

    except OSError as error:
        return f"No se pudo crear el archivo: {error}"
