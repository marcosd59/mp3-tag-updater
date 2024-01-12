##############################################################################
#     File Name           :     main.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-01-12 10:10]
#     Last Modified       :     [2024-01-12 11:00]
#     Description         :     Renombrar archivos MP3
##############################################################################

import os
from mutagen.easyid3 import EasyID3

def num_pista(archivo):
    """
    Obtiene el número de pista de los metadatos del archivo MP3.
    """
    try:
        audio = EasyID3(archivo)
        pista = int(audio['tracknumber'][0])
        return pista
    except (KeyError, ValueError):
        return None

def renombrar(ruta, album):
    """
    Renombra archivos MP3 en la carpeta especificada y actualiza el metadato del álbum.
    """
    archivos = os.listdir(ruta)
    archivos_mp3 = [archivo for archivo in archivos if archivo.lower().endswith(".mp3")]

    for archivo in archivos_mp3:
        ruta_antigua = os.path.join(ruta, archivo)

        numero_pista = num_pista(ruta_antigua)
        if numero_pista is not None:
            nuevo_nombre = f"{numero_pista:02d}. {archivo}"
            ruta_nueva = os.path.join(ruta, nuevo_nombre)

            # Renombra el archivo
            os.rename(ruta_antigua, ruta_nueva)

            print(f"Renombrado: {archivo} -> {nuevo_nombre}")

            # Actualiza el metadato del álbum
            audio = EasyID3(ruta_nueva)
            audio['album'] = album
            audio.save()

            print(f"Album actualizado a \"{album}\" para -> {nuevo_nombre}")
        else:
            print(f"No se pudo obtener el número de pista para: {archivo}")

# ruta = r"C:\Users\Marco\Downloads\ficheros"
ruta = input("Ingrese la ruta de la carpeta con los archivos MP3: ")
album = input("Ingrese el nombre del álbum: ")

print("")
renombrar(ruta, album)
print("")