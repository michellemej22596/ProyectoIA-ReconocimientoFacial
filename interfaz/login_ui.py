import tkinter as tk
from tkinter import messagebox
from metodos.con_libreria import login_con_libreria
from metodos.sin_libreria import login_sin_libreria
from interfaz.registro_ui import iniciar_registro_ui
import tkinter.font as tkFont
from interfaz.ver_historial import mostrar_historial


def login_sin_libreria_ui():
    """Inicia login usando nuestra propia implementación de reconocimiento facial."""
    try:
        login_sin_libreria()  # Llama la función sin librería
        mostrar_home()  # Si el acceso es exitoso, muestra la pantalla Home
    except Exception as e:
        messagebox.showerror("Acceso denegado", f"Ocurrió un error: {e}")


def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema de Login Facial")
    ventana.geometry("400x300")
    ventana.configure(bg="#f0f2f5")

    label_bienvenida = tk.Label(
        ventana,
        text="Bienvenido al Sistema de Login Facial",
        font=("Helvetica", 14, "bold"),
        bg="#f0f2f5",
        fg="#333"
    )
    label_bienvenida.pack(pady=20)

    # Establecemos la fuente personalizada
    fuente_boton = tkFont.Font(family="Segoe UI", size=10)

    # Frame para los botones de login
    frame_boton = tk.Frame(ventana, bg="#f0f2f5")
    frame_boton.pack(pady=30)

    # Botón para login con librería
    btn_login_con_libreria = tk.Button(
        frame_boton,
        text="Login con Librería",
        width=15,
        height=2,
        command=login_con_libreria_ui,
        bg="#6BACC5",
        fg="white",
        activebackground="#6BACC5",
        bd=0,
        relief="flat",
        font=fuente_boton
    )
    btn_login_con_libreria.grid(row=0, column=0, padx=5, pady=5)

    # Botón para login sin librería
    btn_login_sin_libreria = tk.Button(
        frame_boton,
        text="Login sin Librería",
        width=15,
        height=2,
        command=login_sin_libreria_ui,
        bg="#6BACC5",
        fg="white",
        activebackground="#6BACC5",
        bd=0,
        relief="flat",
        font=fuente_boton
    )
    btn_login_sin_libreria.grid(row=0, column=1, padx=5, pady=5)

    # Botón de registro de usuario
    btn_registrar_usuario = tk.Button(
        ventana,
        text="Registrar Nuevo Usuario",
        width=25,
        height=2,
        command=iniciar_registro_ui,  # Abre la ventana de registro
        bg="#6C9CC0",
        fg="white",
        activebackground="#5972B1",
        bd=0,
        relief="flat",
        font=("Helvetica", 10, "bold")
    )
    btn_registrar_usuario.pack(pady=10)

    # Botón de ver historial de accesos
    btn_historial = tk.Button(
        ventana,
        text="Ver historial de accesos",
        width=25,
        height=1,
        command=mostrar_historial,
        bg="#607d8b",
        fg="white",
        activebackground="#546e7a",
        bd=0,
        relief="flat",
        font=("Helvetica", 10, "bold")
    )
    btn_historial.pack(side="bottom", pady=10)

    ventana.mainloop()


def login_con_libreria_ui():
    try:
        login_con_libreria()  # Llama la función con librería
        mostrar_home()  # Si el acceso es exitoso, muestra la pantalla Home
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def mostrar_home():
    """Pantalla Mock de Home después de login exitoso."""
    ventana_home = tk.Toplevel()
    ventana_home.title("Inicio")
    ventana_home.geometry("300x200")
    ventana_home.configure(bg="#ffffff")

    label_home = tk.Label(
        ventana_home,
        text="¡Login exitoso!",
        font=("Helvetica", 16, "bold"),
        bg="#ffffff",
        fg="#4CAF50"
    )
    label_home.pack(pady=30)

    label_bienvenida = tk.Label(
        ventana_home,
        text="Bienvenido al sistema.",
        bg="#ffffff",
        fg="#333"
    )
    label_bienvenida.pack(pady=10)

    btn_salir = tk.Button(
        ventana_home,
        text="Salir",
        command=ventana_home.destroy,
        bg="#f44336",
        fg="white",
        activebackground="#d32f2f",
        bd=0,
        relief="flat",
        font=("Helvetica", 10, "bold")
    )
    btn_salir.pack(pady=20)
    btn_salir.configure(cursor="hand2")
    btn_salir.bind("<Enter>", lambda e: btn_salir.config(bg="#d32f2f"))
    btn_salir.bind("<Leave>", lambda e: btn_salir.config(bg="#f44336"))
