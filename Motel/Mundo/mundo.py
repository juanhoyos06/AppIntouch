from Motel.Mundo.conexion import Conexion
from Motel.Mundo.errores import UsuarioExistenteError, UsuarioNoExistenteError, ContraseniaIncorrecta, \
    Usuario_o_ContraseniaIncorrecto, HabitacionExistenteError, CategoriaExistenteError, HabitacionNoDisponible, \
    HabitacionNoOcupada, HabitacionReservada, ReservaExistente


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

    def __init__(self, Numero_habitacion, Fecha_reserva):
        self.Numero_habitacion: str = Numero_habitacion
        self.Fecha_reserva = Fecha_reserva

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


    def Agregarhabitacion(self, numero, cedula, categoria, estado, jacuzzi, sauna, turco, otros):
        consultaInsert = f"Insert into Habitaciones values('{numero}','{cedula}','{categoria}', '{estado}', '{jacuzzi}','{sauna}','{turco}', '{otros}')"
        consultaSelect = f"select Numero, Cedula_Usuario from Habitaciones where Numero = '{numero}' and Cedula_Usuario = '{cedula}'"

        if self.c.select_in_database(consultaSelect) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise HabitacionExistenteError(numero, f"ya existe una habitacion con el numero: {numero}")

    def AgregarCategoria(self, cedula, nombre, capacidad, tipoEntrada, precioBase, precioAdicional, personaAdicional):
        consultaInsert = f"Insert into Categorias values('{nombre}', '{cedula}', '{capacidad}', '{tipoEntrada}'," \
                         f" '{precioBase}', '{precioAdicional}', '{personaAdicional}')"
        consultaSelect = f"select Nombre, Cedula_usuario from Categorias where Nombre = '{nombre}' and Cedula_usuario = '{cedula}' "

        if self.c.select_in_database(consultaSelect) == []:
            self.c.insert_in_database(consultaInsert)
        else:
            raise CategoriaExistenteError(nombre, f"Ya existe una categoria con el nombre: {nombre}")

    def SeleccionarCategoria(self, cedula):
        consulta = f"Select Nombre from Categorias where Cedula_usuario = '{cedula}' "
        return self.c.select_in_database(consulta)



