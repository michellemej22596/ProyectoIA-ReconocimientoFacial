# metodos/con_libreria.py

import cv2
import face_recognition
import os

def cargar_usuario(ruta_imagen):
    """Carga la imagen de un usuario y genera su codificación facial."""
    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"No se encontró la imagen en {ruta_imagen}")

    imagen = face_recognition.load_image_file(ruta_imagen)
    encoding = face_recognition.face_encodings(imagen)

    if not encoding:
        raise ValueError("No se pudo obtener la codificación de la imagen.")

    return encoding[0]

def reconocer_usuario(known_encoding):
    """Captura video y compara el rostro detectado con el usuario conocido."""
    video = cv2.VideoCapture(0)

    acceso_concedido = False  # 🔥 Variable para romper el bucle

    while True:
        ret, frame = video.read()
        if not ret:
            continue

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = []

        if face_locations:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            match = face_recognition.compare_faces([known_encoding], face_encoding)[0]

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            name = "Acceso permitido" if match else "Desconocido"
            color = (0, 255, 0) if match else (0, 0, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            if match:
                acceso_concedido = True
                break  # 🔥 Salir del for

        cv2.imshow('Reconocimiento Facial - face_recognition', frame)

        if acceso_concedido:
            break  # 🔥 Salir del while si ya hay acceso permitido

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    if not acceso_concedido:
        raise Exception("Acceso no permitido")


def login_con_libreria():
    """Función principal para usar el sistema de login facial con face_recognition."""
    try:
        ruta_imagen = "usuarios/rostros/persona1.jpg"
        known_encoding = cargar_usuario(ruta_imagen)
        reconocer_usuario(known_encoding)
    except Exception as e:
        print(f"Error en el login con librería: {e}")
