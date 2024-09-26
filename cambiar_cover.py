#####################################################################################
#     File Name           :     cambiar_cover.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-09-29 12:10]
#     Last Modified       :     [2024-09-29 14:20]
#     Description         :     Cambia el cover de todas las canciones en una carpeta
#                               especificada con una imagen dada.
#####################################################################################

import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen.flac import FLAC, Picture


def agregar_cover_mp3(archivo_mp3, imagen):
    """
    Agrega o reemplaza el cover en un archivo MP3.

    :param archivo_mp3: Ruta del archivo MP3.
    :param imagen: Ruta de la imagen para el cover.
    """
    try:
        audio = MP3(archivo_mp3, ID3=ID3)

        # Si no tiene etiquetas ID3, las añadimos
        try:
            audio.add_tags()
        except error:
            pass

        # Elimina la portada anterior si existe
        audio.tags.delall("APIC")

        # Añade la nueva portada
        with open(imagen, 'rb') as img:
            audio.tags.add(
                APIC(
                    encoding=3,  # 3 es UTF-8
                    mime='image/jpeg',  # O 'image/png'
                    type=3,  # Cover del frente
                    desc='Cover',
                    data=img.read()
                )
            )
        audio.save()

        print(f"Cover actualizado para {archivo_mp3}")

    except Exception as e:
        print(f"No se pudo actualizar el cover en {archivo_mp3}: {e}")


def agregar_cover_flac(archivo_flac, imagen):
    """
    Agrega o reemplaza el cover en un archivo FLAC.

    :param archivo_flac: Ruta del archivo FLAC.
    :param imagen: Ruta de la imagen para el cover.
    """
    try:
        audio = FLAC(archivo_flac)

        # Elimina la portada anterior si existe
        audio.clear_pictures()

        # Añade la nueva portada
        with open(imagen, 'rb') as img:
            pic = Picture()
            pic.data = img.read()
            pic.type = 3  # Cover del frente
            pic.mime = "image/jpeg"  # O "image/png"
            audio.add_picture(pic)
        audio.save()

        print(f"Cover actualizado para {archivo_flac}")

    except Exception as e:
        print(f"No se pudo actualizar el cover en {archivo_flac}: {e}")


def cambiar_cover_canciones(ruta_carpeta, ruta_imagen):
    """
    Cambia el cover de todas las canciones MP3 y FLAC en la carpeta especificada.

    :param ruta_carpeta: Ruta de la carpeta que contiene los archivos de música.
    :param ruta_imagen: Ruta de la imagen que se usará como cover.
    """
    archivos = os.listdir(ruta_carpeta)
    archivos_musica = [
        archivo for archivo in archivos if archivo.lower().endswith((".mp3", ".flac"))
    ]

    for archivo in archivos_musica:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)

        # Actualiza el cover según el formato de archivo
        if archivo.lower().endswith(".mp3"):
            agregar_cover_mp3(ruta_archivo, ruta_imagen)
        elif archivo.lower().endswith(".flac"):
            agregar_cover_flac(ruta_archivo, ruta_imagen)
        else:
            print(f"Formato no compatible para -> {archivo}")


# Ruta de la carpeta con las canciones
ruta_carpeta = r"C:\Users\Marco\Music\Vocaloid"

# Ruta de la imagen que se usará como cover
ruta_imagen = r"D:\Downloads\cover.jpg"

print("")
cambiar_cover_canciones(ruta_carpeta, ruta_imagen)
print("")
