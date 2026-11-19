
# Fase 4
# Sistema Integral de Gestion de Clientes, Servicios y Reservas

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
            "Carlos Perez",
            "123456789",
            "carlos@gmail.com"
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


if __name__ == "__main__":
    main()
