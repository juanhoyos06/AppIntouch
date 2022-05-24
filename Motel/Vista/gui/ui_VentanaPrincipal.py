# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipalztZEGT.ui'
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
        VentanaPrincipal.resize(700, 379)
        VentanaPrincipal.setMinimumSize(QSize(700, 359))
        VentanaPrincipal.setMaximumSize(QSize(700, 379))
        VentanaPrincipal.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.frame = QFrame(VentanaPrincipal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(185, -1, 511, 381))
        self.frame.setToolTipDuration(-1)
        self.frame.setStyleSheet(u"\n"
"background-color: None;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pages = QStackedWidget(self.frame)
        self.pages.setObjectName(u"pages")
        self.pages.setEnabled(True)
        self.pages.setGeometry(QRect(0, 0, 511, 361))
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
        self.tableHabitacionesDisp = QTableWidget(self.page_entradas)
        if (self.tableHabitacionesDisp.columnCount() < 4):
            self.tableHabitacionesDisp.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableHabitacionesDisp.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableHabitacionesDisp.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableHabitacionesDisp.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableHabitacionesDisp.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableHabitacionesDisp.setObjectName(u"tableHabitacionesDisp")
        self.tableHabitacionesDisp.setGeometry(QRect(30, 110, 451, 201))
        self.tableHabitacionesDisp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.page_entradas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 20, 491, 80))
        self.frame_2.setMinimumSize(QSize(491, 80))
        self.frame_2.setMaximumSize(QSize(491, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_categoriasBuscar = QComboBox(self.frame_2)
        self.comboBox_categoriasBuscar.setObjectName(u"comboBox_categoriasBuscar")
        self.comboBox_categoriasBuscar.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.comboBox_categoriasBuscar, 0, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.lineedit_capacidadBus = QLineEdit(self.frame_2)
        self.lineedit_capacidadBus.setObjectName(u"lineedit_capacidadBus")
        self.lineedit_capacidadBus.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_capacidadBus, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.pbutton_filtrar = QPushButton(self.frame_2)
        self.pbutton_filtrar.setObjectName(u"pbutton_filtrar")
        self.pbutton_filtrar.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	border: 0.5px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	border-color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.pbutton_filtrar, 2, 8, 1, 1)

        self.lineedit_precioBus = QLineEdit(self.frame_2)
        self.lineedit_precioBus.setObjectName(u"lineedit_precioBus")
        self.lineedit_precioBus.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_precioBus, 0, 8, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 8, 1, 1)

        self.label_4 = QLabel(self.page_entradas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 330, 131, 21))
        self.label_4.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.lineedit_numHab = QLineEdit(self.page_entradas)
        self.lineedit_numHab.setObjectName(u"lineedit_numHab")
        self.lineedit_numHab.setGeometry(QRect(240, 330, 113, 20))
        self.lineedit_numHab.setStyleSheet(u"background-color: None;\n"
"")
        self.pbutton_registrar = QPushButton(self.page_entradas)
        self.pbutton_registrar.setObjectName(u"pbutton_registrar")
        self.pbutton_registrar.setGeometry(QRect(380, 330, 91, 21))
        self.pbutton_registrar.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	border: 0.5px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	border-color: rgb(0, 0, 0);\n"
"\n"
"}")
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
        self.pbutton_configurarHabitaciones.setStyleSheet(u"font: 12pt \"Sitka Small\";\n"
"border: 0.5px solid;")
        icon = QIcon()
        icon.addFile(u"imgs/simbolo-de-interfaz-de-configuracion-de-dos-ruedas-dentadas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbutton_configurarHabitaciones.setIcon(icon)
        self.pbutton_configurarHabitaciones.setIconSize(QSize(205, 61))
        self.pbutton_configurarHabitaciones.setCheckable(False)
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
        self.frame_botonoes.setGeometry(QRect(0, 0, 170, 379))
        self.frame_botonoes.setMinimumSize(QSize(170, 379))
        self.frame_botonoes.setMaximumSize(QSize(110, 379))
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

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Menu Principal", None))
        self.label_bienvenida.setText("")
        ___qtablewidgetitem = self.tableHabitacionesDisp.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaPrincipal", u"Numero", None));
        ___qtablewidgetitem1 = self.tableHabitacionesDisp.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaPrincipal", u"Categoria", None));
        ___qtablewidgetitem2 = self.tableHabitacionesDisp.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaPrincipal", u"Capacidad", None));
        ___qtablewidgetitem3 = self.tableHabitacionesDisp.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio", None));
        self.label.setText(QCoreApplication.translate("VentanaPrincipal", u"Categoria", None))
        self.label_3.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio", None))
        self.label_2.setText(QCoreApplication.translate("VentanaPrincipal", u"Capacidad", None))
        self.pbutton_filtrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Filtrar", None))
        self.label_4.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Habitacion numero: </span></p></body></html>", None))
        self.pbutton_registrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Registrar", None))
        self.pbutton_crearUsuario.setText(QCoreApplication.translate("VentanaPrincipal", u"Crear Usuario", None))
        self.pbutton_configurarHabitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Configuracion", None))
        self.pbutton_modificarHabitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar Habitaciones ", None))
        self.pushButton_3.setText(QCoreApplication.translate("VentanaPrincipal", u"Reservas", None))
        self.pbutton_entradas.setText(QCoreApplication.translate("VentanaPrincipal", u"Entradas", None))
        self.pbutton_configuracion.setText(QCoreApplication.translate("VentanaPrincipal", u"Configuracion", None))
        self.pbutton_reservas.setText(QCoreApplication.translate("VentanaPrincipal", u"Reservas", None))
    # retranslateUi

