import sys

from Motel.Mundo import conexion
from Motel.Mundo.mundo import *
from Motel.Vista.gui.ui_DialogoCrearHabitaciones import Ui_DialogoCrearHabitaciones
from Motel.Vista.gui.ui_DialogoModificarHabitaciones import Ui_DialogoModificarHabitaciones
from Motel.Vista.gui.ui_VentanaDeInicio import Ui_VentanaDeInicio
from Motel.Vista.gui.ui_DialogoCrearUsuario import Ui_DialogoCrearUsuario
from Motel.Vista.gui.imgs import *
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


        self.ventana.pbutton_configuracion.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_configuracion))
        self.ventana.pbutton_entradas.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_entradas))
        self.ventana.pbutton_reservas.clicked.connect(lambda: self.ventana.pages.setCurrentWidget(self.ventana.page_reservas))
        self.ventana.label_bienvenida.setText(f"Bienvenido a InTouch\n                              {self.nombreUsuario}")
        if self.cedula == '1000410302' or self.cedula == '1125618030' or self.cedula == '1000414766':
           self.ventana.pbutton_crearUsuario.setEnabled(True)
        self.ventana.pbutton_crearUsuario.clicked.connect(self.abrir_dialogo_crearUsuario)
        self.ventana.pbutton_configurarHabitaciones.clicked.connect(self.abrir_dialogo_crearHabitaciones)
        self.ventana.pbutton_modificarHabitaciones.clicked.connect(self.abrir_dialogo_modificarHabitaciones)
        self.ventana.pbutton_entradas.clicked.connect(self.registrar_entrada)


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


    def abrir_dialogo_crearHabitaciones(self):

        dialogo = DialogoCrearHabitaciones(self)
        resp = dialogo.exec()

        if resp == QDialog.Accepted:
            capturaNumHabitacion = dialogo.ui.lineedit_numHabitacion.text()
            capturaTipo = dialogo.ui.lineedit_tipo.text()
            capturaCapacidad = dialogo.ui.lineedit_capacidad.text()
            capturaTipoEntrada = dialogo.ui.lineedit_tipoEntrada.text()
            capturaEstado = dialogo.ui.lineedit_estado.text()
            if capturaEstado == "":
                capturaEstado = 'Disponible'

            try:
                self.motel.Agregarhabitacion(self.cedula, capturaNumHabitacion, capturaTipo, capturaCapacidad, capturaTipoEntrada, capturaEstado)
            except HabitacionExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error Agregando Habitacion.")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Operacion Exitosa")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Habitacion agregada correctamente.")
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

    def registrar_entrada(self):
        habitacionesDisponibles = self.motel.BuscarhabitacionDisponible(self.cedula)
        self.ventana.listView_habitacionesDisponibles.setModel(habitacionesDisponibles)




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