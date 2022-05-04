# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipalubNyyJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(624, 359)
        VentanaPrincipal.setMinimumSize(QSize(624, 359))
        VentanaPrincipal.setMaximumSize(QSize(624, 379))
        VentanaPrincipal.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.frame = QFrame(VentanaPrincipal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(185, -1, 441, 361))
        self.frame.setToolTipDuration(-1)
        self.frame.setStyleSheet(u"\n"
"background-color: None;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pages = QStackedWidget(self.frame)
        self.pages.setObjectName(u"pages")
        self.pages.setEnabled(True)
        self.pages.setGeometry(QRect(0, 0, 441, 361))
        self.pages.setStyleSheet(u"background-color: rgba(0,0,0,0%);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_bienvenida = QLabel(self.page)
        self.label_bienvenida.setObjectName(u"label_bienvenida")
        self.label_bienvenida.setGeometry(QRect(10, 10, 411, 321))
        self.label_bienvenida.setMinimumSize(QSize(411, 321))
        self.label_bienvenida.setMaximumSize(QSize(411, 321))
        self.label_bienvenida.setFocusPolicy(Qt.TabFocus)
        self.label_bienvenida.setStyleSheet(u"font: 75 18pt \"Script MT Bold\";")
        self.pages.addWidget(self.page)
        self.page_entradas = QWidget()
        self.page_entradas.setObjectName(u"page_entradas")
        self.listView_habitacionesDisponibles = QListView(self.page_entradas)
        self.listView_habitacionesDisponibles.setObjectName(u"listView_habitacionesDisponibles")
        self.listView_habitacionesDisponibles.setGeometry(QRect(10, 70, 256, 241))
        self.pages.addWidget(self.page_entradas)
        self.page_configuracion = QWidget()
        self.page_configuracion.setObjectName(u"page_configuracion")
        self.pbutton_crearUsuario = QPushButton(self.page_configuracion)
        self.pbutton_crearUsuario.setObjectName(u"pbutton_crearUsuario")
        self.pbutton_crearUsuario.setEnabled(False)
        self.pbutton_crearUsuario.setGeometry(QRect(20, 40, 127, 61))
        self.pbutton_crearUsuario.setMinimumSize(QSize(127, 61))
        self.pbutton_crearUsuario.setMaximumSize(QSize(127, 61))
        self.pbutton_crearUsuario.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border- color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border- color: rgb(0, 0, 0);\n"
"}")
        self.pbutton_crearUsuario.setIconSize(QSize(112, 86))
        self.pbutton_configurarHabitaciones = QPushButton(self.page_configuracion)
        self.pbutton_configurarHabitaciones.setObjectName(u"pbutton_configurarHabitaciones")
        self.pbutton_configurarHabitaciones.setGeometry(QRect(200, 40, 205, 61))
        self.pbutton_configurarHabitaciones.setMinimumSize(QSize(205, 61))
        self.pbutton_configurarHabitaciones.setMaximumSize(QSize(205, 61))
        self.pbutton_configurarHabitaciones.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border- color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border- color: rgb(0, 0, 0);\n"
"}")
        self.pbutton_configurarHabitaciones.setIconSize(QSize(112, 86))
        self.pbutton_modificarHabitaciones = QPushButton(self.page_configuracion)
        self.pbutton_modificarHabitaciones.setObjectName(u"pbutton_modificarHabitaciones")
        self.pbutton_modificarHabitaciones.setGeometry(QRect(200, 150, 205, 61))
        self.pbutton_modificarHabitaciones.setMinimumSize(QSize(205, 61))
        self.pbutton_modificarHabitaciones.setMaximumSize(QSize(205, 61))
        self.pbutton_modificarHabitaciones.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border- color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border- color: rgb(0, 0, 0);\n"
"}")
        self.pbutton_modificarHabitaciones.setIconSize(QSize(112, 86))
        self.pages.addWidget(self.page_configuracion)
        self.page_reservas = QWidget()
        self.page_reservas.setObjectName(u"page_reservas")
        self.pushButton_3 = QPushButton(self.page_reservas)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 100, 241, 121))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pages.addWidget(self.page_reservas)
        self.frame_botonoes = QFrame(VentanaPrincipal)
        self.frame_botonoes.setObjectName(u"frame_botonoes")
        self.frame_botonoes.setGeometry(QRect(0, 0, 170, 359))
        self.frame_botonoes.setMinimumSize(QSize(170, 359))
        self.frame_botonoes.setMaximumSize(QSize(110, 359))
        self.frame_botonoes.setToolTipDuration(-1)
        self.frame_botonoes.setLayoutDirection(Qt.LeftToRight)
        self.frame_botonoes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-right: 5px solid;\n"
"border-top: 5px solid;\n"
"border-bottom: 5px solid;")
        self.frame_botonoes.setFrameShape(QFrame.StyledPanel)
        self.frame_botonoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_botonoes)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)
        self.pbutton_entradas = QPushButton(self.frame_botonoes)
        self.pbutton_entradas.setObjectName(u"pbutton_entradas")
        self.pbutton_entradas.setMinimumSize(QSize(121, 61))
        self.pbutton_entradas.setMaximumSize(QSize(121, 61))
        self.pbutton_entradas.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border-color: rgb(255, 3, 3)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border-color: rgb(255, 3, 3)\n"
"\n"
"}")
        self.pbutton_entradas.setIconSize(QSize(112, 86))

        self.verticalLayout.addWidget(self.pbutton_entradas)

        self.pbutton_configuracion = QPushButton(self.frame_botonoes)
        self.pbutton_configuracion.setObjectName(u"pbutton_configuracion")
        self.pbutton_configuracion.setMinimumSize(QSize(121, 61))
        self.pbutton_configuracion.setMaximumSize(QSize(121, 61))
        self.pbutton_configuracion.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border-color: rgb(255, 3, 3);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border-color: rgb(255, 3, 3)\n"
"}")
        self.pbutton_configuracion.setIconSize(QSize(112, 86))

        self.verticalLayout.addWidget(self.pbutton_configuracion)

        self.pbutton_reservas = QPushButton(self.frame_botonoes)
        self.pbutton_reservas.setObjectName(u"pbutton_reservas")
        self.pbutton_reservas.setMinimumSize(QSize(121, 61))
        self.pbutton_reservas.setMaximumSize(QSize(121, 61))
        self.pbutton_reservas.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255,255,255);\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border-color: rgb(255, 3, 3);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"	color: rgb(0,0, 0);\n"
"	border: 5px solid;\n"
"	border-color: rgb(255, 3, 3)\n"
"\n"
"}")
        self.pbutton_reservas.setIconSize(QSize(112, 86))

        self.verticalLayout.addWidget(self.pbutton_reservas)


        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Menu Principal", None))
        self.label_bienvenida.setText("")
        self.pbutton_crearUsuario.setText(QCoreApplication.translate("VentanaPrincipal", u"Crear Usuario", None))
        self.pbutton_configurarHabitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar Habitaciones ", None))
        self.pbutton_modificarHabitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar Habitaciones ", None))
        self.pushButton_3.setText(QCoreApplication.translate("VentanaPrincipal", u"Reservas", None))
        self.pbutton_entradas.setText(QCoreApplication.translate("VentanaPrincipal", u"Entradas", None))
        self.pbutton_configuracion.setText(QCoreApplication.translate("VentanaPrincipal", u"Configuracion", None))
        self.pbutton_reservas.setText(QCoreApplication.translate("VentanaPrincipal", u"Reservas", None))
    # retranslateUi

