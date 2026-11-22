import tkinter as tk
from tkinter import messagebox, ttk

from main import (
    Cliente,
    DatosInvalidosError,
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
)

clientes = []


def registrar_cliente():
    try:
        cliente = Cliente(
            entrada_nombre.get().strip(),
            entrada_documento.get().strip(),
            entrada_correo.get().strip(),
        )
        clientes.append(cliente)
        messagebox.showinfo("Registro exitoso", "Cliente validado y agregado a la sesión")
    except DatosInvalidosError as error:
        messagebox.showerror("Datos incorrectos", str(error))


def actualizar_campos(*_):
    servicio = tipo_servicio.get()
    if servicio == "Reserva de sala":
        etiqueta_detalle.config(text="Capacidad de la sala (personas):")
    elif servicio == "Alquiler de equipo":
        etiqueta_detalle.config(text="Cantidad de equipos:")
    else:
        etiqueta_detalle.config(text="Especialidad de la asesoría:")


def calcular_costo():
    try:
        nombre = entrada_servicio.get().strip()
        if not nombre:
            raise DatosInvalidosError("Ingrese el nombre del servicio")

        tarifa = float(entrada_tarifa.get().strip())
        duracion = float(entrada_duracion.get().strip())
        if tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero")
        if duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero")

        detalle = entrada_detalle.get().strip()
        servicio_elegido = tipo_servicio.get()

        if servicio_elegido == "Reserva de sala":
            servicio = ReservaSala(nombre, tarifa, int(detalle))
        elif servicio_elegido == "Alquiler de equipo":
            servicio = AlquilerEquipo(nombre, tarifa, int(detalle))
        else:
            servicio = AsesoriaEspecializada(nombre, tarifa, detalle)

        costo = servicio.calcular_costo(duracion)
        resultado.config(
            text=f"Costo total: ${costo:,.2f} COP",
        )
        messagebox.showinfo(
            "Resultado del servicio",
            f"{servicio.describir_servicio()}\n"
            f"Duración: {duracion:g} horas\n"
            f"Costo total: ${costo:,.2f} COP",
        )
    except (ValueError, DatosInvalidosError) as error:
        resultado.config(text="Revise los datos ingresados")
        messagebox.showerror("Error de validación", str(error))


ventana = tk.Tk()
ventana.title("Sistema Integral de Gestión - Fase 4")
ventana.geometry("620x700")
ventana.minsize(560, 650)

contenedor = ttk.Frame(ventana, padding=20)
contenedor.pack(fill="both", expand=True)


ttk.Label(contenedor, text="REGISTRO DE CLIENTES", font=("Arial", 16, "bold")).pack(pady=(0, 12))

ttk.Label(contenedor, text="Nombre:").pack()
entrada_nombre = ttk.Entry(contenedor, width=43)
entrada_nombre.pack(pady=(0, 6))

ttk.Label(contenedor, text="Documento:").pack()
entrada_documento = ttk.Entry(contenedor, width=43)
entrada_documento.pack(pady=(0, 6))

ttk.Label(contenedor, text="Correo electrónico:").pack()
entrada_correo = ttk.Entry(contenedor, width=43)
entrada_correo.pack(pady=(0, 6))

ttk.Button(contenedor, text="Registrar cliente", command=registrar_cliente).pack(pady=(6, 15))

ttk.Separator(contenedor, orient="horizontal").pack(fill="x", pady=8)

ttk.Label(contenedor, text="GESTIÓN DE SERVICIOS Y RESERVAS", font=("Arial", 14, "bold")).pack(pady=(8, 12))

ttk.Label(contenedor, text="Tipo de servicio:").pack()
tipo_servicio = tk.StringVar(value="Reserva de sala")
selector = ttk.Combobox(
    contenedor,
    textvariable=tipo_servicio,
    values=["Reserva de sala", "Alquiler de equipo", "Asesoría especializada"],
    state="readonly",
    width=40,
)
selector.pack(pady=(0, 8))
selector.bind("<<ComboboxSelected>>", actualizar_campos)

ttk.Label(contenedor, text="Nombre de la sala, equipo o asesoría:").pack()
entrada_servicio = ttk.Entry(contenedor, width=43)
entrada_servicio.pack(pady=(0, 8))

ttk.Label(contenedor, text="Tarifa por hora (COP):").pack()
entrada_tarifa = ttk.Entry(contenedor, width=43)
entrada_tarifa.pack(pady=(0, 8))

etiqueta_detalle = ttk.Label(contenedor, text="Capacidad de la sala (personas):")
etiqueta_detalle.pack()
entrada_detalle = ttk.Entry(contenedor, width=43)
entrada_detalle.pack(pady=(0, 8))

ttk.Label(contenedor, text="Duración (horas):").pack()
entrada_duracion = ttk.Entry(contenedor, width=43)
entrada_duracion.pack(pady=(0, 10))

ttk.Button(contenedor, text="Calcular costo del servicio", command=calcular_costo).pack(pady=8)
resultado = ttk.Label(contenedor, text="Costo total: pendiente", font=("Arial", 12, "bold"))
resultado.pack(pady=8)

ttk.Label(contenedor, text="Los registros se conservan solo mientras el programa esté abierto.", font=("Arial", 9)).pack(pady=(8, 0))

ventana.mainloop()
