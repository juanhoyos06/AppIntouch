import pyodbc
class MotelError(Exception):
    pass

class DatabaseError(pyodbc.ProgrammingError):

    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg

class UsuarioNoExistenteError(MotelError):
    """
    Representa una excepción que indica que el usuario no existe en la base de datos

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg

class UsuarioExistenteError(MotelError):
    """
    Representa una excepción que indica que el usuario ya existe en la base de datos

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):

        self.cedula = cedula
        self.msg = msg

class CategoriaExistenteError(MotelError):
    """
    Representa una excepción que indica que la categoria ya existe en la base de datos

    Attributes:
        nombre: un str que indica el nombre de la categoria
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, nombre: str, msg: str):

        self.nombre = nombre
        self.msg = msg

class HabitacionExistenteError(MotelError):
    def __init__(self, numero: str, msg: str):

        self.numero = numero
        self.msg = msg

class HabitacionNoExistenteError(MotelError):
    def __init__(self, numero: str, msg: str):

        self.numero = numero
        self.msg = msg

class HabitacionNoDisponible(MotelError):
    def __init__(self, numero: str, msg: str):

        self.numero = numero
        self.msg = msg

class HabitacionNoOcupada(MotelError):
    def __init__(self, numero: str, msg: str):

        self.numero = numero
        self.msg = msg

class HabitacionReservada(MotelError):
    def __init__(self, numero: str, msg: str):

        self.numero = numero
        self.msg = msg

class ReservaExistente(MotelError):
    def __init__(self, numero: str, msg: str):

        self.numero = numero
        self.msg = msg

class Usuario_o_ContraseniaIncorrecto(MotelError):
    """
    Representa una excepción que indica que el usuario ya existe en la base de datos

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """

    def __init__(self, cedula: str, msg: str):
        self.cedula = cedula
        self.msg = msg

class ContraseniaIncorrecta(MotelError):

    def __init__(self, contrasenia: str, msg: str):
        self.contrasenia = contrasenia
        self.msg = msg
