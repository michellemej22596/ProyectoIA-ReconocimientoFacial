# metodos/registro.py

import cv2
import os
from tkinter import messagebox
import face_recognition

def registrar_usuario(nombre_usuario):
    """Captura una imagen del rostro del nuevo usuario y la guarda como .jpg"""
    carpeta_destino = "usuarios/rostros"
    ruta_archivo = os.path.join(carpeta_destino, f"{nombre_usuario}.jpg")

    # Validación: ya existe ese nombre
    if os.path.exists(ruta_archivo):
        messagebox.showerror("Error", f"Ya existe un usuario con el nombre '{nombre_usuario}'.")
        return

    # Crear carpeta si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    cam = cv2.VideoCapture(0)
    print(f"[INFO] Mirá a la cámara, vamos a tomar tu foto, {nombre_usuario}...")

    while True:
        ret, frame = cam.read()
        if not ret:
            continue

        cv2.imshow(f"Capturando rostro de {nombre_usuario} - Presiona 's' para guardar, 'q' para cancelar", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Validar que haya una cara
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if not face_recognition.face_locations(rgb):
                messagebox.showerror("Error", "No se detectó ningún rostro en la imagen.")
                continue

            cv2.imwrite(ruta_archivo, frame)
            print(f"[✔] Imagen guardada en: {ruta_archivo}")
            messagebox.showinfo("Registro exitoso", f"Usuario '{nombre_usuario}' registrado correctamente.")
            break
        elif key == ord('q'):
            print("[✘] Registro cancelado.")
            break

    cam.release()
    cv2.destroyAllWindows()
