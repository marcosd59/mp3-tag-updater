# Cambia el nombre del album de todas las canciones.

import os
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC

def renombrar_album(ruta, album):
    """
    Actualiza el metadato del álbum en archivos MP3 y FLAC en la carpeta especificada.
    """
    archivos = os.listdir(ruta)
    archivos_musica = [archivo for archivo in archivos if archivo.lower().endswith((".mp3", ".flac"))]

    for archivo in archivos_musica:
        ruta_antigua = os.path.join(ruta, archivo)

        # Actualiza el metadato del álbum
        if archivo.lower().endswith(".mp3"):
            audio = EasyID3(ruta_antigua)
        elif archivo.lower().endswith(".flac"):
            audio = FLAC(ruta_antigua)
        else:
            print(f"Formato no compatible para -> {archivo}")
            continue

        audio['album'] = album
        audio.save()

        print(f"Album actualizado a \"{album}\" para -> {archivo}")

# ruta = r"D:\LOVE LIVE SCHOOL IDOL PROJECT\Solo Live! collection Memorial BOX III\LoveLive! Solo Live! III from μ’s Nozomi Tojo Memories with Nozomi"
# album = "Solo Live! collection III Memories with Nozomi"

ruta = input("Ingrese la ruta de la carpeta con los archivos: ")
album = input("Ingrese el nombre del álbum: ")

print("")
renombrar_album(ruta, album)
print("")
