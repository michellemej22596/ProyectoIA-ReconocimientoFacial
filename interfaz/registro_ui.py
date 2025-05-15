# interfaz/registro_ui.py

import tkinter as tk
from tkinter import messagebox
from metodos.registro import registrar_usuario

print("Interfaz de registro lanzada")

def iniciar_registro_ui():
    ventana = tk.Tk()
    ventana.title("Registro de Nuevo Usuario")
    ventana.geometry("400x200")

    label = tk.Label(ventana, text="Registrar nuevo usuario", font=("Arial", 14))
    label.pack(pady=15)

    label_nombre = tk.Label(ventana, text="Nombre del usuario:")
    label_nombre.pack()

    entrada_nombre = tk.Entry(ventana, width=30)
    entrada_nombre.pack(pady=10)

    def registrar():
        nombre = entrada_nombre.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Por favor ingresa un nombre válido.")
            return
        registrar_usuario(nombre)

    btn_registrar = tk.Button(ventana, text="Registrar Rostro", command=registrar)
    btn_registrar.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_registro_ui()
