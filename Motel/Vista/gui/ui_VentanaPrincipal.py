# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipalwJOnHT.ui'
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
        VentanaPrincipal.resize(720, 394)
        VentanaPrincipal.setMinimumSize(QSize(720, 394))
        VentanaPrincipal.setMaximumSize(QSize(720, 394))
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
        self.pages.setGeometry(QRect(0, 0, 531, 401))
        self.pages.setMinimumSize(QSize(531, 401))
        self.pages.setMaximumSize(QSize(531, 401))
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
        self.label_bienvenida.setScaledContents(True)
        self.pages.addWidget(self.page)
        self.page_entradas = QWidget()
        self.page_entradas.setObjectName(u"page_entradas")
        self.tabWidget = QTabWidget(self.page_entradas)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(5, 20, 506, 361))
        self.tabWidget.setMinimumSize(QSize(506, 361))
        self.tabWidget.setMaximumSize(QSize(506, 361))
        self.tabWidget.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pbutton_registrar = QPushButton(self.tab)
        self.pbutton_registrar.setObjectName(u"pbutton_registrar")
        self.pbutton_registrar.setGeometry(QRect(360, 310, 121, 21))
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
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 310, 131, 21))
        self.label_4.setStyleSheet(u"background-color: None;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tableHabitacionesDisp = QTableWidget(self.tab)
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
        self.tableHabitacionesDisp.setGeometry(QRect(30, 90, 451, 201))
        self.tableHabitacionesDisp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 0, 491, 80))
        self.frame_2.setMinimumSize(QSize(491, 80))
        self.frame_2.setMaximumSize(QSize(491, 80))
        self.frame_2.setStyleSheet(u"background-color: None;\n"
"")
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
        self.label.setStyleSheet(u"background-color: None;")

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

        self.lineedit_numHab = QLineEdit(self.tab)
        self.lineedit_numHab.setObjectName(u"lineedit_numHab")
        self.lineedit_numHab.setGeometry(QRect(240, 310, 113, 20))
        self.lineedit_numHab.setStyleSheet(u"background-color: None;\n"
"")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableHabitacionesOcupadas = QTableWidget(self.tab_2)
        if (self.tableHabitacionesOcupadas.columnCount() < 4):
            self.tableHabitacionesOcupadas.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableHabitacionesOcupadas.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableHabitacionesOcupadas.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableHabitacionesOcupadas.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableHabitacionesOcupadas.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableHabitacionesOcupadas.setObjectName(u"tableHabitacionesOcupadas")
        self.tableHabitacionesOcupadas.setGeometry(QRect(30, 70, 451, 201))
        self.tableHabitacionesOcupadas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineedit_numHab_salida = QLineEdit(self.tab_2)
        self.lineedit_numHab_salida.setObjectName(u"lineedit_numHab_salida")
        self.lineedit_numHab_salida.setGeometry(QRect(240, 290, 113, 20))
        self.lineedit_numHab_salida.setStyleSheet(u"background-color: None;\n"
"")
        self.pbutton_registrar_salida = QPushButton(self.tab_2)
        self.pbutton_registrar_salida.setObjectName(u"pbutton_registrar_salida")
        self.pbutton_registrar_salida.setGeometry(QRect(360, 290, 121, 21))
        self.pbutton_registrar_salida.setStyleSheet(u"\n"
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
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 290, 131, 21))
        self.label_5.setStyleSheet(u"background-color: None;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tabWidget.addTab(self.tab_2, "")
        self.pages.addWidget(self.page_entradas)
        self.page_configuracion = QWidget()
        self.page_configuracion.setObjectName(u"page_configuracion")
        self.pbutton_crearUsuario = QPushButton(self.page_configuracion)
        self.pbutton_crearUsuario.setObjectName(u"pbutton_crearUsuario")
        self.pbutton_crearUsuario.setEnabled(False)
        self.pbutton_crearUsuario.setGeometry(QRect(40, 40, 127, 61))
        self.pbutton_crearUsuario.setMinimumSize(QSize(127, 61))
        self.pbutton_crearUsuario.setMaximumSize(QSize(127, 61))
        self.pbutton_crearUsuario.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"\n"
"\n"
"}")
        self.pbutton_crearUsuario.setIconSize(QSize(112, 86))
        self.pbutton_configurarHabitaciones = QPushButton(self.page_configuracion)
        self.pbutton_configurarHabitaciones.setObjectName(u"pbutton_configurarHabitaciones")
        self.pbutton_configurarHabitaciones.setGeometry(QRect(260, 40, 205, 61))
        self.pbutton_configurarHabitaciones.setMinimumSize(QSize(205, 61))
        self.pbutton_configurarHabitaciones.setMaximumSize(QSize(205, 61))
        self.pbutton_configurarHabitaciones.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";;\n"
