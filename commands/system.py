from datetime import datetime
import subprocess

import pyautogui
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


def bloquear_pc():

    subprocess.run([
        "rundll32.exe",
        "user32.dll,LockWorkStation"
    ])

    return "PC bloqueada."


def apagar_pc():

    subprocess.run([
        "shutdown",
        "/s",
        "/t",
        "0"
    ])

    return "Apagando PC."


def reiniciar_pc():

    subprocess.run([
        "shutdown",
        "/r",
        "/t",
        "0"
    ])

    return "Reiniciando PC."


def suspender_pc():

    subprocess.run([
        "powershell",
        "-Command",
        "Start-Process",
        "rundll32.exe",
        "powrprof.dll,SetSuspendState",
        "0,1,0"
    ])

    return "Suspendiendo PC."


def sacar_captura():

    imagen = pyautogui.screenshot()

    nombre = datetime.now().strftime(
        "captura_%Y%m%d_%H%M%S.png"
    )

    imagen.save(nombre)

    return f"Captura guardada como {nombre}."