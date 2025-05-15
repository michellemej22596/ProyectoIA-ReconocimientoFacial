# interfaz/ver_historial.py

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

def mostrar_historial():
    ruta_csv = "resultados/historial_accesos.csv"

    if not os.path.exists(ruta_csv):
        messagebox.showerror("Error", "No se encontr\u00f3 el archivo de historial.")
        return

    ventana = tk.Toplevel()
    ventana.title("Historial de Accesos")
    ventana.geometry("500x400")
    ventana.configure(bg="#f0f2f5")

    label = tk.Label(
        ventana,
        text="Historial de Accesos",
        font=("Helvetica", 16, "bold"),
        bg="#f0f2f5",
        fg="#333"
    )
    label.pack(pady=15)

    columnas = ("fecha", "usuario", "resultado")
    estilo = ttk.Style()
    estilo.configure("Treeview",
                     background="#ffffff",
                     foreground="#333333",
                     rowheight=25,
                     fieldbackground="#ffffff",
                     font=("Helvetica", 10))
    estilo.configure("Treeview.Heading",
                     font=("Helvetica", 10, "bold"),
                     background="#e0e0e0",
                     foreground="#000")
    estilo.map("Treeview",
               background=[("selected", "#90caf9")])

    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

    tabla.heading("fecha", text="Fecha y Hora")
    tabla.heading("usuario", text="Usuario")
    tabla.heading("resultado", text="Resultado")

    tabla.column("fecha", width=180, anchor="w")
    tabla.column("usuario", width=120, anchor="center")
    tabla.column("resultado", width=100, anchor="center")

    tabla.pack(padx=15, pady=10)

    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) == 3:
                tabla.insert("", tk.END, values=fila)

    btn_cerrar = tk.Button(
        ventana,
        text="Cerrar",
        command=ventana.destroy,
        bg="#f44336",
        fg="white",
        activebackground="#d32f2f",
        bd=0,
        relief="flat",
        font=("Helvetica", 10, "bold")
    )
    btn_cerrar.pack(pady=10)
    btn_cerrar.configure(cursor="hand2")
    btn_cerrar.bind("<Enter>", lambda e: btn_cerrar.config(bg="#d32f2f"))
    btn_cerrar.bind("<Leave>", lambda e: btn_cerrar.config(bg="#f44336"))
