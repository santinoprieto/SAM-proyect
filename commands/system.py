from datetime import datetime


def obtener_hora():
    hora = datetime.now()
    return hora.strftime("Son las %H:%M.")