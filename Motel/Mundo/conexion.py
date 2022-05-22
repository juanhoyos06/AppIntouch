import pyodbc




class Conexion:
    server = "DESKTOP"
    bd = "Conexion_python"
    usuario = "sa"
    contrasena = "sqlserver2008*"

    conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+server+
                            f";DATABASE={bd}; UID={usuario};PWD={contrasena}")

##Consulta a la base de datos
    def select_in_database(self, consulta):
        habitaciones = []
        cursorSelect = self.conexion.cursor()

        cursorSelect.execute(consulta)


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
    def update_in_database(self, consulta):
        cursorUpdate = self.conexion.cursor()


        cursorUpdate.execute(consulta)

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

c = Conexion()
#
consulta1 = f"SELECT H.Numero as Numero_Habitacion, C.Nombre as Categoria, C.Capacidad as Capacidad_Personas, C.Precio_base FROM Habitaciones as H " \
            f"INNER JOIN Categorias as C ON H.Cedula_Usuario = C.Cedula_usuario AND H.Categoria = C.Nombre where H.Estado = 'Disponible' and H.Cedula_Usuario = '1000410302'"
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
#print(str(c.select_in_database(consulta1)))