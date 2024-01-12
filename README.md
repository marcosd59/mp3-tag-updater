# mp3-tag-updater

## Descripción
Este proyecto proporciona herramientas para actualizar los metadatos de archivos de música en formato MP3 y FLAC. Actualiza el número de pista, el nombre del álbum y el género de las canciones de forma independiente.

## Funcionalidades
- Renombra archivos MP3 según el número de pista y agrega el nombre del álbum.
- Actualiza los metadatos del álbum y del intérprete colaborador en cada archivo MP3.
- Personalización del nombre del álbum y del intérprete colaborador por parte del usuario.

## Archivos
- **main.py**: Versión 2.0 del mp3-tag-updater. Combina funcionalidades de renombrar número de pista, álbum y género.
  
- **pista.py**: Actualiza solo el número de pista de las canciones.

- **album.py**: Actualiza solo el nombre del álbum de las canciones.

- **genero.py**: Actualiza solo el género de las canciones.

## Uso
- **main.py**: Ejecuta `main.py` y sigue las instrucciones para ingresar la ruta de la carpeta, el nombre del álbum y el género.

- **pista.py**: Ejecuta `pista.py` para modificar el número de pista de todas las canciones en una carpeta.

- **album.py**: Ejecuta `album.py` para modificar solo el nombre del álbum de las canciones en una carpeta.

- **genero.py**: Ejecuta `genero.py` para modificar solo el género de las canciones en una carpeta.

## Ejemplos de Uso
```bash
python main.py
```

```bash
python pista.py
```

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
