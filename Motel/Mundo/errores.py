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
