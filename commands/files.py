import os
import subprocess


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
        return f"No se pudo abrir el archivo: {error}"
