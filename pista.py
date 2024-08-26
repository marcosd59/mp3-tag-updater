#####################################################################################
#     File Name           :     pista.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-01-12 10:10]
#     Last Modified       :     [2024-08-25 19:45]
#     Description         :     Actualiza el número de pista en los metadatos de
#                               archivos FLAC y MP3 en la carpeta especificada.
#####################################################################################

import os
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3


def modificar_numero_pista(ruta_carpeta):
    """
    Actualiza el número de pista en los metadatos de archivos FLAC y MP3.

    :param ruta_carpeta: Ruta de la carpeta que contiene los archivos de música.
    """
    archivos = os.listdir(ruta_carpeta)
    archivos_musica = [
        archivo for archivo in archivos if archivo.lower().endswith((".flac", ".mp3"))
    ]

    total_canciones = len(archivos_musica)

    for i, archivo in enumerate(archivos_musica, start=1):
        ruta_antigua = os.path.join(ruta_carpeta, archivo)

        # Identifica el tipo de archivo y carga el archivo de audio correspondiente
        if archivo.lower().endswith(".flac"):
            audio = FLAC(ruta_antigua)
        elif archivo.lower().endswith(".mp3"):
            audio = EasyID3(ruta_antigua)
        else:
            print(f"Formato no compatible para -> {archivo}")
            continue

        # Actualiza el metadato del número de pista
        audio['tracknumber'] = f"{i}/{total_canciones}"
        audio.save()
        print(
            f"Número de pista actualizado a {i}/{total_canciones} para -> {archivo}")


# Ruta de la carpeta con las canciones
ruta_carpeta = r"C:\Users\Marco\Music\City Pop\Showa Idol's Groove"

print("")
modificar_numero_pista(ruta_carpeta)
print("")
