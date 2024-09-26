#####################################################################################
#     File Name           :     interpretes_colaboradores.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-09-29 10:10]
#     Last Modified       :     [2024-09-29 19:50]
#     Description         :     Actualiza el metadato de los intérpretes colaboradores
#                               en archivos MP3 y FLAC en la carpeta especificada.
#####################################################################################

import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC


def actualizar_interpretes(ruta, interpretes):
    """
    Actualiza el metadato de los intérpretes colaboradores en archivos MP3 y FLAC
    en la carpeta especificada.

    :param ruta: Ruta de la carpeta que contiene los archivos de música.
    :param interpretes: Lista de intérpretes colaboradores a asignar a los archivos.
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

        # Actualiza el metadato de los intérpretes colaboradores
        audio['artist'] = interpretes
        audio.save()

        print(
            f"Intérpretes colaboradores actualizados a \"{interpretes}\" para -> {archivo}")


# Ruta de la carpeta con las canciones
ruta = r"C:\Users\Marco\Music\Vocaloid"

# Nuevos intérpretes colaboradores para las canciones
interpretes = "Hatsune Miku, Kagamine Rin, Kagamine Len"

print("")
actualizar_interpretes(ruta, interpretes)
print("")
