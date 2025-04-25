# interfaz/login_ui.py

import tkinter as tk
from tkinter import messagebox
from metodos.con_libreria import login_con_libreria
# Aquí después importaremos el sin_libreria cuando esté listo

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema de Login Facial")
    ventana.geometry("400x300")

    label_bienvenida = tk.Label(ventana, text="Bienvenido al Sistema de Login Facial", font=("Arial", 14))
    label_bienvenida.pack(pady=20)

    btn_login_con_libreria = tk.Button(ventana, text="Login con Librería", width=25, height=2, command=login_con_libreria_ui)
    btn_login_con_libreria.pack(pady=10)

    btn_login_sin_libreria = tk.Button(ventana, text="Login sin Librería", width=25, height=2, command=login_sin_libreria_ui)
    btn_login_sin_libreria.pack(pady=10)

    ventana.mainloop()

def login_con_libreria_ui():
    """Iniciar login usando la librería face_recognition."""
    try:
        login_con_libreria()
        mostrar_home()
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def login_sin_libreria_ui():
    """Iniciar login usando nuestra propia implementación."""
    try:
        # Aquí llamaríamos el método propio cuando esté listo
        # from metodos.sin_libreria import login_sin_libreria
        # login_sin_libreria()
        messagebox.showinfo("En desarrollo", "Login sin librería aún no implementado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def mostrar_home():
    """Pantalla Mock de Home después de login exitoso."""
    ventana_home = tk.Toplevel()
    ventana_home.title("Inicio")
    ventana_home.geometry("300x200")

    label_home = tk.Label(ventana_home, text="¡Login exitoso!", font=("Arial", 16))
    label_home.pack(pady=30)

    label_bienvenida = tk.Label(ventana_home, text="Bienvenido al sistema.")
    label_bienvenida.pack(pady=10)

    btn_salir = tk.Button(ventana_home, text="Salir", command=ventana_home.destroy)
    btn_salir.pack(pady=20)
