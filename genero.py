# Cambia el genero de todas las canciones en la carpeta.

import os
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC

def modificar_genero(ruta_carpeta, genero):
    """
    Actualiza el metadato de género en archivos MP3 y FLAC en la carpeta especificada.
    """
    archivos = os.listdir(ruta_carpeta)
    archivos_musica = [archivo for archivo in archivos if archivo.lower().endswith((".mp3", ".flac"))]

    for archivo in archivos_musica:
        ruta_antigua = os.path.join(ruta_carpeta, archivo)

        # Actualiza el metadato de género
        if archivo.lower().endswith(".mp3"):
            audio = EasyID3(ruta_antigua)
        elif archivo.lower().endswith(".flac"):
            audio = FLAC(ruta_antigua)
        else:
            print(f"Formato no compatible para -> {archivo}")
            continue

        audio['genre'] = genero
        audio.save()

        print(f"Género actualizado a \"{genero}\" para -> {archivo}")

# ruta_carpeta = r"D:\Music\Walküre Instrumental"
# genero = "Anime"

ruta_carpeta = input("Ingrese la ruta de la carpeta con los archivos: ")
genero = input("Ingrese el genero de los archivos: ")

print("")
modificar_genero(ruta_carpeta, genero)
print("")