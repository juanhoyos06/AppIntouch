import pyodbc

from Motel.Mundo.errores import UsuarioNoExistenteError


class Conexion:
    server = "DESKTOP"
    bd = "Conexion_python"
    usuario = "sa"
    contrasena = "sqlserver2008*"

    conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+server+
                            f";DATABASE={bd}; UID={usuario};PWD={contrasena}")

##Consulta a la base de datos
    def select_in_database(self, consulta):
        habitaciones = list()
        cursorSelect = self.conexion.cursor()
        try:
            cursorSelect.execute(consulta)
        except UsuarioNoExistenteError as e:
            print(e.msg)

        Habitacion = cursorSelect.fetchone()

        while Habitacion:

            habitaciones.append(Habitacion)
            Habitacion = cursorSelect.fetchone()

        cursorSelect.close()
        return habitaciones
##Insertar datos
    def insert_in_database(self,consulta):
        """
        Inserta un nuevo objeto en la base de datos
        :arg Consulta: instrucciones para insertar en la base de datos
        """
        cursorInsert = self.conexion.cursor()

        cursorInsert.execute(consulta)
        cursorInsert.commit()
        cursorInsert.close()

##Actualizar datos
    def update_in_database(self):
        cursorUpdate = self.conexion.cursor()
        consultaUpdate = "update Habitaciones set Tipo_habitacion = 'Especial' where Numero_Habitacion = 005"

        cursorUpdate.execute(consultaUpdate)

        cursorUpdate.commit()
        cursorUpdate.close()

##Elimiar datos
    def delete_in_database(self):
        cursorEliminar = self.conexion.cursor()
        consultaEliminar = f"delete from Habitaciones where Numero_Habitacion = 001"

        cursorEliminar.execute(consultaEliminar)

        cursorEliminar.commit()
        cursorEliminar.close()

    def BuscarContrasenia(self,consulta):

        return self.select_in_database(consulta)

#c = Conexion()
#
#consulta1 = f"select * from Usuarios "
#consulta2 = f"select Contraseña from Usuarios where Documento_Identidad = 1000410302"
#consulta = f"select Contraseña from Usuarios where Documento_Identidad = 1000410302"
#Cedula = c.select_in_database(consulta2)
#print(Cedula)
#contrasenia=c.BuscarContrasenia(consulta)
#print(contrasenia[0][0])
#if Cedula == []:
#    print("hello")
#else:
#    print("hi")
