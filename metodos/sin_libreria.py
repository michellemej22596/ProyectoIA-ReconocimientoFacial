# metodos/sin_libreria.py

import cv2
import os
import numpy as np
from datetime import datetime
import csv
import time  # Para medir el rendimiento

# Cargar Haar Cascade para detectar rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def registrar_historial(usuario, resultado):
    """Registra en CSV el resultado del intento de acceso."""
    ruta = "resultados/historial_accesos.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([now, usuario, resultado])

def calcular_histograma(rostro):
    """Devuelve un histograma normalizado del rostro en escala de grises"""
    rostro_gray = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([rostro_gray], [0], None, [256], [0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def cargar_histogramas():
    """Carga todos los rostros registrados y guarda sus histogramas"""
    base = "usuarios/rostros"
    histogramas = []
    nombres = []

    for archivo in os.listdir(base):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            ruta = os.path.join(base, archivo)
            imagen = cv2.imread(ruta)
            rostros = face_cascade.detectMultiScale(cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5)

            if len(rostros) > 0:
                x, y, w, h = rostros[0]
                rostro = imagen[y:y+h, x:x+w]
                hist = calcular_histograma(rostro)
                histogramas.append(hist)
                nombres.append(os.path.splitext(archivo)[0])
            else:
                print(f"[!] No se detectó rostro en {archivo}")

    return histogramas, nombres

def login_sin_libreria():
    """Inicia el proceso de login facial sin usar face_recognition"""
    histogramas_base, nombres = cargar_histogramas()
    if not histogramas_base:
        print("No se encontraron rostros registrados.")
        return

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("[ERROR] No se pudo abrir la cámara.")
        return

    acceso_concedido = False
    nombre_detectado = "Desconocido"
    umbral_similitud = 0.8  # Umbral ajustable para la similitud

    # Iniciar el conteo de tiempo
    start_time = time.time()

    frame_count = 0  # Inicializa el contador de fotogramas

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostros = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in rostros:
            rostro_capturado = frame[y:y+h, x:x+w]
            hist_capturado = calcular_histograma(rostro_capturado)

            # Comparar con los histogramas de los rostros registrados
            distancias = [cv2.norm(hist_capturado - hist, cv2.NORM_L2) for hist in histogramas_base]
            idx_min = np.argmin(distancias)
            distancia_minima = distancias[idx_min]

            # Ajustar el umbral de similitud
            if distancia_minima < umbral_similitud:
                acceso_concedido = True
                nombre_detectado = nombres[idx_min]
                color = (0, 255, 0)  # Verde si se detecta al usuario
            else:
                color = (0, 0, 255)  # Rojo si no se detecta al usuario

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, nombre_detectado, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            break  # Solo consideramos el primer rostro detectado

        # Calcular FPS
        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time

        # Mostrar FPS en la pantalla
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.imshow("Login sin Librería", frame)

        if acceso_concedido or (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cam.release()
    cv2.destroyAllWindows()

    # Finalizar el conteo de tiempo
    end_time = time.time()
    elapsed_time = end_time - start_time  # Calcula el tiempo total de ejecución
    print(f"[INFO] Tiempo de ejecución sin librería: {elapsed_time:.4f} segundos")

    # Guardar el rendimiento en un archivo CSV
    guardar_resultados_rendimiento("Sin librería", elapsed_time)

    if acceso_concedido:
        registrar_historial(nombre_detectado, "Permitido")
    else:
        registrar_historial("Desconocido", "Denegado")
        raise Exception("Acceso no permitido")

def guardar_resultados_rendimiento(metodo, tiempo):
    """Guarda los resultados de la medición de rendimiento en un archivo CSV."""
    ruta = "resultados/comparacion_rendimiento.csv"
    
    try:
        with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            if archivo.tell() == 0:
                escritor.writerow(["Método", "Tiempo de ejecución (segundos)"])
            
            escritor.writerow([metodo, tiempo])

        print(f"[INFO] Resultados guardados en: {ruta}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo de resultados: {e}")