"\n"
"}")
        self.pbutton_configurarHabitaciones.setIconSize(QSize(205, 61))
        self.pbutton_configurarHabitaciones.setCheckable(False)
        self.pbutton_modificarHabitaciones = QPushButton(self.page_configuracion)
        self.pbutton_modificarHabitaciones.setObjectName(u"pbutton_modificarHabitaciones")
        self.pbutton_modificarHabitaciones.setGeometry(QRect(260, 160, 205, 61))
        self.pbutton_modificarHabitaciones.setMinimumSize(QSize(205, 61))
        self.pbutton_modificarHabitaciones.setMaximumSize(QSize(205, 61))
        self.pbutton_modificarHabitaciones.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"}")
        self.pbutton_modificarHabitaciones.setIconSize(QSize(112, 86))
        self.pages.addWidget(self.page_configuracion)
        self.page_reservas = QWidget()
        self.page_reservas.setObjectName(u"page_reservas")
        self.tabWidget_2 = QTabWidget(self.page_reservas)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 10, 506, 361))
        self.tabWidget_2.setMinimumSize(QSize(506, 361))
        self.tabWidget_2.setMaximumSize(QSize(506, 361))
        self.tabWidget_2.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pbutton_reservar = QPushButton(self.tab_3)
        self.pbutton_reservar.setObjectName(u"pbutton_reservar")
        self.pbutton_reservar.setGeometry(QRect(360, 310, 121, 21))
        self.pbutton_reservar.setStyleSheet(u"\n"
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
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 220, 131, 21))
        self.label_6.setStyleSheet(u"background-color: None;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tableHabitacionesDisp_reservar = QTableWidget(self.tab_3)
        if (self.tableHabitacionesDisp_reservar.columnCount() < 4):
            self.tableHabitacionesDisp_reservar.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableHabitacionesDisp_reservar.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableHabitacionesDisp_reservar.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableHabitacionesDisp_reservar.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableHabitacionesDisp_reservar.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.tableHabitacionesDisp_reservar.setObjectName(u"tableHabitacionesDisp_reservar")
        self.tableHabitacionesDisp_reservar.setGeometry(QRect(30, 10, 451, 201))
        self.tableHabitacionesDisp_reservar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_numeroHabitacion_reserva = QComboBox(self.tab_3)
        self.comboBox_numeroHabitacion_reserva.setObjectName(u"comboBox_numeroHabitacion_reserva")
        self.comboBox_numeroHabitacion_reserva.setGeometry(QRect(370, 220, 111, 22))
        self.comboBox_numeroHabitacion_reserva.setStyleSheet(u"background-color: None;")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 270, 131, 21))
        self.label_7.setStyleSheet(u"background-color: None;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 220, 131, 21))
        self.label_8.setStyleSheet(u"background-color: None;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.lineedit_NumeroReserva = QLineEdit(self.tab_3)
        self.lineedit_NumeroReserva.setObjectName(u"lineedit_NumeroReserva")
        self.lineedit_NumeroReserva.setGeometry(QRect(110, 220, 113, 20))
        self.lineedit_NumeroReserva.setStyleSheet(u"background-color:None;")
        self.lineedit_fechaReserva = QLineEdit(self.tab_3)
        self.lineedit_fechaReserva.setObjectName(u"lineedit_fechaReserva")
        self.lineedit_fechaReserva.setGeometry(QRect(110, 270, 131, 20))
        self.lineedit_fechaReserva.setStyleSheet(u"background-color:None;")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableHabitaciones_reservadas = QTableWidget(self.tab_4)
        if (self.tableHabitaciones_reservadas.columnCount() < 3):
            self.tableHabitaciones_reservadas.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableHabitaciones_reservadas.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableHabitaciones_reservadas.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableHabitaciones_reservadas.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.tableHabitaciones_reservadas.setObjectName(u"tableHabitaciones_reservadas")
        self.tableHabitaciones_reservadas.setGeometry(QRect(80, 70, 361, 211))
        self.tableHabitaciones_reservadas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineedit_numReserva_entradaReserva = QLineEdit(self.tab_4)
        self.lineedit_numReserva_entradaReserva.setObjectName(u"lineedit_numReserva_entradaReserva")
        self.lineedit_numReserva_entradaReserva.setGeometry(QRect(240, 310, 113, 20))
        self.lineedit_numReserva_entradaReserva.setStyleSheet(u"background-color: None;\n"
"")
        self.pbutton_registrar_entrada_reserva = QPushButton(self.tab_4)
        self.pbutton_registrar_entrada_reserva.setObjectName(u"pbutton_registrar_entrada_reserva")
        self.pbutton_registrar_entrada_reserva.setGeometry(QRect(360, 310, 121, 21))
        self.pbutton_registrar_entrada_reserva.setStyleSheet(u"\n"
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
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 310, 131, 21))
        self.label_10.setStyleSheet(u"background-color: None;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 491, 80))
        self.frame_4.setMinimumSize(QSize(491, 80))
        self.frame_4.setMaximumSize(QSize(491, 80))
        self.frame_4.setStyleSheet(u"background-color: None;\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.comboBox_numeroReserva = QComboBox(self.frame_4)
        self.comboBox_numeroReserva.setObjectName(u"comboBox_numeroReserva")
        self.comboBox_numeroReserva.setGeometry(QRect(170, 30, 111, 20))
        self.comboBox_numeroReserva.setStyleSheet(u"background-color: None;")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 30, 111, 16))
        self.label_11.setStyleSheet(u"background-color: None;")
        self.pbutton_BuscarReserva = QPushButton(self.frame_4)
        self.pbutton_BuscarReserva.setObjectName(u"pbutton_BuscarReserva")
        self.pbutton_BuscarReserva.setGeometry(QRect(360, 30, 121, 20))
        self.pbutton_BuscarReserva.setStyleSheet(u"\n"
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
        self.tabWidget_2.addTab(self.tab_4, "")
        self.pages.addWidget(self.page_reservas)
        self.frame_botonoes = QFrame(VentanaPrincipal)
        self.frame_botonoes.setObjectName(u"frame_botonoes")
        self.frame_botonoes.setGeometry(QRect(0, 0, 170, 394))
        self.frame_botonoes.setMinimumSize(QSize(170, 394))
        self.frame_botonoes.setMaximumSize(QSize(170, 394))
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
        self.pbutton_entradas.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";;\n"
"\n"
"}")
        self.pbutton_entradas.setIconSize(QSize(112, 86))

        self.verticalLayout.addWidget(self.pbutton_entradas)

        self.pbutton_configuracion = QPushButton(self.frame_botonoes)
        self.pbutton_configuracion.setObjectName(u"pbutton_configuracion")
        self.pbutton_configuracion.setMinimumSize(QSize(121, 61))
        self.pbutton_configuracion.setMaximumSize(QSize(121, 61))
        self.pbutton_configuracion.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";;\n"
"\n"
"}")
        self.pbutton_configuracion.setIconSize(QSize(112, 86))

        self.verticalLayout.addWidget(self.pbutton_configuracion)

        self.pbutton_reservas = QPushButton(self.frame_botonoes)
        self.pbutton_reservas.setObjectName(u"pbutton_reservas")
        self.pbutton_reservas.setMinimumSize(QSize(121, 61))
        self.pbutton_reservas.setMaximumSize(QSize(121, 61))
        self.pbutton_reservas.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 75 14pt \"Script MT Bold\";;\n"
