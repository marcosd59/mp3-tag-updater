#####################################################################################
#     File Name           :     album.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-01-12 10:10]
#     Last Modified       :     [2024-08-25 19:50]
#     Description         :     Actualiza el metadato del álbum en archivos MP3 y FLAC
#                               en la carpeta especificada.
#####################################################################################

import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC


def renombrar_album(ruta, album):
    """
    Actualiza el metadato del álbum en archivos MP3 y FLAC en la carpeta especificada.

    :param ruta: Ruta de la carpeta que contiene los archivos de música.
    :param album: Nombre del álbum que se asignará a los archivos.
    """
    archivos = os.listdir(ruta)
    archivos_musica = [
        archivo for archivo in archivos if archivo.lower().endswith((".mp3", ".flac"))
    ]

    for archivo in archivos_musica:
        ruta_antigua = os.path.join(ruta, archivo)

        # Identifica el tipo de archivo y carga el archivo de audio correspondiente
        if archivo.lower().endswith(".mp3"):
            audio = EasyID3(ruta_antigua)
        elif archivo.lower().endswith(".flac"):
            audio = FLAC(ruta_antigua)
        else:
            print(f"Formato no compatible para -> {archivo}")
            continue

        # Actualiza el metadato del álbum
        audio['album'] = album
        audio.save()

        print(f"Álbum actualizado a \"{album}\" para -> {archivo}")


# Ruta de la carpeta con las canciones
ruta = r"D:\LOVE LIVE SCHOOL IDOL PROJECT\Solo Live! collection Memorial BOX II\Love Live! Solo Live! collection Wakakusa no Season (Hanayo Koizumi)"

# Nuevo álbum para las canciones
album = "Solo Live! collection II Wakakusa no Season - Koizumi Hanayo"

print("")
renombrar_album(ruta, album)
print("")
