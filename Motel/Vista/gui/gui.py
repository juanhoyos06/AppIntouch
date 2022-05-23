import sys

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
        self.ListCategorias = []



        self.ventana.pbutton_configuracion.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_configuracion))
        self.ventana.pbutton_entradas.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_entradas))
        self.ventana.pbutton_reservas.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_reservas))
        self.ventana.label_bienvenida.setText(f"        Bienvenido a InTouch\n                              {self.nombreUsuario}")

        if self.cedula == '1000410302' or self.cedula == '1125618030' or self.cedula == '1000414766':
           self.ventana.pbutton_crearUsuario.setEnabled(True)

        self.ventana.pbutton_crearUsuario.clicked.connect(self.abrir_dialogo_crearUsuario)
        self.ventana.pbutton_configurarHabitaciones.clicked.connect(self.abrir_ventana_configuracion)
        self.ventana.pbutton_modificarHabitaciones.clicked.connect(self.abrir_dialogo_modificarHabitaciones)
        self.ventana.pbutton_entradas.clicked.connect(self.registrar_entrada)
        self.ventana.pbutton_filtrar.clicked.connect(self.filtrar)
        self.ventana.comboBox_categoriasBuscar.addItems(self.Lista_categorias())

    def Lista_categorias(self):
        for i in range(len(self.Categorias)):
            self.ListCategorias.append(self.Categorias[i][0])

        return self.ListCategorias

    def abrir_ventana_configuracion(self):
        self.ventanaC = VentanaConfiguracion(self.cedula, self.motel)
        self.ventanaC.show()

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

    def abrir_dialogo_modificarHabitaciones(self):
        dialogo = DialogoModificarHabitaciones(self)
        resp = dialogo.exec()

        if resp == QDialog.Accepted:
            capturaNumero = dialogo.ui.lineedit_numeroHabitacion.text()
            capturaTipo = dialogo.ui.lineedit_tipoHabitacion.text()
            capturaCapacidad = dialogo.ui.lineedit_capacidadHabitacion.text()
            capturaTipoEntrada = dialogo.ui.lineedit_tipoEntrada.text()
            capturaEstado = dialogo.ui.lineedit_estadoHabitacion.text()

            if capturaNumero != "":


                if capturaTipo != "":

                    self.motel.ActualizarTipoHabitacion(self.cedula,capturaNumero, capturaTipo)

                if capturaCapacidad != "":

                    self.motel.ActualizarCapacidadHabitacion(self.cedula, capturaNumero, capturaCapacidad)

                if capturaTipoEntrada != "":

                    self.motel.ActualizarTipoEntradaHabitacion(self.cedula, capturaNumero, capturaTipoEntrada)

                if capturaEstado != "":

                    self.motel.ActualizarEstadoHabitacion(self.cedula,capturaNumero, capturaEstado)
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error de validación")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Debe ingresar el numero de la habitacion que desea modificar")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def actualizar_tabla(self, habitacionesDisponibles):
        i = len(habitacionesDisponibles)

        self.ventana.tableHabitacionesDisp.setRowCount(i)
        tablerow = 0

        for row in habitacionesDisponibles:
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ventana.tableHabitacionesDisp.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1

    def registrar_entrada(self):
        habitacionesDisponibles = self.motel.BuscarhabitacionDisponible(self.cedula)
        self.actualizar_tabla(habitacionesDisponibles)

    def filtrar(self):
        capturaCategoria = self.ventana.comboBox_categoriasBuscar.currentText()
        capturaCapacidad = self.ventana.lineedit_capacidadBus.text()
        capturaPrecio = self.ventana.lineedit_precioBus.text()

        if capturaCapacidad == "" and capturaPrecio == "":
            habitacionesDisponibles = self.motel.BuscarhabitacionCategoria(self.cedula, capturaCategoria)
            self.actualizar_tabla(habitacionesDisponibles)

        elif capturaCapacidad != "" and capturaPrecio == "":
            habitacionesDisponibles = self.motel.BuscarhabitacionCapcidad(self.cedula, capturaCapacidad)
            self.actualizar_tabla(habitacionesDisponibles)
            self.ventana.lineedit_capacidadBus.setText("")

        elif capturaCapacidad == "" and capturaPrecio != "":
            habitacionesDisponibles = self.motel.BuscarhabitacionPrecio(self.cedula, capturaPrecio)
            self.actualizar_tabla(habitacionesDisponibles)
            self.ventana.lineedit_precioBus.setText("")

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
        self.listCategorias = []

        self.ventanaC.pushButton_aceptar.clicked.connect(self.definir_categorias)
        self.ventanaC.pushButton_aceptarHab.clicked.connect(self.agregar_habitacion)
        self.ventanaC.comboBox_jacuzzi.addItems(self.servicios)
        self.ventanaC.comboBox_sauna.addItems(self.servicios)
        self.ventanaC.comboBox_turco.addItems(self.servicios)
        self.ventanaC.comboBox_sillaTantra.addItems(self.servicios)
        self.ventanaC.comboBox_categorias.addItems(self.lista_categorias())
        self.ventanaC.comboBox_estado.addItems(self.estados)

    def lista_categorias(self):
        for i in range(len(self.categorias)):
            self.listCategorias.append(self.categorias[i][0])

        return self.listCategorias

    def agregar_habitacion(self):
        capturaNumero = self.ventanaC.lineedit_numHabitacion.text()
        capturaCategoria = self.ventanaC.comboBox_categorias.currentText()
        capturaEstado = self.ventanaC.comboBox_estado.currentText()

        if capturaNumero != "" :
            try:
                self.motel.Agregarhabitacion(capturaNumero, self.cedula, capturaCategoria, capturaEstado)
            except HabitacionExistenteError as e:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error Agregando Habitacion.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(e.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Habitacion agregada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.ventanaC.lineedit_numHabitacion.setText("")

        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
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
        capturaJacuzzi = self.ventanaC.comboBox_jacuzzi.currentText()
        capturaSauna = self.ventanaC.comboBox_sauna.currentText()
        capturaTurco = self.ventanaC.comboBox_turco.currentText()
        capturaSilla = self.ventanaC.comboBox_sillaTantra.currentText()
        capturaOtros = self.ventanaC.lineedit_otros.text()


        if (capturaNombreCategoria != "" and capturaCapacidad != "" and capturaTipoEntrada != "" and capturaPrecioBase != ""
                and capturaPrecioAdicional != "" and capturaPersonaAdicional != ""):
            try:
                self.motel.AgregarCategoria(self.cedula,capturaNombreCategoria,capturaCapacidad,capturaTipoEntrada,
                                            capturaPrecioBase, capturaPrecioAdicional, capturaPersonaAdicional,capturaJacuzzi,
                                            capturaSauna, capturaTurco, capturaSilla, capturaOtros)
            except CategoriaExistenteError as e:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error Agregando Categoria.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(e.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Categoria agregada correctamente.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

                self.ventanaC.lineedit_nombreCategoria.setText("")
                self.ventanaC.lineedit_capacidad.setText("")
                self.ventanaC.lineedit_tipoEntrada.setText("")
                self.ventanaC.lineedit_precioBase.setText("")
                self.ventanaC.lineedit_precioAdicional.setText("")
                self.ventanaC.lineedit_personaAdicional.setText("")
                self.ventanaC.lineedit_precioAdicional.setText("")
                self.ventanaC.lineedit_otros.setText("")






        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Todos los campos obligatorios debe ingresarlos.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


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
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Todos los campos son obligatorios, debe ingresarlos.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

class DialogoCrearHabitaciones(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogoCrearHabitaciones()
        self.ui.setupUi(self)

    def accept(self) -> None:
        capturaNumHabitacion = self.ui.lineedit_numHabitacion.text()
        capturaTipo = self.ui.lineedit_tipo.text()
        capturaCapacidad = self.ui.lineedit_capacidad.text()
        capturaTipoEntrada = self.ui.lineedit_tipoEntrada.text()

        if capturaNumHabitacion != "" and capturaTipo != "" and capturaCapacidad != "" and capturaTipoEntrada != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Todos los campos obligatorios debe ingresarlos.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

class DialogoModificarHabitaciones(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self,parent)
        self.ui = Ui_DialogoModificarHabitaciones()
        self.ui.setupUi(self)

    def accept(self) -> None:
        capturaNumHabitacion = self.ui.lineedit_numeroHabitacion.text()

        if capturaNumHabitacion != "":
            super().accept()
        else:

            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Primero debe ingresar el numero de la habitacion ")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()