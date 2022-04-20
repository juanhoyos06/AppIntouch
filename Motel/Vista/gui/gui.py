import sys

from Motel.Mundo.conexion import Conexion
from Motel.Mundo.mundo import *
from Motel.Vista.gui.ui_VentanaDeInicio import Ui_VentanaDeInicio
from Motel.Mundo.errores import UsuarioExistenteError,UsuarioNoExistenteError
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QIntValidator, QStandardItemModel, QStandardItem, QIcon
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QInputDialog
from PySide2 import QtGui
from Motel.Vista.gui.ui_VentanaPrincipal import Ui_VentanaPrincipal


class VentanaLogin(QMainWindow):
    def __init__(self, motel: Motel):
        QMainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.motel = motel
        self.ui = Ui_VentanaDeInicio()
        self.ui.setupUi(self)
        self._configurar()
        self.show()


    def _configurar(self):
        self.ui.pbutton_ingresar.clicked.connect(self.iniciar_sesion)

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
                self.hide()
                self.ventana = VentanaPrincipal()
                self.ventana.show()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
       super().__init__()
       self.ventana = Ui_VentanaPrincipal()
       self.ventana.setupUi(self)





