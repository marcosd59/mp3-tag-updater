# mp3-tag-updater

## Descripción
Este script en Python proporciona una solución eficiente para organizar y actualizar archivos de música en formato MP3 en una carpeta específica. Utiliza la biblioteca Mutagen para renombrar archivos MP3 según su número de pista, agregar el nombre del álbum y actualizar los metadatos del álbum y del intérprete colaborador.

## Funcionalidades
- Renombra archivos MP3 según el número de pista y agrega el nombre del álbum.
- Actualiza los metadatos del álbum y del intérprete colaborador en cada archivo MP3.
- Personalización del nombre del álbum y del intérprete colaborador por parte del usuario.

## Uso
1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/marcosd59/mp3-tag-updater.git
    ```

2. **Ejecutar el script:**
    ```bash
    cd mp3-tag-updater
    python main.py
    ```
    Se te pedirá que ingreses la ruta de la carpeta con los archivos MP3 y el nombre del álbum.

## Requisitos
- Python 3.x
- Mutagen library (instalable con `pip install mutagen`)

## Contribuciones
¡Contribuciones son bienvenidas! Si encuentras algún problema, tienes una sugerencia o quieres agregar una nueva funcionalidad, no dudes en abrir un [issue](https://github.com/marcosd59/mp3-tag-updater/issues) o enviar un [pull request](https://github.com/marcosd59/mp3-tag-updater/pulls).
