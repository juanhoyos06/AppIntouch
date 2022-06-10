import sys
from datetime import date
from datetime import datetime
from Motel.Mundo import conexion
from Motel.Mundo.mundo import *
from Motel.Vista.gui.ui_DialogoCrearHabitaciones import Ui_DialogoCrearHabitaciones
from Motel.Vista.gui.ui_DialogoModificarHabitaciones import Ui_DialogoModificarHabitaciones
from Motel.Vista.gui.ui_VentanaDeInicio import Ui_VentanaDeInicio
from Motel.Vista.gui.ui_DialogoCrearUsuario import Ui_DialogoCrearUsuario

from Motel.Mundo.errores import UsuarioExistenteError, UsuarioNoExistenteError, HabitacionNoExistenteError
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QIntValidator, QStandardItemModel, QStandardItem, QIcon
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QInputDialog
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation

from Motel.Vista.gui.ui_VentanaModificar import Ui_VentanaModificar
from Motel.Vista.gui.ui_VentanaPrincipal import Ui_VentanaPrincipal
from Motel.Vista.gui.ui_VentanaConfiguracion import Ui_VentanaConfiguracion


class VentanaLogin(QMainWindow):
    def __init__(self, motel: Motel):
        QMainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.motel = motel
        self.ui = Ui_VentanaDeInicio()
        self.ui.setupUi(self)
        self.c = Conexion()
        self._configurar()
        self.show()

    def _configurar(self):
        self.ui.pbutton_ingresar.clicked.connect(self.iniciar_sesion)

    def nombre_usuario(self, cedula):
        consulta = (f"select Nombres from Usuarios where Cedula = {cedula}")
        nombre = self.c.select_in_database(consulta)
        return nombre[0][0]

    def iniciar_sesion(self):

        capturaUsuario = self.ui.lineedit_usuario.text()

        capturaContrasenia = self.ui.lineedit_contrasenia.text()
        if capturaUsuario != "" and capturaContrasenia != "":
            try:
                self.motel.IniciarSesion(capturaUsuario, capturaContrasenia)
            except Usuario_o_ContraseniaIncorrecto as e:

                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error iniciando sesion")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(e.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            else:
                nombreUsuario = self.nombre_usuario(capturaUsuario)
                self.hide()
                self.ventana = VentanaPrincipal(nombreUsuario, capturaUsuario, self.motel)
                self.ventana.show()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class VentanaPrincipal(QMainWindow):
    def __init__(self, nombreUsuario, cedula, motel : Motel):
        super().__init__()
        self.ventana = Ui_VentanaPrincipal()
        self.ventana.setupUi(self)
        self.motel = motel
        self.nombreUsuario = nombreUsuario
        self.cedula = cedula
        self.Categorias = self.motel.SeleccionarCategoria(self.cedula)
        self.ListCategorias = ['Seleccionar']
        self.listaHabitaciones = ['Seleccionar']
        self.listaReservas = ['Seleccionar']

        self.reservas = self.motel.SeleccionarNumReserva(self.cedula)
        self.habitaciones = self.motel.SeleccionarNumHabitacion(self.cedula)




        self.ventana.pbutton_configuracion.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_configuracion))
        self.ventana.pbutton_entradas.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_entradas))
        self.ventana.pbutton_reservas.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_reservas))
        self.ventana.label_bienvenida.setText(f"        Bienvenido a InTouch\n                              {self.nombreUsuario}")

        if self.cedula == '1000410302' or self.cedula == '1125618030' or self.cedula == '1000414766':
           self.ventana.pbutton_crearUsuario.setEnabled(True)

        self.ventana.pbutton_crearUsuario.clicked.connect(self.abrir_dialogo_crearUsuario)
        self.ventana.pbutton_configurarHabitaciones.clicked.connect(self.abrir_ventana_configuracion)
        self.ventana.pbutton_modificarHabitaciones.clicked.connect(self.abrir_ventana_modificar)
        self.ventana.pbutton_entradas.clicked.connect(self.habitaciones_para_entrada)
        self.ventana.pbutton_entradas.clicked.connect(self.habitaciones_para_salida)
        self.ventana.pbutton_filtrar.clicked.connect(self.filtrar)
        self.ventana.comboBox_categoriasBuscar.addItems(self.Lista_categorias())
        self.ventana.comboBox_numeroHabitacion_reserva.addItems(self.lista_habitaciones())
        self.ventana.comboBox_numeroReserva.addItems(self. lista_numReservas())

        self.ventana.pbutton_registrar.clicked.connect(self.registrar_entrada)
        self.ventana.pbutton_registrar_salida.clicked.connect(self.registrar_salida)
        self.ventana.pbutton_reservas.clicked.connect(self.habitaciones_para_reservar)
        self.ventana.pbutton_reservas.clicked.connect(self.habitaciones_reservadas)
        self.ventana.pbutton_reservar.clicked.connect(self.reservar)
        self.ventana.pbutton_BuscarReserva.clicked.connect(self.buscar_reserva)
        self.ventana.pbutton_registrar_entrada_reserva.clicked.connect(self.registrar_entrada_reserva)

    def lista_habitaciones(self):
        for i in range(len(self.habitaciones)):
            self.listaHabitaciones.append(self.habitaciones[i][0])

        return self.listaHabitaciones

    def Lista_categorias(self):
        for i in range(len(self.Categorias)):
            self.ListCategorias.append(self.Categorias[i][0])

        return self.ListCategorias

    def lista_numReservas(self):
        for i in range(len(self.reservas)):
            self.listaReservas.append(self.reservas[i][0])
        return self.listaReservas

    def abrir_ventana_configuracion(self):
        self.ventanaC = VentanaConfiguracion(self.cedula, self.motel)
        self.ventanaC.show()

    def abrir_ventana_modificar(self):
        self.ventanaM = VentanaModificar(self.cedula, self.motel)
        self.ventanaM.show()
        self.ventanaM.mostrar_categorias()
        self.ventanaM.mostrar_habitaciones()

    def abrir_dialogo_crearUsuario(self):
        dialog = DialogoCrearUsuario(self)
        resp = dialog.exec()

        if resp == QDialog.Accepted:
            capturaCedula = dialog.ui.lineedit_cedula.text()
            capturaNombres = dialog.ui.lineedit_nombres.text()
            capturaApellidos = dialog.ui.lineedit_apellidos.text()
            capturaContrasenia = dialog.ui.lineedit_contrasenia.text()

            try:
                self.motel.CrearUsuario(capturaCedula, capturaNombres,capturaApellidos, capturaContrasenia)
            except UsuarioExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error creando usuario.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Usuario creado correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def actualizar_tabla_habitaciones_disponibles(self, habitacionesDisponibles):
        i = len(habitacionesDisponibles)

        self.ventana.tableHabitacionesDisp.setRowCount(i)
        tablerow = 0

        for row in habitacionesDisponibles:
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def actualizar_tabla_habitaciones_para_reservar(self, habitaciones):
        i = len(habitaciones)

        self.ventana.tableHabitacionesDisp_reservar.setRowCount(i)
        tablerow = 0

        for row in habitaciones:
            self.ventana.tableHabitacionesDisp_reservar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventana.tableHabitacionesDisp_reservar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ventana.tableHabitacionesDisp_reservar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ventana.tableHabitacionesDisp_reservar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def actualizar_tabla_habitaciones_ocupadas(self, habitacionesOcupadas):
        i = len(habitacionesOcupadas)

        self.ventana.tableHabitacionesOcupadas.setRowCount(i)
        tablerow = 0

        for row in habitacionesOcupadas:
            self.ventana.tableHabitacionesOcupadas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventana.tableHabitacionesOcupadas.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ventana.tableHabitacionesOcupadas.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ventana.tableHabitacionesOcupadas.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def actualizar_tabla_reservas(self, habitaciones_reservadas):
        i = len(habitaciones_reservadas)

        self.ventana.tableHabitaciones_reservadas.setRowCount(i)
        tablerow = 0

        for row in habitaciones_reservadas:
            self.ventana.tableHabitaciones_reservadas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventana.tableHabitaciones_reservadas.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ventana.tableHabitaciones_reservadas.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            tablerow += 1

    def habitaciones_para_entrada(self):
        habitacionesDisponibles = self.motel.BuscarhabitacionDisponible(self.cedula)
        self.actualizar_tabla_habitaciones_disponibles(habitacionesDisponibles)

    def habitaciones_para_reservar(self):
        habitaciones = self.motel.BuscarHabitacionesParaReserva(self.cedula)
        self.actualizar_tabla_habitaciones_para_reservar(habitaciones)

    def habitaciones_para_salida(self):
        habitacionesOcupada = self.motel.BuscarhabitacionOcupada(self.cedula)
        self.actualizar_tabla_habitaciones_ocupadas(habitacionesOcupada)

    def habitaciones_reservadas(self):
        habitacionesReservadas = self.motel.MostrarReservas(self.cedula)
        self.actualizar_tabla_reservas(habitacionesReservadas)

    def filtrar(self):
        capturaCategoria = self.ventana.comboBox_categoriasBuscar.currentText()
        capturaCapacidad = self.ventana.lineedit_capacidadBus.text()
        capturaPrecio = self.ventana.lineedit_precioBus.text()

        if capturaCapacidad == "" and capturaPrecio == "" and capturaCategoria != "Seleccionar":
            habitacionesDisponibles = self.motel.BuscarhabitacionCategoria(self.cedula, capturaCategoria)
            self.actualizar_tabla_habitaciones_disponibles(habitacionesDisponibles)

        elif capturaCapacidad != "" and capturaPrecio == "":
            habitacionesDisponibles = self.motel.BuscarhabitacionCapcidad(self.cedula, capturaCapacidad)
            self.actualizar_tabla_habitaciones(habitacionesDisponibles)
            self.ventana.lineedit_capacidadBus.clear()

        elif capturaCapacidad == "" and capturaPrecio != "":
            habitacionesDisponibles = self.motel.BuscarhabitacionPrecio(self.cedula, capturaPrecio)
            self.actualizar_tabla_habitaciones(habitacionesDisponibles)
            self.ventana.lineedit_precioBus.clear()

    def registrar_entrada(self):
        capturaNum = self.ventana.lineedit_numHab.text()

        if capturaNum != "":
            try:
                self.motel.entradaHabitacion(self.cedula, capturaNum)
            except HabitacionNoDisponible as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error registrando entrada")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Entrada registrada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.habitaciones_para_entrada()
                self.ventana.lineedit_numHab.clear()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de registro")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe de ingresar el numero de la habitacion que va a ser ocupada")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def registrar_salida(self):
        capturaNum = self.ventana.lineedit_numHab_salida.text()
        if capturaNum != "":
            try:
                self.motel.salidaHabitacion(self.cedula, capturaNum)
            except HabitacionNoOcupada as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error registrando salida")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("salida registrada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.habitaciones_para_salida()
                self.ventana.lineedit_numHab_salida.clear()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de registro")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe de ingresar el numero de la habitacion que va a ser desocupada")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def reservar(self):
        capturaNumRes = self.ventana.lineedit_NumeroReserva.text()
        capturaNumHab= self.ventana.comboBox_numeroHabitacion_reserva.currentText()
        capturaFecha = self.ventana.lineedit_fechaReserva.text()

        if capturaNumRes  != "" and capturaNumHab != 'Seleccionar' and capturaFecha != "":
            try:
                self.motel.Reservar(capturaNumRes, self.cedula, capturaNumHab, capturaFecha)
            except HabitacionReservada as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            except ReservaExistente as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error realizando reserva")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Reserva realizada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.ventana.lineedit_NumeroReserva.clear()
                self.ventana.comboBox_numeroHabitacion_reserva.setCurrentIndex(0)
                self.ventana.lineedit_fechaReserva.clear()
                self.habitaciones_reservadas()

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de reserva")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe de ingresar todos los campos")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def buscar_reserva(self):
        capturaNumReserva = self.ventana.comboBox_numeroReserva.currentText()

        if capturaNumReserva != 'Seleccionar':
            Habitaciones_reservadas = self.motel.BuscarReservas(self.cedula, capturaNumReserva)
            self.actualizar_tabla_reservas(Habitaciones_reservadas)
            self.ventana.comboBox_numeroReserva.setCurrentIndex(0)

    def registrar_entrada_reserva(self):
        capturaNumReserva = self.ventana.lineedit_numReserva_entradaReserva.text()

        if capturaNumReserva != "":
            self.motel.RegistrarEntradaReserva(self.cedula,capturaNumReserva)
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Operacion Exitosa")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Entrada registrada correctamente.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

            self.habitaciones_reservadas()
            self.ventana.lineedit_numReserva_entradaReserva.clear()



        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de registro")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe de ingresar el numero de la reserva")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()






