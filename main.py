# Fase 4
# Sistema Integral de Gestion de Clientes, Servicios y Reservas

from abc import ABC, abstractmethod
import logging
import tkinter as tk
from tkinter import ttk, messagebox

# datos incorrectos
class DatosInvalidosError(Exception):
    pass


# gestion de clientes
class Cliente:
    def __init__(self, nombre, documento, correo):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.validar_datos()

    def validar_datos(self):
        try:
            if not self.nombre.strip():
                raise DatosInvalidosError(
                    "El nombre no puede estar vacio"
                )

            if not str(self.documento).isdigit():
                raise DatosInvalidosError(
                    "El documento debe contener solo numeros"
                )

            if "@" not in self.correo:
                raise DatosInvalidosError(
                    "El correo electronico no es valido"
                )

        except DatosInvalidosError as error:
            print(f"Error al registrar cliente: {error}")
            raise

    def mostrar_cliente(self):
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Correo: {self.correo}")

def main():
    print("======================================")
    print(" SISTEMA DE GESTION - SOFTWARE FJ")
    print("======================================")
    print("Bienvenido al sistema")
    print("Proyecto Fase 4")

    print("\nPRUEBA 1: Cliente valido")
    try:
        cliente1 = Cliente(
            "Milton Rojas",
            "123456789",
            "milro@gmail.com"
        )
        cliente1.mostrar_cliente()
    except DatosInvalidosError:
        print("No fue posible registrar el cliente")

    print("\nPRUEBA 2: Cliente sin nombre")
    try:
        cliente2 = Cliente(
            "",
            "987654321",
            "cliente@gmail.com"
        )
        cliente2.mostrar_cliente()
    except DatosInvalidosError:
        print("El sistema controlo el error correctamente")

    print("\nPRUEBA 3: Documento incorrecto")
    try:
        cliente3 = Cliente(
            "Ana Gomez",
            "ABC123",
            "ana@gmail.com"
        )
        cliente3.mostrar_cliente()
    except DatosInvalidosError:
        print("El sistema controlo el error correctamente")


# Clase abstracta para los servicios
class Servicio(ABC):

    def __init__(self, nombre, tarifa):
        if not nombre or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio no puede estar vacio"
            )

        if tarifa <= 0:
            raise DatosInvalidosError(
                "La tarifa debe ser mayor que cero"
            )

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

# Servicio especializado: reserva de salas
class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa, capacidad):
        super().__init__(nombre, tarifa)
        self.capacidad = capacidad
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.capacidad, int) or self.capacidad <= 0:
            raise DatosInvalidosError(
                "La capacidad de la sala debe ser un entero positivo"
            )

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero"
            )
        return self.tarifa * duracion

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre}, "
            f"Capacidad: {self.capacidad} personas, "
            f"Tarifa por hora: ${self.tarifa}"
        )

# Servicio especializado: alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa, cantidad):
        super().__init__(nombre, tarifa)
        self.cantidad = cantidad
        self.validar_parametros()

    def validar_parametros(self):
        if type(self.cantidad) is not int or self.cantidad <= 0:
            raise DatosInvalidosError(
                "La cantidad de equipos debe ser un entero positivo"
            )

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero"
            )
        return self.tarifa * duracion * self.cantidad

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre}, "
            f"Cantidad: {self.cantidad} equipos, "
            f"Tarifa por equipo y hora: ${self.tarifa}"
        )


# Servicio especializado: asesoria especializada
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa, especialidad):
        super().__init__(nombre, tarifa)
        self.especialidad = especialidad
        self.validar_parametros()

    def validar_parametros(self):
        if not self.especialidad.strip():
            raise DatosInvalidosError(
                "La especialidad no puede estar vacia"
            )

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero"
            )
        return self.tarifa * duracion

    def describir_servicio(self):
        return (
            f"Servicio: {self.nombre}, "
            f"Especialidad: {self.especialidad}, "
            f"Tarifa por hora: ${self.tarifa}"
        )

if __name__ == "__main__":
    main()