#>>>>>>>>>>>>>>>>>>>>>>>>Metodos Categorias<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def ActualizarNombreCategoria(self, cedula, nombreCategoria, NuevoNombre):
        consulta = f"update Categorias set Nombre = '{NuevoNombre}' where Nombre = '{nombreCategoria}' and Cedula_usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarCapacidadCategoria(self, cedula, nombreCategoria, capacidad):
        consulta = f"update Categorias set Capacidad = {capacidad} where Nombre = '{nombreCategoria}' and Cedula_usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarTipoEntradaCategoria(self, cedula, nombreCategoria, tipoEntradaHabitacionNuevo):
        consulta = f"update Categorias set Tipo_Entrada = '{tipoEntradaHabitacionNuevo}' where Nombre = '{nombreCategoria}' and Cedula_usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarPrecioBase(self, cedula, nombreCategoria, PrecioBaseNuevo):
        consulta = f"update Categorias set Precio_base = '{PrecioBaseNuevo}' where Nombre = '{nombreCategoria}' and Cedula_usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarPrecioHoraAdicional(self, cedula, nombreCategoria, PrecioAdicionalNuevo):
        consulta = f"update Categorias set Precio_hora_adicional = '{PrecioAdicionalNuevo}' where Nombre = '{nombreCategoria}' and Cedula_usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarPrecioPersonaAdicional(self, cedula, nombreCategoria, PrecioPersonaAdicionalNuevo):
        consulta = f"update Categorias set Precio_hora_adicional = '{PrecioPersonaAdicionalNuevo}' where Nombre = '{nombreCategoria}' and Cedula_usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def BuscarCategorias(self, cedula):
        consulta = f"SELECT Nombre, Capacidad, Tipo_Entrada, Precio_base, Precio_hora_adicional," \
                   f"Precio_persona_adicional FROM Categorias WHERE Cedula_usuario = '{cedula}'"
        return self.c.select_in_database(consulta)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FIN CATEGORIAS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>Metodos Habitaciones<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def ActualizarNumeroHabitacion(self, cedula,numeroHabitacion, numeroHabitacionNuevo):
        consulta = f"update Habitaciones set Numero = {numeroHabitacionNuevo} where " \
                   f"Numero = {numeroHabitacion} and Cedula_Usuario = '{cedula}' "
        self.c.update_in_database(consulta)

    def ActualizarEstadoHabitacion(self, cedula, numeroHabitacion, estado):
        consulta = f"update Habitaciones set Estado = '{estado}' where Cedula_Usuario = '{cedula}' and Numero = {numeroHabitacion}"
        self.c.update_in_database(consulta)

    def ActualizarCategoriaHabitacion(self, cedula, numero, categoria):
        consulta = f"update Habitaciones set Categoria = '{categoria}' where Cedula_Usuario = '{cedula}' and Numero = {numero}"
        self.c.update_in_database(consulta)

    def ActualizarJacuzziHabitacion(self, cedula, numero, jacuzzi):
        consulta = f"UPDATE Habitaciones SET Jacuzzi = '{jacuzzi}' WHERE Numero = '{numero}' AND Cedula_Usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarSaunaHabitacion(self, cedula, numero, sauna):
        consulta = f"UPDATE Habitaciones SET Sauna = '{sauna}' WHERE Numero = '{numero}' AND Cedula_Usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarTurcoHabitacion(self, cedula, numero, turco):
        consulta = f"UPDATE Habitaciones SET Turco = '{turco}' WHERE Numero = '{numero}' AND Cedula_Usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def ActualizarOtrosHabitacion(self, cedula, numero, otros):
        consulta = f"UPDATE Habitaciones SET Otros = '{otros}' WHERE Numero = '{numero}' AND Cedula_Usuario = '{cedula}'"
        self.c.update_in_database(consulta)

    def entradaHabitacion(self, cedula, numero):
        consultaUpdate = f"update Habitaciones set Estado = 'Ocupada' where Cedula_Usuario = '{cedula}' and Numero = {numero}"
        consultaSelect = f"Select Estado from Habitaciones where Cedula_Usuario = '{cedula}' and Numero = {numero} "
        estado = self.c.select_in_database(consultaSelect)

        if estado[0][0] != "Disponible":
            raise HabitacionNoDisponible(numero, f"La habitacion {numero} no esta disponible, revise nuevamente la lista")
        else:
            self.c.update_in_database(consultaUpdate)

    def salidaHabitacion(self, cedula, numero):
        consultaUpdate = f"update Habitaciones set Estado = 'Disponible' where Cedula_Usuario = '{cedula}' and Numero = {numero}"
        consultaSelect = f"Select Estado from Habitaciones where Cedula_Usuario = '{cedula}' and Numero = {numero} "
        estado = self.c.select_in_database(consultaSelect)

        if estado[0][0] != "Ocupada":
            raise HabitacionNoOcupada(numero, f"La habitacion {numero} no esta ocupada, revise nuevamente la lista")
        else:
            self.c.update_in_database(consultaUpdate)

    def BuscarhabitacionDisponible(self, cedula):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}';"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionOcupada(self, cedula):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Ocupada' AND H.Cedula_Usuario = '{cedula}';"
        return self.c.select_in_database(consulta)

    def BuscarHabitacionesParaReserva(self, cedula):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Cedula_Usuario = '{cedula}';"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionCategoria(self, cedula, categoria):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}' AND H.Categoria = '{categoria}';"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionPrecio(self, cedula, precio):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}' AND C.Precio_base <= '{precio}' ORDER BY C.Precio_base;"
        return self.c.select_in_database(consulta)

    def BuscarhabitacionCapcidad(self, cedula, capacidad):
        consulta = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas," \
                   f" C.Precio_base FROM Habitaciones as H INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario" \
                   f" AND H.Categoria = C.Nombre where H.Estado = 'Disponible' AND H.Cedula_Usuario = '{cedula}' AND C.Capacidad >= '{capacidad}'ORDER BY C.Precio_base;"
        return self.c.select_in_database(consulta)

    def BuscarHabitaciones(self, cedula):
        consulta = f"select Numero, Categoria, Estado, Jacuzzi, Sauna, Turco, Otros from Habitaciones Where Cedula_Usuario = '{cedula}'"
        return self.c.select_in_database(consulta)

    def SeleccionarNumHabitacion(self, cedula):
        consulta = f"Select Numero from Habitaciones where Cedula_Usuario = '{cedula}' "
        return self.c.select_in_database(consulta)

    def Reservar(self, numero_reserva, cedula, numero_habitacion, fecha_reserva):
        consultaSelect = f"Select * from Reservas Where Numero ='{numero_reserva}'"
        numeroReserva = self.c.select_in_database(consultaSelect)
        if numeroReserva == []:
            consultaInsert = f"INSERT INTO Reservas VALUES('{numero_reserva}', '{numero_habitacion}','{cedula}', '{fecha_reserva}')"
            consultaUpdate = f"UPDATE Habitaciones SET Estado = 'Reservada' WHERE Cedula_Usuario = '{cedula}' AND Numero = '{numero_habitacion}'"
        else:
            raise ReservaExistente(numero_reserva, f"Ya existe una reserva con el numero {numero_reserva}")


        self.c.insert_in_database(consultaInsert)
        self.c.update_in_database(consultaUpdate)

    def SeleccionarNumReserva(self, cedula):
        consulta = f"select Numero from Reservas where Cedula_Usuario = '{cedula}'"
        return self.c.select_in_database(consulta )

    def MostrarReservas(self, cedula):
        consultaSelect = f"Select R.Numero as Numero_reserva, R.Numero_habitacion, R.Fecha_reserva from Reservas as R " \
                         f"inner join Habitaciones as H on H.Numero = R.Numero_habitacion where H.Estado = 'Reservada'  and H.Cedula_Usuario = '{cedula}'"


        return self.c.select_in_database(consultaSelect)

    def BuscarReservas(self, cedula, numero_reserva):
        consulta = f"Select * from Reservas where Numero = '{numero_reserva}' and Cedula_Usuario = '{cedula}'"

        return self.c.select_in_database(consulta)

    def RegistrarEntradaReserva(self, cedula, numeroReserva):
        consultaSelectNumHabitacion = f"Select Numero_habitacion from Reservas where Numero = '{numeroReserva}' and Cedula_Usuario = '{cedula}'"
        numeroHabitacion = self.c.select_in_database(consultaSelectNumHabitacion)

        consultaUpdate = f"update Habitaciones set Estado = 'Ocupada' where Cedula_Usuario = '{cedula}' and Numero = '{numeroHabitacion[0][0]}'"

        self.c.update_in_database(consultaUpdate)
