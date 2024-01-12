# Actualiza el numero de la pista de 1 en 1 hasta el total de canciones

import os
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3

def modificar_numero_pista(ruta_carpeta):
    archivos = os.listdir(ruta_carpeta)
    archivos_musica = [archivo for archivo in archivos if archivo.lower().endswith((".flac", ".mp3"))]

    total_canciones = len(archivos_musica)

    for i, archivo in enumerate(archivos_musica, start=1):
        ruta_antigua = os.path.join(ruta_carpeta, archivo)

        # Actualiza el metadato del número de pista
        if archivo.lower().endswith(".flac"):
            audio = FLAC(ruta_antigua)
        elif archivo.lower().endswith(".mp3"):
            audio = EasyID3(ruta_antigua)
        else:
            print(f"Formato no compatible para -> {archivo}")
            continue

        if 'tracknumber' in audio:
            audio['tracknumber'] = str(0)
            audio.save()
            print(f"Número de pista actualizado a {i}/{total_canciones} para -> {archivo}")
        else:
            print(f"No se pudo actualizar el número de pista para -> {archivo}")

# ruta_carpeta = r"D:\Music\City Pop\Showa Idol's Groove"

ruta_carpeta = input("Ingrese la ruta de la carpeta con los archivos: ")


print("")
modificar_numero_pista(ruta_carpeta)
print("")
