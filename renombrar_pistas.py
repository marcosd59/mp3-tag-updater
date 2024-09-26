#####################################################################################
#     File Name           :     renombrar_pistas.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-09-29 10:10]
#     Last Modified       :     [2024-09-29 10:17]
#     Description         :     Renombra los archivos de música en orden alfabético
#                               y les agrega un prefijo numérico.
#####################################################################################

import os


def renombrar_pistas(ruta):
    """
    Renombra los archivos de música en orden alfabético y les agrega un prefijo numérico.

    :param ruta: Ruta de la carpeta que contiene los archivos de música.
    """
    archivos = os.listdir(ruta)
    archivos_musica = [
        archivo for archivo in archivos if archivo.lower().endswith((".mp3", ".flac"))
    ]

    # Ordena los archivos por nombre de forma alfabética
    archivos_musica.sort()

    # Renombra los archivos
    for indice, archivo in enumerate(archivos_musica, start=1):
        # Genera el nuevo nombre con formato "NN - Nombre de la pista"
        nombre_antiguo, extension = os.path.splitext(archivo)
        nuevo_nombre = f"{indice:02d} - {nombre_antiguo}{extension}"

        ruta_antigua = os.path.join(ruta, archivo)
        ruta_nueva = os.path.join(ruta, nuevo_nombre)

        # Renombra el archivo
        os.rename(ruta_antigua, ruta_nueva)

        print(f"Renombrado: {archivo} -> {nuevo_nombre}")


# Ruta de la carpeta con las canciones
ruta = r"C:\Users\Marco\Music\Vocaloid"

print("")
renombrar_pistas(ruta)
print("")
