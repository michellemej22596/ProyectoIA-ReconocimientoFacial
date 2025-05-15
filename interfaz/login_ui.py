# interfaz/login_ui.py

import tkinter as tk
from tkinter import messagebox
from metodos.con_libreria import login_con_libreria
from interfaz.ver_historial import mostrar_historial


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

    btn_login_con_libreria = tk.Button(
        ventana,
        text="Login con Librer\u00eda",
        width=25,
        height=2,
        command=login_con_libreria_ui,
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        bd=0,
        relief="flat",
        font=("Helvetica", 10, "bold")
    )
    btn_login_con_libreria.pack(pady=10)
    btn_login_con_libreria.configure(highlightbackground="#4CAF50")
    btn_login_con_libreria.configure(cursor="hand2")

    btn_login_con_libreria.bind("<Enter>", lambda e: btn_login_con_libreria.config(bg="#45a049"))
    btn_login_con_libreria.bind("<Leave>", lambda e: btn_login_con_libreria.config(bg="#4CAF50"))

    btn_login_sin_libreria = tk.Button(
        ventana,
        text="Login sin Librer\u00eda",
        width=25,
        height=2,
        command=login_sin_libreria_ui,
        bg="#2196F3",
        fg="white",
        activebackground="#1e88e5",
        bd=0,
        relief="flat",
        font=("Helvetica", 10, "bold")
    )
    btn_login_sin_libreria.pack(pady=10)
    btn_login_sin_libreria.configure(cursor="hand2")

    btn_login_sin_libreria.bind("<Enter>", lambda e: btn_login_sin_libreria.config(bg="#1e88e5"))
    btn_login_sin_libreria.bind("<Leave>", lambda e: btn_login_sin_libreria.config(bg="#2196F3"))

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
    btn_historial.configure(cursor="hand2")

    btn_historial.bind("<Enter>", lambda e: btn_historial.config(bg="#546e7a"))
    btn_historial.bind("<Leave>", lambda e: btn_historial.config(bg="#607d8b"))


    ventana.mainloop()


def login_con_libreria_ui():
    try:
        login_con_libreria()
        mostrar_home()
    except Exception as e:
        messagebox.showerror("Error", f"Ocurri\u00f3 un error: {e}")


def login_sin_libreria_ui():
    try:
        messagebox.showinfo("En desarrollo", "Login sin librer\u00eda a\u00fan no implementado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurri\u00f3 un error: {e}")


def mostrar_home():
    ventana_home = tk.Toplevel()
    ventana_home.title("Inicio")
    ventana_home.geometry("300x200")
    ventana_home.configure(bg="#ffffff")

    label_home = tk.Label(
        ventana_home,
        text="\u00a1Login exitoso!",
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
