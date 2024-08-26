#####################################################################################
#     File Name           :     titulo.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-01-12 10:10]
#     Last Modified       :     [2024-08-25 20:00]
#     Description         :     Cambia el título de cada canción en archivos MP3 en
#                               la carpeta especificada, permitiendo mantener el
#                               título actual si se desea.
#####################################################################################

import os
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError


def cambiar_titulo(ruta_carpeta):
    """
    Cambia el título de cada canción en una carpeta.

    :param ruta_carpeta: Ruta de la carpeta que contiene los archivos MP3.
    """
    archivos = os.listdir(ruta_carpeta)
    archivos_mp3 = [
        archivo for archivo in archivos if archivo.lower().endswith(".mp3")]

    for archivo in archivos_mp3:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)

        try:
            # Carga los metadatos del archivo y obtiene el título actual
            audio = EasyID3(ruta_archivo)
            titulo_actual = audio['title'][0]

            # Pregunta por el nuevo título
            nuevo_titulo = input(
                f"Ingrese el nuevo título para '{titulo_actual}' (Presiona Enter para mantener el mismo): ")

            # Actualiza el título si se proporciona uno nuevo
            if nuevo_titulo.strip():
                audio['title'] = nuevo_titulo
                audio.save()
                print(
                    f"Título actualizado a '{nuevo_titulo}' para -> {archivo}")
            else:
                print(f"No se ha cambiado el título para -> {archivo}")

        except MutagenError as e:
            print(f"No se pudo procesar el archivo {archivo}: {e}")


# Ruta de la carpeta con las canciones
ruta_carpeta = r"C:\Users\Marco\Music\City Pop"

print("")
cambiar_titulo(ruta_carpeta)
print("")
