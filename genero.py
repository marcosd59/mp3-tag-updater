#####################################################################################
#     File Name           :     genero.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-01-12 10:10]
#     Last Modified       :     [2024-08-25 19:55]
#     Description         :     Actualiza el metadato de género en archivos MP3 y FLAC
#                               en la carpeta especificada.
#####################################################################################

import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC


def modificar_genero(ruta_carpeta, genero):
    """
    Actualiza el metadato de género en archivos MP3 y FLAC en la carpeta especificada.

    :param ruta_carpeta: Ruta de la carpeta que contiene los archivos de música.
    :param genero: Género musical que se asignará a los archivos.
    """
    archivos = os.listdir(ruta_carpeta)
    archivos_musica = [
        archivo for archivo in archivos if archivo.lower().endswith((".mp3", ".flac"))
    ]

    for archivo in archivos_musica:
        ruta_antigua = os.path.join(ruta_carpeta, archivo)

        # Identifica el tipo de archivo y carga el archivo de audio correspondiente
        if archivo.lower().endswith(".mp3"):
            audio = EasyID3(ruta_antigua)
        elif archivo.lower().endswith(".flac"):
            audio = FLAC(ruta_antigua)
        else:
            print(f"Formato no compatible para -> {archivo}")
            continue

        # Actualiza el metadato de género
        audio['genre'] = genero
        audio.save()

        print(f"Género actualizado a \"{genero}\" para -> {archivo}")


# Ruta de la carpeta con las canciones
ruta_carpeta = r"C:\Users\Marco\Music\Vocaloid"

# Nuevo género para las canciones
genero = "Anime"

print("")
modificar_genero(ruta_carpeta, genero)
print("")
