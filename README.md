````markdown
# Proyecto IA - Reconocimiento Facial
Michelle Mejía 22596 - Silvia Illescas 22376

Este proyecto implementa un sistema de **reconocimiento facial** utilizando las librerías `face_recognition` para el reconocimiento avanzado y `Tkinter` para la interfaz gráfica. El sistema permite registrar usuarios, autenticar mediante el rostro y registrar el historial de accesos. Además, incluye un análisis de rendimiento al comparar el uso de la librería `face_recognition` contra una implementación manual de comparación de rostros sin librerías.

## Requisitos

Este proyecto requiere las siguientes librerías de Python:

- `opencv-python`: Para la captura de video desde la cámara y el procesamiento de imágenes.
- `face_recognition`: Para el reconocimiento facial utilizando técnicas avanzadas.
- `tkinter`: Para crear la interfaz gráfica de usuario.
- `csv`: Para manejar el almacenamiento de datos como el historial de accesos.

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install opencv-python face_recognition
````

> **Nota**: `tkinter` viene preinstalado con la mayoría de las distribuciones de Python.

## Características

1. **Registro de usuarios:**

   * Permite registrar un nuevo usuario mediante la captura de una imagen de su rostro.
   * El nombre del usuario se asocia con la imagen y se guarda en la carpeta `usuarios/rostros`.

2. **Login con reconocimiento facial:**

   * Compara el rostro capturado con las imágenes registradas para permitir o denegar el acceso.
   * Ofrece dos métodos de comparación: usando la librería `face_recognition` y otro basado en histogramas de imágenes sin librerías avanzadas.

3. **Historial de accesos:**

   * Se guarda un historial de los accesos realizados, registrando la fecha y el usuario.
   * El historial se almacena en un archivo CSV (`historial_accesos.csv`) para futuras consultas.

4. **Análisis de rendimiento:**

   * Compara el rendimiento entre el método de reconocimiento facial utilizando la librería `face_recognition` y el método sin librerías avanzadas, midiendo el tiempo de ejecución de ambos métodos.
   * Los resultados de rendimiento se guardan en un archivo CSV (`comparacion_rendimiento.csv`).

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
PROYECTOIA-ReconocimientoFacial/
│
├── interfaz/
│   ├── __init__.py
│   ├── login_ui.py           # Interfaz de inicio de sesión
│   ├── registro_ui.py        # Interfaz de registro de usuarios
│   ├── ver_historial.py      # Interfaz para ver el historial de accesos
│
├── metodos/
│   ├── __init__.py
│   ├── con_libreria.py       # Lógica de login con la librería `face_recognition`
│   ├── sin_libreria.py       # Lógica de login sin usar librerías avanzadas
│   ├── registro.py           # Funciones relacionadas con el registro de usuarios
│
├── resultados/
│   ├── comparacion_rendimiento.csv  # Archivo con la comparación de tiempos de ejecución
│   ├── historial_accesos.csv        # Historial de accesos de los usuarios
│
├── usuarios/rostros/
│   ├── Marconi.jpg        # Imagen de usuario registrada
│   ├── Michelle.jpg       # Imagen de usuario registrada
│   ├── Ruben.jpg          # Imagen de usuario registrada
│
├── utils/
│   ├── preprocesamiento.py   # Funciones auxiliares para el procesamiento de imágenes
│
├── .gitignore               # Para ignorar archivos no necesarios en Git
├── main.py                  # Archivo principal para ejecutar la aplicación
└── README.md                # Este archivo
```

## Cómo usar

1. **Registrar un nuevo usuario:**

   * Introduce un nombre en el campo correspondiente y presiona el botón "Abrir cámara y registrar rostro".
   * El sistema abrirá la cámara y registrará la imagen del rostro para el usuario especificado.

2. **Login con reconocimiento facial:**

   * Para iniciar sesión, el sistema comparará el rostro en vivo con los registros de rostros guardados.
   * Puedes elegir entre dos métodos de reconocimiento: usando `face_recognition` o sin librerías avanzadas.

3. **Ver historial de accesos:**

   * Puedes consultar el historial de accesos de todos los intentos de inicio de sesión realizados.

4. **Análisis de rendimiento:**

   * El proyecto mide y compara el tiempo de ejecución de los métodos de reconocimiento facial con y sin librerías, y guarda los resultados en un archivo CSV para analizar el rendimiento.

## Comparación de Métodos

### Reconocimiento con Librerías (`face_recognition`)

Este método utiliza la librería `face_recognition` para detectar y comparar rostros. Este enfoque es más preciso y rápido, ya que utiliza técnicas avanzadas de aprendizaje automático y procesamiento de imágenes.

### Reconocimiento sin Librerías

Este método no utiliza librerías avanzadas. En su lugar, se basa en el análisis de histogramas de imágenes (luminancia y color) para realizar la comparación de rostros. Aunque no es tan preciso como el primer método, es una alternativa interesante que no depende de librerías externas avanzadas.

## Resultados de Rendimiento

Los resultados de la comparación de los métodos de reconocimiento facial en cuanto al tiempo de ejecución y el rendimiento se guardan en el archivo `resultados/comparacion_rendimiento.csv`. Este archivo contiene los tiempos de ejecución para ambos métodos y permite visualizar cuál es el más eficiente.

