from Motel.Mundo.conexion import Conexion
from Motel.Mundo.errores import UsuarioExistenteError, UsuarioNoExistenteError, ContraseniaIncorrecta, \
    Usuario_o_ContraseniaIncorrecto, HabitacionExistenteError, CategoriaExistenteError


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


        consultaInsert = f"insert into Usuarios values('{cedula}', '{nombre}','{apellido}', '{contrasenia}')"
        consultaSelect= f"select Cedula from Usuarios where Cedula = '{cedula}'"

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
        consulta = f"select Cedula from Usuarios where Cedula = '{cedula_usuario}'"
        return self.c.select_in_database(consulta)

    def BuscarContrasenia(self, cedula_usuario):
        """
        Se encarga de buscar la contraseña del usuario
        :param cedula_usuario: Identificador del usuario
        :return: La contraseña del usuario en una lista si el usuario existe, si no, la lista estara vacia
        """
        consulta = f"select Contraseña from Usuarios where Cedula = '{cedula_usuario}'"
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
        consulta = f"create table Habitaciones{cedula}(Numero INT PRIMARY KEY, Tipo VARCHAR(15) NOT NULL, Capacidad INT NOT NULL, TipoEntrada VARCHAR(15) NOT NULL, Estado VARCHAR(15) NOT NULL)"
        CursorCrear.execute(consulta)

        CursorCrear.commit()
        CursorCrear.close()

    def Agregarhabitacion(self, numero, cedula, categoria, estado):
        consultaInsert = f"Insert into Habitaciones values('{numero}','{cedula}','{categoria}', '{estado}')"
        consultaSelect = f"select Numero, Cedula_Usuario from Habitaciones where Numero = '{numero}' and Cedula_Usuario = '{cedula}'"

        if self.c.select_in_database(consultaSelect) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise HabitacionExistenteError(numero, f"ya existe una habitacion con el numero: {numero}")

    def AgregarCategoria(self, cedula, nombre, capacidad, tipoEntrada, precioBase, precioAdicional, personaAdicional, jacuzzi, sauna, turco, silla, otros):
        consultaInsert = f"Insert into Categorias values('{nombre}', '{cedula}', '{capacidad}', '{tipoEntrada}'," \
                         f" '{precioBase}', '{precioAdicional}', '{personaAdicional}', '{jacuzzi}', '{sauna}', '{turco}', '{silla}', '{otros}')"
        consultaSelect = f"select Nombre, Cedula_usuario from Categorias where Nombre = '{nombre}' and Cedula_usuario = '{cedula}' "

        if self.c.select_in_database(consultaSelect) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise CategoriaExistenteError(nombre, f"Ya existe una categoria con el nombre: {nombre}")

    def SeleccionarCategoria(self, cedula):
        consulta = f"Select Nombre from Categorias where Cedula_usuario = '{cedula}' "
        return self.c.select_in_database(consulta)

    def selectTipo(self, cedula, numeroHabitacion):
        consulta= f"select Tipo from Habitaciones{cedula} where Numero = {numeroHabitacion}"
        Tipo = self.c.select_in_database(consulta)
        return Tipo[0][0]

    def selectCapacidad(self, cedula, numeroHabitacion):
        consulta = f"select Capacidad from Habitaciones{cedula} where Numero = {numeroHabitacion}"
        self.c.select_in_database(consulta)

    def selectTipoEntrada(self, cedula, numeroHabitacion):
        consulta = f"select TipoEntrada from Habitaciones{cedula} where Numero = {numeroHabitacion}"
        self.c.select_in_database(consulta)

    def selectEstado(self, cedula, numeroHabitacion):
        consulta = f"select Estado from Habitaciones{cedula} where Numero = {numeroHabitacion}"
        self.c.select_in_database(consulta)

    def ActualizarNumeroHabitacion(self, cedula,numeroHabitacion, numeroHabitacionNuevo):
        consulta = f"update Habitaciones{cedula} set Numero = {numeroHabitacionNuevo} where Numero = {numeroHabitacion}"
        self.c.update_in_database(consulta)

    def ActualizarTipoHabitacion(self, cedula, numeroHabitacion, tipoHabitacionNuevo):

        consulta = f"update Habitaciones{cedula} set Tipo = '{tipoHabitacionNuevo}' where Numero = {numeroHabitacion}"
        self.c.update_in_database(consulta)

    def ActualizarCapacidadHabitacion(self, cedula, numeroHabitacion, capacidadHabitacionNuevo):
        consulta = f"update Habitaciones{cedula} set Capacidad = '{capacidadHabitacionNuevo}' where Numero = {numeroHabitacion}"
        self.c.update_in_database(consulta)

    def ActualizarTipoEntradaHabitacion(self, cedula, numeroHabitacion, tipoEntradaHabitacionNuevo):
        consulta = f"update Habitaciones{cedula} set TipoEntrada = '{tipoEntradaHabitacionNuevo}' where Numero = {numeroHabitacion}"
        self.c.update_in_database(consulta)

    def ActualizarEstadoHabitacion(self, cedula, numeroHabitacion, EstadoHabitacionNuevo):
        consulta = f"update Habitaciones{cedula} set Estado = '{EstadoHabitacionNuevo}' where Numero = {numeroHabitacion}"
        self.c.update_in_database(consulta)

    def BuscarhabitacionDisponible(self, cedula):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}';"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionCategoria(self, cedula, categoria):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}' AND H.Categoria = '{categoria}';"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionPrecio(self, cedula, precio):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}' AND C.Precio_base < '{precio}';"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionCapcidad(self, cedula, capacidad):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}' AND C.Capacidad >= '{capacidad}';"
        return self.c.select_in_database(consulta)