from Motel.Mundo.conexion import Conexion
from Motel.Mundo.errores import UsuarioExistenteError, UsuarioNoExistenteError, ContraseniaIncorrecta, \
    Usuario_o_ContraseniaIncorrecto, HabitacionExistenteError


class Habitacion:

    def __init__(self, Numero, Tipo, Capacidad, TipoEntrada, Estado = "Disponible"):
        self.Numero: int = Numero
        self.Tipo: str = Tipo
        self.Capacidad: int = Capacidad
        self.TipoEntrada: str = TipoEntrada
        self.Estado: str = Estado
    pass

class Usuario:
    c = Conexion()
    def __init__(self, cedula, nombre, apellido, contrasenia):
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.contrasenia: str = contrasenia


    def BuscarhabitacionDisponible(self, habitacion: Habitacion):
        consulta = f"select * from Habitaciones{self.cedula} where Estado = {habitacion.Estado}"
        self.c.select_in_database(consulta)
    def BuscarHabitacionTipo(self, habitacion: Habitacion):
        pass
    def AgregarNuevaHabitacion(self, habitacion: Habitacion):
        consulta = f"insert into Habitaciones{self.cedula}(Numero, Tipo, Capacidad, TipoEntrada, Estado) " \
                   f"values({habitacion.Numero}, {habitacion.Tipo}, {habitacion.Capacidad}," \
                   f" {habitacion.TipoEntrada}, {habitacion.Estado})"

        self.c.insert_in_database(consulta)
    pass

class Reserva:

    def __init__(self, TipoHabitacion, CantidadPersonas, TipoEntrada, FechaReserva, HoraReserva):
        self.TipoHabitacion: str = TipoHabitacion
        self.CantidadPersonas: int = CantidadPersonas
        self.TipoEntrada: str = TipoEntrada
        self.FechaReserva = FechaReserva
        self.HorReserva = HoraReserva
    pass

class Motel:

    def __init__(self):
        self.c = Conexion()

    def CrearUsuario(self, cedula, nombre, apellido, contrasenia):


        consultaInsert = f"insert into Usuarios(Documento_Identidad, Nombre, Apellido, Contraseña)" \
                   f"values('{cedula}', '{nombre}','{apellido}', '{contrasenia}')"
        consultaSelect= f"select Documento_Identidad from Usuarios where Documento_Identidad = '{cedula}'"

        if self.c.select_in_database(consultaSelect) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise UsuarioExistenteError(cedula,f"Ya existe un usuario con la cedula{cedula}")

    def BuscarUsuario(self, cedula_usuario):
        """
        Se encarga de buscar si el usuario si esta registrado en la base de datos
        :param cedula_usuario: Identificador del usuario
        :return: El identificador del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """
        consulta = f"select Documento_Identidad from Usuarios where Documento_Identidad = '{cedula_usuario}'"
        return self.c.select_in_database(consulta)

    def BuscarContrasenia(self, cedula_usuario):
        """
        Se encarga de buscar la contraseña del usuario
        :param cedula_usuario: Identificador del usuario
        :return: La contraseña del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """
        consulta = f"select Contraseña from Usuarios where Documento_Identidad = '{cedula_usuario}'"
        return self.c.select_in_database(consulta)

    def IniciarSesion(self, CedulaUsuario, ContraseniaUsuario):
        """
        verifica que el usuario que quiere ingresar este en la base de datos, siendo asi le da acceso,
        de lo contrario no le permite el ingreso a la aplicacion
        :param CedulaUsuario: Identificador para el ingreso
        :param ContraseniaUsuario: Conntraseña para ese identificador
        :return:
        """
        cedula = self.BuscarUsuario(CedulaUsuario)
        contrasenia= self.BuscarContrasenia(CedulaUsuario)

        if cedula != [] and ContraseniaUsuario == contrasenia[0][0]:
           return (CedulaUsuario, ContraseniaUsuario)

        else:
            raise Usuario_o_ContraseniaIncorrecto(CedulaUsuario, f"Usuario o contraseña incorrecto, porfavor intente nuevamente")

    def CrearDatabaseHabitaciones(self, cedula):
        """
        Crea la tabla de las habitaciones al usuario
        :arg : cedula del usuario que va a crear las habitaciones

        """
        CursorCrear = Conexion.conexion.cursor()
        consulta = f"create table Habitaciones{cedula}(Numero INT PRIMARY KEY, Tipo VARCHAR(25) NOT NULL, Capacidad INT NOT NULL, Estado TEXT NOT NULL)"
        CursorCrear.execute(consulta)

        CursorCrear.commit()
        CursorCrear.close()

    def buscarTabla(self, cedula):
        consulta = f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Habitacioes{cedula}'"
        self.c.select_in_database(consulta)

    def Agregarhabitacion(self, cedula, numero, tipo, capacidad, tipoEntrada, estado):
        consultaInsert = f"Insert into Habitaciones{cedula} values('{numero}','{tipo}', '{capacidad}', '{tipoEntrada}', '{estado}')"
        consultaSelect = f"select Numero from Habitaciones{cedula} where Numero = {numero}"

        if self.c.select_in_database(consultaSelect) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise HabitacionExistenteError(numero, f"ya existe una habitacion con el numero: {numero}")