class VentanaConfiguracion(QMainWindow):
    def __init__(self, cedula, motel : Motel):
        super().__init__()
        self.ventanaC = Ui_VentanaConfiguracion()
        self.ventanaC.setupUi(self)
        self.motel = motel
        self.cedula = cedula
        self.servicios = ['No', 'Si']
        self.estados = ['Disponible', 'Ocupada', 'Reservada']
        self.categorias = self.motel.SeleccionarCategoria(self.cedula)
        self.listCategorias = ['Seleccionar']

        self.ventanaC.pushButton_aceptar.clicked.connect(self.definir_categorias)
        self.ventanaC.pushButton_aceptarHab.clicked.connect(self.agregar_habitacion)
        self.ventanaC.pushButton_limpiar_categoria.clicked.connect(self.limpiar_categoria)
        self.ventanaC.pushButton_limpiarHab.clicked.connect(self.limpiar_habitaciones)
        self.ventanaC.comboBox_jacuzzi.addItems(self.servicios)
        self.ventanaC.comboBox_sauna.addItems(self.servicios)
        self.ventanaC.comboBox_turco.addItems(self.servicios)
        self.ventanaC.pushButton_volver_AH.clicked.connect(self.volver)
        self.ventanaC.pushButton_volver_DC.clicked.connect(self.volver)

        self.ventanaC.comboBox_categorias.addItems(self.lista_categorias())
        self.ventanaC.comboBox_estado.addItems(self.estados)

    def volver(self):
        self.close()

    def lista_categorias(self):
        for i in range(len(self.categorias)):
            self.listCategorias.append(self.categorias[i][0])

        return self.listCategorias

    def agregar_habitacion(self):
        capturaNumero = self.ventanaC.lineedit_numHabitacion.text()
        capturaCategoria = self.ventanaC.comboBox_categorias.currentText()
        capturaEstado = self.ventanaC.comboBox_estado.currentText()
        capturaJacuzzi = self.ventanaC.comboBox_jacuzzi.currentText()
        capturaSauna = self.ventanaC.comboBox_sauna.currentText()
        capturaTurco = self.ventanaC.comboBox_turco.currentText()
        capturaOtros = self.ventanaC.lineedit_otros.text()

        if capturaNumero != "" and capturaCategoria != "Seleccionar":
            try:
                self.motel.Agregarhabitacion(capturaNumero, self.cedula, capturaCategoria, capturaEstado, capturaJacuzzi, capturaSauna, capturaTurco, capturaOtros)
            except HabitacionExistenteError as e:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error Agregando Habitacion.")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(e.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Habitacion agregada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.ventanaC.lineedit_numHabitacion.clear()

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Todos los campos obligatorios debe ingresarlos.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def definir_categorias(self):

        capturaNombreCategoria = self.ventanaC.lineedit_nombreCategoria.text()
        capturaCapacidad = self.ventanaC.lineedit_capacidad.text()
        capturaTipoEntrada = self.ventanaC.lineedit_tipoEntrada.text()
        capturaPrecioBase = self.ventanaC.lineedit_precioBase.text()
        capturaPrecioAdicional = self.ventanaC.lineedit_precioAdicional.text()
        capturaPersonaAdicional = self.ventanaC.lineedit_personaAdicional.text()



        if (capturaNombreCategoria != "" and capturaCapacidad != "" and capturaTipoEntrada != "" and capturaPrecioBase != ""
                and capturaPrecioAdicional != "" and capturaPersonaAdicional != ""):
            try:
                self.motel.AgregarCategoria(self.cedula,capturaNombreCategoria,capturaCapacidad,capturaTipoEntrada,
                                            capturaPrecioBase, capturaPrecioAdicional, capturaPersonaAdicional)
            except CategoriaExistenteError as e:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error Agregando Categoria.")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(e.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Categoria agregada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.ventanaC.lineedit_nombreCategoria.clear()
                self.ventanaC.lineedit_capacidad.clear()
                self.ventanaC.lineedit_tipoEntrada.clear()
                self.ventanaC.lineedit_precioBase.clear()
                self.ventanaC.lineedit_precioAdicional.clear()
                self.ventanaC.lineedit_personaAdicional.clear()
                self.ventanaC.lineedit_precioAdicional.clear()
                self.ventanaC.lineedit_otros.clear()

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Todos los campos obligatorios debe ingresarlos.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def limpiar_categoria(self):
        self.ventanaC.lineedit_nombreCategoria.clear()
        self.ventanaC.lineedit_capacidad.clear()
        self.ventanaC.lineedit_tipoEntrada.clear()
        self.ventanaC.lineedit_precioBase.clear()
        self.ventanaC.lineedit_precioAdicional.clear()
        self.ventanaC.lineedit_personaAdicional.clear()

    def limpiar_habitaciones(self):
        self.ventanaC.lineedit_numHabitacion.clear()
        self.ventanaC.lineedit_otros.clear()
        self.ventanaC.comboBox_categorias.setCurrentIndex(0)
        self.ventanaC.comboBox_estado.setCurrentIndex(0)
        self.ventanaC.comboBox_jacuzzi.setCurrentIndex(0)
        self.ventanaC.comboBox_sauna.setCurrentIndex(0)
        self.ventanaC.comboBox_turco.setCurrentIndex(0)

