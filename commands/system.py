from datetime import datetime

from pycaw.pycaw import AudioUtilities


def obtener_hora():
    hora = datetime.now()
    return hora.strftime("Son las %H:%M.")


def obtener_volumen():

    dispositivo = AudioUtilities.GetSpeakers()
    volumen = dispositivo.EndpointVolume

    return volumen


def cambiar_volumen(cantidad):

    volumen = obtener_volumen()

    volumen_actual = volumen.GetMasterVolumeLevelScalar()

    nuevo_volumen = volumen_actual + cantidad

    if nuevo_volumen > 1:
        nuevo_volumen = 1

    if nuevo_volumen < 0:
        nuevo_volumen = 0

    volumen.SetMasterVolumeLevelScalar(nuevo_volumen, None)

    porcentaje = int(nuevo_volumen * 100)

    return f"Volumen: {porcentaje}%."


def silenciar():

    volumen = obtener_volumen()

    volumen.SetMute(1, None)

    return "Volumen silenciado."

def desilenciar():

    volumen = obtener_volumen()

    volumen.SetMute(0, None)

    return "Volumen activado."