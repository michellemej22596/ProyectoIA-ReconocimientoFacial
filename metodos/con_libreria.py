# metodos/con_libreria.py

import cv2
import face_recognition
import os
import time  # Para medir el tiempo de ejecución

from datetime import datetime
import csv

def registrar_historial(usuario, resultado):
    """Registra en CSV el resultado del intento de acceso."""
    ruta = "resultados/historial_accesos.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([now, usuario, resultado])

def cargar_usuario(ruta_imagen):
    """Carga la imagen de un usuario y genera su codificación facial."""
    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"No se encontró la imagen en {ruta_imagen}")

    imagen = face_recognition.load_image_file(ruta_imagen)
    encoding = face_recognition.face_encodings(imagen)

    if not encoding:
        raise ValueError("No se pudo obtener la codificación de la imagen.")

    return encoding[0]

def cargar_todos_los_usuarios():
    """Carga todas las imágenes en la carpeta de rostros y devuelve codificaciones y nombres."""
    carpeta = "usuarios/rostros"
    codificaciones = []
    nombres = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            ruta = os.path.join(carpeta, archivo)
            nombre = os.path.splitext(archivo)[0]
            try:
                imagen = face_recognition.load_image_file(ruta)
                encoding = face_recognition.face_encodings(imagen)
                if encoding:
                    codificaciones.append(encoding[0])
                    nombres.append(nombre)
                else:
                    print(f"[!] No se detectó rostro en: {archivo}")
            except Exception as e:
                print(f"[!] Error al cargar {archivo}: {e}")

    return codificaciones, nombres


def reconocer_usuario(lista_encodings, lista_nombres):
    """Reconoce usuarios en vivo comparando con todos los rostros registrados."""
    video = cv2.VideoCapture(0)
    acceso_concedido = False
    nombre_detectado = "Desconocido"

    while True:
        ret, frame = video.read()
        if not ret:
            continue

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) if face_locations else []

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(lista_encodings, face_encoding)
            name = "Desconocido"

            if True in matches:
                match_index = matches.index(True)
                name = lista_nombres[match_index]
                acceso_concedido = True
                nombre_detectado = name

            top, right, bottom, left = top*4, right*4, bottom*4, left*4
            color = (0, 255, 0) if acceso_concedido else (0, 0, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            if acceso_concedido:
                break

        cv2.imshow('Reconocimiento Facial - face_recognition', frame)

        if acceso_concedido or (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    video.release()
    cv2.destroyAllWindows()

    # Registrar resultado
    if acceso_concedido:
        registrar_historial(nombre_detectado, "Permitido")
    else:
        registrar_historial("Desconocido", "Denegado")
        raise Exception("Acceso no permitido")


def login_con_libreria():
    """Función principal para usar el sistema de login facial con face_recognition."""
    try:
        start_time = time.time()  # Inicia el conteo del tiempo

        encodings, nombres = cargar_todos_los_usuarios()
        if not encodings:
            raise Exception("No hay usuarios registrados con rostros válidos.")
        
        reconocer_usuario(encodings, nombres)  # Llama a la función de reconocimiento de usuario

        end_time = time.time()  # Finaliza el conteo del tiempo
        elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
        
        # Imprimir el tiempo en la consola
        print(f"[INFO] Tiempo de ejecución con librería: {elapsed_time:.4f} segundos")

        # Aquí también puedes guardar los resultados del rendimiento en un archivo CSV
        guardar_resultados_rendimiento("Con librería", elapsed_time)
    except Exception as e:
        print(f"Error en el login con librería: {e}")


def guardar_resultados_rendimiento(metodo, tiempo):
    """Guarda los resultados de la medición de rendimiento en un archivo CSV."""
    ruta = "resultados/comparacion_rendimiento.csv"
    
    try:
        with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            # Si el archivo está vacío, escribir el encabezado
            if archivo.tell() == 0:
                escritor.writerow(["Método", "Tiempo de ejecución (segundos)"])
            
            # Escribir los resultados de ambos métodos
            escritor.writerow([metodo, tiempo])

        print(f"[INFO] Resultados guardados en: {ruta}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo de resultados: {e}")