"\n"
"}")
        self.pbutton_reservas.setIconSize(QSize(112, 86))

        self.verticalLayout.addWidget(self.pbutton_reservas)


        self.retranslateUi(VentanaPrincipal)

        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Menu Principal", None))
        self.label_bienvenida.setText("")
        self.pbutton_registrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Registrar entrada", None))
        self.label_4.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Habitacion numero</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableHabitacionesDisp.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaPrincipal", u"Numero", None));
        ___qtablewidgetitem1 = self.tableHabitacionesDisp.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaPrincipal", u"Categoria", None));
        ___qtablewidgetitem2 = self.tableHabitacionesDisp.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaPrincipal", u"Capacidad", None));
        ___qtablewidgetitem3 = self.tableHabitacionesDisp.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio", None));
        self.label.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Categoria </span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Precio</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Capacidad</span></p></body></html>", None))
        self.pbutton_filtrar.setText(QCoreApplication.translate("VentanaPrincipal", u"Filtrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("VentanaPrincipal", u"Entradas", None))
        ___qtablewidgetitem4 = self.tableHabitacionesOcupadas.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaPrincipal", u"Numero", None));
        ___qtablewidgetitem5 = self.tableHabitacionesOcupadas.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaPrincipal", u"Categoria", None));
        ___qtablewidgetitem6 = self.tableHabitacionesOcupadas.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VentanaPrincipal", u"Capacidad", None));
        ___qtablewidgetitem7 = self.tableHabitacionesOcupadas.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio", None));
        self.pbutton_registrar_salida.setText(QCoreApplication.translate("VentanaPrincipal", u"Registrar salida", None))
        self.label_5.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Habitacion numero</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("VentanaPrincipal", u"Salidas", None))
        self.pbutton_crearUsuario.setText(QCoreApplication.translate("VentanaPrincipal", u"Crear Usuario", None))
        self.pbutton_configurarHabitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Configuracion", None))
        self.pbutton_modificarHabitaciones.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar Habitaciones ", None))
        self.pbutton_reservar.setText(QCoreApplication.translate("VentanaPrincipal", u"Reservar", None))
        self.label_6.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Habitacion numero</span></p></body></html>", None))
        ___qtablewidgetitem8 = self.tableHabitacionesDisp_reservar.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VentanaPrincipal", u"Numero", None));
        ___qtablewidgetitem9 = self.tableHabitacionesDisp_reservar.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VentanaPrincipal", u"Categoria", None));
        ___qtablewidgetitem10 = self.tableHabitacionesDisp_reservar.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VentanaPrincipal", u"Capacidad", None));
        ___qtablewidgetitem11 = self.tableHabitacionesDisp_reservar.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("VentanaPrincipal", u"Precio", None));
        self.comboBox_numeroHabitacion_reserva.setCurrentText("")
        self.label_7.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Fecha y hora</span></p><p><br/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Numero reserva</span></p></body></html>", None))
        self.lineedit_fechaReserva.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"AAAA-DD-MM hh:mm:ss", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("VentanaPrincipal", u"Reservar", None))
        ___qtablewidgetitem12 = self.tableHabitaciones_reservadas.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("VentanaPrincipal", u"Numero Reserva", None));
        ___qtablewidgetitem13 = self.tableHabitaciones_reservadas.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("VentanaPrincipal", u"Numero Habitacion ", None));
        ___qtablewidgetitem14 = self.tableHabitaciones_reservadas.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("VentanaPrincipal", u"Fecha Reserva", None));
        self.pbutton_registrar_entrada_reserva.setText(QCoreApplication.translate("VentanaPrincipal", u"Registrar entrada", None))
        self.label_10.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Reserva numero</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Numero reserva</span></p></body></html>", None))
        self.pbutton_BuscarReserva.setText(QCoreApplication.translate("VentanaPrincipal", u"Buscar reserva ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("VentanaPrincipal", u"Entrada reserva", None))
        self.pbutton_entradas.setText(QCoreApplication.translate("VentanaPrincipal", u"Entradas", None))
        self.pbutton_configuracion.setText(QCoreApplication.translate("VentanaPrincipal", u"Configuracion", None))
        self.pbutton_reservas.setText(QCoreApplication.translate("VentanaPrincipal", u"Reservas", None))
    # retranslateUi

