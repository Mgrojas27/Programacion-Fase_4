import tkinter as tk
from tkinter import messagebox
from main import Cliente, DatosInvalidosError

def registrar_cliente():
    nombre = entrada_nombre.get().strip()
    documento = entrada_documento.get().strip()
    correo = entrada_correo.get().strip()

        try:
        cliente = Cliente(nombre, documento, correo)
        messagebox.showinfo(
            "Registro exitoso",
            "Cliente validado correctamente"
        )
    except DatosInvalidosError as error:
        messagebox.showerror("Error", str(error))

ventana = tk.Tk()
ventana.title("Sistema Integral de Gestión - Fase 4")
ventana.geometry("450x350")

tk.Label(ventana, text="REGISTRO DE CLIENTES",
         font=("Arial", 16, "bold")).pack(pady=15)

tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack()

tk.Label(ventana, text="Documento:").pack()
entrada_documento = tk.Entry(ventana, width=40)
entrada_documento.pack()

tk.Label(ventana, text="Correo electrónico:").pack()
entrada_correo = tk.Entry(ventana, width=40)
entrada_correo.pack()

tk.Button(ventana, text="Registrar cliente",
          command=registrar_cliente).pack(pady=20)

ventana.mainloop()
