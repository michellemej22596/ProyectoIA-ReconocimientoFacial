# metodos/sin_libreria.py

import cv2
import os
import numpy as np
from datetime import datetime
import csv

# Utiliza haarcascade preentrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def registrar_historial(usuario, resultado):
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
    acceso_concedido = False
    nombre_detectado = "Desconocido"

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostros = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in rostros:
            rostro_capturado = frame[y:y+h, x:x+w]
            hist_capturado = calcular_histograma(rostro_capturado)

            distancias = [cv2.norm(hist_capturado - h, cv2.NORM_L2) for h in histogramas_base]
            idx_min = np.argmin(distancias)
            distancia_minima = distancias[idx_min]

            # Umbral ajustable según pruebas
            if distancia_minima < 0.5:
                acceso_concedido = True
                nombre_detectado = nombres[idx_min]
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, nombre_detectado, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            break  # solo consideramos el primer rostro detectado

        cv2.imshow("Login sin Librería", frame)

        if acceso_concedido or (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cam.release()
    cv2.destroyAllWindows()

    if acceso_concedido:
        registrar_historial(nombre_detectado, "Permitido")
    else:
        registrar_historial("Desconocido", "Denegado")
        raise Exception("Acceso no permitido")
