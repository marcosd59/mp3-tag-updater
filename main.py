#####################################################################################
#     File Name           :     main.py
#     Created By          :     Marcos Damian Pool Canul
#     Creation Date       :     [2024-01-12 10:10]
#     Last Modified       :     [2024-08-25 20:10]
#     Description         :     Permite seleccionar y ejecutar diversas operaciones
#                               de manipulación de metadatos de archivos MP3 y FLAC.
#####################################################################################

import os
from pista import modificar_numero_pista
from album import renombrar_album
from genero import modificar_genero
from titulo import cambiar_titulo


def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("Seleccione una opción:")
    print("1. Modificar número de pista")
    print("2. Renombrar álbum")
    print("3. Modificar género")
    print("4. Cambiar título")
    print("5. Salir")


def ejecutar_opcion(opcion, ruta):
    """
    Ejecuta la opción seleccionada por el usuario.

    :param opcion: Opción seleccionada por el usuario.
    :param ruta: Ruta de la carpeta que contiene los archivos de música.
    """
    if opcion == '1':
        modificar_numero_pista(ruta)
    elif opcion == '2':
        album = input("Ingrese el nuevo nombre del álbum: ")
        renombrar_album(ruta, album)
    elif opcion == '3':
        genero = input("Ingrese el nuevo género: ")
        modificar_genero(ruta, genero)
    elif opcion == '4':
        cambiar_titulo(ruta)
    elif opcion == '5':
        print("Saliendo del programa...")
        return False
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
    return True


def main():
    """
    Función principal que controla el flujo del programa.
    """
    ruta = input("Ingrese la ruta de la carpeta con los archivos de música: ")

    if not os.path.isdir(ruta):
        print("La ruta ingresada no es válida. Por favor, verifique e intente de nuevo.")
        return

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        if not ejecutar_opcion(opcion, ruta):
            break
        print("")


if __name__ == "__main__":
    main()