class DialogoCrearUsuario(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogoCrearUsuario()
        self.ui.setupUi(self)

    def accept(self) -> None:
        capturaCedula = self.ui.lineedit_cedula.text()
        capturaNombres = self.ui.lineedit_nombres.text()
        capturaApellidos = self.ui.lineedit_apellidos.text()
        capturaContrasenia = self.ui.lineedit_contrasenia.text()

        if capturaCedula != "" and capturaNombres != "" and capturaApellidos != "" and capturaContrasenia != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Todos los campos son obligatorios, debe ingresarlos.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

class VentanaModificar(QMainWindow):
    def __init__(self, cedula, motel: Motel):
        super().__init__()
        self.ventanaM = Ui_VentanaModificar()
        self.ventanaM.setupUi(self)
        self.motel = motel
        self.cedula = cedula
        self.servicios = ['Seleccionar', 'No', 'Si']
        self.estados = ['Seleccionar', 'Disponible', 'Ocupada', 'Reservada']
        self.categorias = self.motel.SeleccionarCategoria(self.cedula)
        self.listCategorias = ['Seleccionar']
        self.listHabitaciones = ['Seleccionar']
        self.habitaciones = self.motel.SeleccionarNumHabitacion(self.cedula)

        self.ventanaM.pbutton_modificar.clicked.connect(self.ModificarCategorias)
        self.ventanaM.pbutton_refrescar.clicked.connect(self.mostrar_categorias)
        self.ventanaM.pbutton_limpiar.clicked.connect(self.LimpiarModificarCategorias)
        self.ventanaM.pbutton_limpiar_mh.clicked.connect(self.limpiarModificarHabitaciones)
        self.ventanaM.pbutton_volver.clicked.connect(self.volver)
        self.ventanaM.comboBox_categorias.addItems(self.lista_categorias())
        self.ventanaM.comboBox_categoriasMH.addItems(self.listCategorias)
        self.ventanaM.comboBox_jacuzzi.addItems(self.servicios)
        self.ventanaM.comboBox_sauna.addItems(self.servicios)
        self.ventanaM.comboBox_turco.addItems(self.servicios)
        self.ventanaM.comboBox_numeroHabitacion.addItems(self.lista_habitaciones())
        self.ventanaM.pbutton_refrescar_2.clicked.connect(self.mostrar_habitaciones)
        self.ventanaM.pbutton_modificar_mh.clicked.connect(self.ModificarHabitaciones)
        self.ventanaM.pbutton_volver_mh.clicked.connect(self.volver)



    def lista_categorias(self):
        for i in range(len(self.categorias)):
            self.listCategorias.append(self.categorias[i][0])

        return self.listCategorias

    def mostrar_categorias(self):
        categorias = self.motel.BuscarCategorias(self.cedula)

        i = len(categorias)

        self.ventanaM.tableCategorias.setRowCount(i)
        tablerow = 0

        for row in categorias:
            self.ventanaM.tableCategorias.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventanaM.tableCategorias.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ventanaM.tableCategorias.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ventanaM.tableCategorias.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ventanaM.tableCategorias.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ventanaM.tableCategorias.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            tablerow += 1

    def ModificarCategorias(self):

        capturaNombreCategoria = self.ventanaM.comboBox_categorias.currentText()
        capturaNombre =          self.ventanaM.lineedit_Nomcategoria.text()
        capturaCapacidad =       self.ventanaM.lineedit_capacidadCateg.text()
        capturaTipoEntrada =     self.ventanaM.lineedit_tipoEntrada.text()
        capturaPrecioBase =      self.ventanaM.lineedit_precioBase.text()
        capturaPrecioAdicional = self.ventanaM.lineedit_precioAdicional.text()
        capturaPersonaAdicional =self.ventanaM.lineedit_personaAdicional.text()

        if capturaNombreCategoria != "Seleccionar":
            if capturaNombre != "":
                self.motel.ActualizarNombreCategoria(self.cedula,capturaNombreCategoria, capturaNombre)
                self.ventanaM.lineedit_Nomcategoria.clear()

            if capturaCapacidad != "":
                self.motel.ActualizarCapacidadCategoria(self.cedula, capturaNombreCategoria, capturaCapacidad)
                self.ventanaM.lineedit_capacidadCateg.clear()

            if capturaTipoEntrada != "":
                self.motel.ActualizarTipoEntradaCategoria(self.cedula, capturaNombreCategoria, capturaTipoEntrada)
                self.ventanaM.lineedit_tipoEntrada.clear()

            if capturaPrecioBase != "":
                self.motel.ActualizarPrecioBase(self.cedula,capturaNombreCategoria, capturaPrecioBase)
                self.ventanaM.lineedit_precioBase.clear()

            if capturaPrecioAdicional != "":
                self.motel.ActualizarPrecioHoraAdicional(self.cedula, capturaNombreCategoria, capturaPrecioAdicional)
                self.ventanaM.lineedit_precioAdicional.clear()

            if capturaPersonaAdicional != "":
                self.motel.ActualizarPrecioPersonaAdicional(self.cedula, capturaNombreCategoria, capturaPersonaAdicional)
                self.ventanaM.lineedit_personaAdicional.clear()

            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Operacion Exitosa")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Categoria modificada correctamente")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            self.mostrar_categorias()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe seleccionar el nombre de la categoria a modificar")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

    def LimpiarModificarCategorias(self):

        self.ventanaM.lineedit_Nomcategoria.clear()
        self.ventanaM.lineedit_capacidadCateg.clear()
        self.ventanaM.lineedit_tipoEntrada.clear()
        self.ventanaM.lineedit_precioBase.clear()
        self.ventanaM.lineedit_precioAdicional.clear()
        self.ventanaM.lineedit_personaAdicional.clear()
        self.ventanaM.comboBox_categorias.setCurrentIndex(0)

    def limpiarModificarHabitaciones(self):
        self.ventanaM.comboBox_numeroHabitacion.setCurrentIndex(0)
        self.ventanaM.comboBox_categoriasMH.setCurrentIndex(0)
        self.ventanaM.comboBox_jacuzzi.setCurrentIndex(0)
        self.ventanaM.comboBox_sauna.setCurrentIndex(0)
        self.ventanaM.comboBox_turco.setCurrentIndex(0)
        self.ventanaM.lineedit_otros.clear()

    def volver(self):
        self.close()

    def mostrar_habitaciones(self):
        habitaciones = self.motel.BuscarHabitaciones(self.cedula)

        i = len(habitaciones)

        self.ventanaM.tableHabitaciones.setRowCount(i)
        tablerow = 0

        for row in habitaciones:
            self.ventanaM.tableHabitaciones.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventanaM.tableHabitaciones.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ventanaM.tableHabitaciones.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ventanaM.tableHabitaciones.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ventanaM.tableHabitaciones.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ventanaM.tableHabitaciones.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ventanaM.tableHabitaciones.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            tablerow += 1

    def lista_habitaciones(self):
        for i in range(len(self.habitaciones)):
            self.listHabitaciones.append(self.habitaciones[i][0])

        return self.listHabitaciones

    def ModificarHabitaciones(self):

        capturaNumeroH  = self.ventanaM.comboBox_numeroHabitacion.currentText()
        capturaCategoria = self.ventanaM.comboBox_categoriasMH.currentText()
        capturaJacuzzi = self.ventanaM.comboBox_jacuzzi.currentText()
        capturaSauna = self.ventanaM.comboBox_sauna.currentText()
        CapturaTurco = self.ventanaM.comboBox_turco.currentText()
        CapturaOtros = self.ventanaM.lineedit_otros.text()

        if capturaNumeroH != 'Seleccionar':
            if capturaCategoria != 'Seleccionar':
                self.motel.ActualizarCategoriaHabitacion(self.cedula, capturaNumeroH, capturaCategoria)

            if capturaJacuzzi != 'Seleccionar':
                self.motel.ActualizarJacuzziHabitacion(self.cedula, capturaNumeroH, capturaJacuzzi)

            if capturaSauna != 'Seleccionar':
                self.motel.ActualizarSaunaHabitacion(self.cedula, capturaNumeroH, capturaSauna)

            if CapturaTurco != 'Seleccionar':
                self.motel.ActualizarTurcoHabitacion(self.cedula, capturaNumeroH, CapturaTurco)

            if CapturaOtros != '':
                self.motel.ActualizarOtrosHabitacion(self.cedula, capturaNumeroH, CapturaOtros)

            if capturaJacuzzi != 'Seleccionar' or capturaSauna != 'Seleccionar' or CapturaTurco != 'Seleccionar' or CapturaOtros != '':
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Habitacion modificada correctamente")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                self.mostrar_habitaciones()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Advertencia")
                msg_box.setStyleSheet('background-color: None')
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("No hay ningun campo a modificar ")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setStyleSheet('background-color: None')
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe seleccionar el numero de la habitacion a modificar")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()