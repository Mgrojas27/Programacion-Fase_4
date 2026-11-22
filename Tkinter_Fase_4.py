import tkinter as tk
from tkinter import messagebox
from main import Cliente, DatosInvalidosError, ReservaSala

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
def calcular_reserva():
    try:
        nombre = entrada_sala.get().strip()
        tarifa = float(entrada_tarifa.get())
        capacidad = int(entrada_capacidad.get())
        duracion = float(entrada_duracion.get())

        if not nombre:
            raise DatosInvalidosError("Ingrese el nombre de la sala")

        sala = ReservaSala(nombre, tarifa, capacidad)
        costo = sala.calcular_costo(duracion)

        messagebox.showinfo(
            "Costo de reserva",
            f"El costo total es: ${costo:,.2f}"
        )

    except (ValueError, DatosInvalidosError) as error:
        messagebox.showerror(
            "Error",
            f"Verifique los datos ingresados: {error}"
        )

ventana = tk.Tk()
ventana.title("Sistema Integral de Gestión - Fase 4")
ventana.geometry("600x600")

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
tk.Label(
    ventana,
    text="GESTIÓN DE SERVICIOS Y RESERVAS",
    font=("Arial", 14, "bold")
).pack(pady=15)

tk.Label(
    ventana,
    text="Seleccione el tipo de servicio:"
).pack(pady=5)

tipo_servicio = tk.StringVar(value="Reserva de sala")

opciones_servicio = [
    "Reserva de sala",
    "Alquiler de equipo",
    "Asesoría especializada"
]

menu_servicios = tk.OptionMenu(
    ventana,
    tipo_servicio,
    *opciones_servicio
)
menu_servicios.pack(pady=10)
tk.Label(ventana, text="Nombre de la sala:").pack()
entrada_sala = tk.Entry(ventana, width=25)
entrada_sala.pack()
tk.Label(ventana, text="Tarifa por hora ($):").pack()
entrada_tarifa = tk.Entry(ventana, width=25)
entrada_tarifa.pack()

tk.Label(ventana, text="Capacidad de la sala (personas):").pack()
entrada_capacidad = tk.Entry(ventana, width=25)
entrada_capacidad.pack()

tk.Label(ventana, text="Duración de la reserva (horas):").pack()
entrada_duracion = tk.Entry(ventana, width=25)
entrada_duracion.pack()
tk.Button(
    ventana,
    text="Calcular costo de reserva",
    command=calcular_reserva
).pack(pady=10)
ventana.mainloop()
