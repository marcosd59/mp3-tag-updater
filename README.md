# MP3 Tag Updater

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## Descripción

El proyecto **MP3 Tag Updater** es una herramienta basada en Python que permite modificar metadatos en archivos de música, específicamente en formatos MP3 y FLAC. Este proyecto facilita la edición de los metadatos como el número de pista, el álbum, el género, el título de las canciones y la portada de los archivos en una carpeta específica. Es ideal para aquellos que desean organizar y mantener actualizada su colección de música.

## Características

- **Modificar número de pista:** Actualiza el número de pista en los metadatos de archivos MP3 y FLAC.
- **Renombrar álbum:** Cambia el nombre del álbum en los archivos de música seleccionados.
- **Modificar género:** Ajusta el género musical en los archivos MP3 y FLAC.
- **Cambiar título:** Permite cambiar el título de cada canción en una carpeta.
- **Cambiar intérpretes colaboradores:** Actualiza los intérpretes colaboradores de tus canciones en MP3 y FLAC.
- **Cambiar portada de canciones:** Reemplaza la imagen de portada de los archivos MP3 y FLAC en una carpeta.

## Estructura del proyecto

El proyecto se organiza de la siguiente manera:

```plaintext
mp3-tag-updater/
│
├── pista.py                  # Modificar número de pista
├── album.py                  # Renombrar álbum
├── genero.py                 # Modificar género
├── titulo.py                 # Cambiar título
├── interpretes.py            # Cambiar intérpretes colaboradores
├── cambiar_cover.py          # Cambiar el cover de las canciones
├── renombrar_pistas.py       # Renombrar canciones en orden alfabético con prefijo numérico
├── main.py                   # Archivo principal que centraliza todas las funcionalidades
└── README.md                 # Documentación del proyecto
```

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/marcosd59/mp3-tag-updater.git
   cd mp3-tag-updater
   ```

2. **Instala las dependencias:**

   Asegúrate de tener instalado `mutagen` para manipular los metadatos de los archivos:

   ```bash
   pip install mutagen
   ```

## Uso

Para utilizar las funcionalidades del proyecto, ejecuta el archivo `main.py`:

```bash
python main.py
```

A continuación, se te pedirá que ingreses la ruta de la carpeta que contiene los archivos de música y se te mostrará un menú interactivo con las opciones disponibles:

1. Modificar número de pista
2. Renombrar álbum
3. Modificar género
4. Cambiar título
5. Cambiar intérpretes colaboradores
6. Cambiar portada de las canciones
7. Renombrar canciones en orden alfabético con prefijo numérico
8. Salir

### Ejemplo de uso

Imagina que tienes una carpeta de música en `C:\Users\Marco\Music\Vocaloid` y deseas cambiar la portada de todas las canciones. Simplemente selecciona la opción "Cambiar portada de las canciones", elige la imagen que deseas usar como portada y listo.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, siéntete libre de hacer un fork y enviar un pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

## Contacto

Desarrollado por Marcos Pool - [GitHub](https://github.com/marcosd59)
