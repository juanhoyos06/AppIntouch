# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaModificargqZzVy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaModificar(object):
    def setupUi(self, VentanaModificar):
        if not VentanaModificar.objectName():
            VentanaModificar.setObjectName(u"VentanaModificar")
        VentanaModificar.resize(643, 525)
        VentanaModificar.setMinimumSize(QSize(643, 525))
        VentanaModificar.setMaximumSize(QSize(643, 525))
        VentanaModificar.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.tabWidget = QTabWidget(VentanaModificar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 625, 507))
        self.tabWidget.setMinimumSize(QSize(625, 507))
        self.tabWidget.setMaximumSize(QSize(625, 507))
        self.ModificarCategorias = QWidget()
        self.ModificarCategorias.setObjectName(u"ModificarCategorias")
        self.frame_opciones = QFrame(self.ModificarCategorias)
        self.frame_opciones.setObjectName(u"frame_opciones")
        self.frame_opciones.setEnabled(True)
        self.frame_opciones.setGeometry(QRect(10, 300, 571, 121))
        self.frame_opciones.setStyleSheet(u"background-color: None;")
        self.frame_opciones.setFrameShape(QFrame.StyledPanel)
        self.frame_opciones.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_opciones)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.lineedit_tipoEntrada = QLineEdit(self.frame_opciones)
        self.lineedit_tipoEntrada.setObjectName(u"lineedit_tipoEntrada")

        self.gridLayout.addWidget(self.lineedit_tipoEntrada, 1, 1, 1, 1)

        self.label_estadoHabitacion = QLabel(self.frame_opciones)
        self.label_estadoHabitacion.setObjectName(u"label_estadoHabitacion")
        self.label_estadoHabitacion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_estadoHabitacion, 1, 3, 1, 1)

        self.label_capacidadHabitacion = QLabel(self.frame_opciones)
        self.label_capacidadHabitacion.setObjectName(u"label_capacidadHabitacion")
        self.label_capacidadHabitacion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_capacidadHabitacion, 0, 3, 1, 1)

        self.label_tipoEntrada = QLabel(self.frame_opciones)
        self.label_tipoEntrada.setObjectName(u"label_tipoEntrada")
        self.label_tipoEntrada.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_tipoEntrada, 1, 0, 1, 1)

        self.lineedit_capacidadCateg = QLineEdit(self.frame_opciones)
        self.lineedit_capacidadCateg.setObjectName(u"lineedit_capacidadCateg")

        self.gridLayout.addWidget(self.lineedit_capacidadCateg, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lineedit_Nomcategoria = QLineEdit(self.frame_opciones)
        self.lineedit_Nomcategoria.setObjectName(u"lineedit_Nomcategoria")

        self.gridLayout.addWidget(self.lineedit_Nomcategoria, 0, 1, 1, 1)

        self.lineedit_precioBase = QLineEdit(self.frame_opciones)
        self.lineedit_precioBase.setObjectName(u"lineedit_precioBase")

        self.gridLayout.addWidget(self.lineedit_precioBase, 1, 4, 1, 1)

        self.label_tipoHabitacion = QLabel(self.frame_opciones)
        self.label_tipoHabitacion.setObjectName(u"label_tipoHabitacion")
        self.label_tipoHabitacion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_tipoHabitacion, 0, 0, 1, 1)

        self.label_precioHoraAdicional = QLabel(self.frame_opciones)
        self.label_precioHoraAdicional.setObjectName(u"label_precioHoraAdicional")
        self.label_precioHoraAdicional.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_precioHoraAdicional, 2, 0, 1, 1)

        self.lineedit_precioAdicional = QLineEdit(self.frame_opciones)
        self.lineedit_precioAdicional.setObjectName(u"lineedit_precioAdicional")

        self.gridLayout.addWidget(self.lineedit_precioAdicional, 2, 1, 1, 1)

        self.label_precioPersonaAdicional = QLabel(self.frame_opciones)
        self.label_precioPersonaAdicional.setObjectName(u"label_precioPersonaAdicional")
        self.label_precioPersonaAdicional.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_precioPersonaAdicional, 2, 3, 1, 1)

        self.lineedit_personaAdicional = QLineEdit(self.frame_opciones)
        self.lineedit_personaAdicional.setObjectName(u"lineedit_personaAdicional")

        self.gridLayout.addWidget(self.lineedit_personaAdicional, 2, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.label_titulo = QLabel(self.ModificarCategorias)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(90, 0, 421, 31))
        self.label_titulo.setMinimumSize(QSize(421, 31))
        self.label_titulo.setMaximumSize(QSize(421, 31))
        font = QFont()
        font.setFamily(u"Script MT Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_titulo.setFont(font)
        self.label_titulo.setCursor(QCursor(Qt.ArrowCursor))
        self.label_titulo.setLayoutDirection(Qt.LeftToRight)
        self.label_titulo.setStyleSheet(u"background-color:None;\n"
"font: 75 18pt \"Script MT Bold\";")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.tableCategorias = QTableWidget(self.ModificarCategorias)
        if (self.tableCategorias.columnCount() < 6):
            self.tableCategorias.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCategorias.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCategorias.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCategorias.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCategorias.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCategorias.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCategorias.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableCategorias.setObjectName(u"tableCategorias")
        self.tableCategorias.setGeometry(QRect(10, 40, 601, 201))
        self.tableCategorias.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.ModificarCategorias)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 270, 251, 51))
        self.label.setStyleSheet(u"background-color: None;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"color:rgb(130, 130, 130)")
        self.label.setAlignment(Qt.AlignCenter)
        self.pbutton_limpiar = QPushButton(self.ModificarCategorias)
        self.pbutton_limpiar.setObjectName(u"pbutton_limpiar")
        self.pbutton_limpiar.setGeometry(QRect(520, 440, 75, 23))
        self.pbutton_limpiar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.pbutton_modificar = QPushButton(self.ModificarCategorias)
        self.pbutton_modificar.setObjectName(u"pbutton_modificar")
        self.pbutton_modificar.setGeometry(QRect(430, 440, 75, 23))
        self.pbutton_modificar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.pbutton_refrescar = QPushButton(self.ModificarCategorias)
        self.pbutton_refrescar.setObjectName(u"pbutton_refrescar")
        self.pbutton_refrescar.setGeometry(QRect(530, 250, 71, 23))
        self.pbutton_refrescar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"")
        self.pbutton_volver = QPushButton(self.ModificarCategorias)
        self.pbutton_volver.setObjectName(u"pbutton_volver")
        self.pbutton_volver.setGeometry(QRect(30, 440, 75, 23))
        self.pbutton_volver.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.comboBox_categorias = QComboBox(self.ModificarCategorias)
        self.comboBox_categorias.setObjectName(u"comboBox_categorias")
        self.comboBox_categorias.setGeometry(QRect(20, 250, 111, 22))
        self.comboBox_categorias.setStyleSheet(u"background-color: None;")
        self.tabWidget.addTab(self.ModificarCategorias, "")
        self.ModificarHabitaciones = QWidget()
        self.ModificarHabitaciones.setObjectName(u"ModificarHabitaciones")
        self.label_titulo_2 = QLabel(self.ModificarHabitaciones)
        self.label_titulo_2.setObjectName(u"label_titulo_2")
        self.label_titulo_2.setGeometry(QRect(100, 0, 421, 31))
        self.label_titulo_2.setMinimumSize(QSize(421, 31))
        self.label_titulo_2.setMaximumSize(QSize(421, 31))
        self.label_titulo_2.setFont(font)
        self.label_titulo_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_titulo_2.setLayoutDirection(Qt.LeftToRight)
        self.label_titulo_2.setStyleSheet(u"background-color:None;\n"
"font: 75 18pt \"Script MT Bold\";")
        self.label_titulo_2.setAlignment(Qt.AlignCenter)
        self.tableHabitaciones = QTableWidget(self.ModificarHabitaciones)
        if (self.tableHabitaciones.columnCount() < 7):
            self.tableHabitaciones.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tableHabitaciones.setObjectName(u"tableHabitaciones")
        self.tableHabitaciones.setGeometry(QRect(20, 30, 591, 211))
        self.tableHabitaciones.setStyleSheet(u"background-color: None;")
        self.label_2 = QLabel(self.ModificarHabitaciones)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 270, 251, 51))
        self.label_2.setStyleSheet(u"background-color: None;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"color:rgb(130, 130, 130)")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pbutton_volver_mh = QPushButton(self.ModificarHabitaciones)
        self.pbutton_volver_mh.setObjectName(u"pbutton_volver_mh")
        self.pbutton_volver_mh.setGeometry(QRect(40, 440, 75, 23))
        self.pbutton_volver_mh.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.frame_opciones_2 = QFrame(self.ModificarHabitaciones)
        self.frame_opciones_2.setObjectName(u"frame_opciones_2")
        self.frame_opciones_2.setEnabled(True)
        self.frame_opciones_2.setGeometry(QRect(20, 300, 571, 121))
        self.frame_opciones_2.setStyleSheet(u"background-color: None;")
        self.frame_opciones_2.setFrameShape(QFrame.StyledPanel)
        self.frame_opciones_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_opciones_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_turco = QComboBox(self.frame_opciones_2)
        self.comboBox_turco.setObjectName(u"comboBox_turco")
        self.comboBox_turco.setMinimumSize(QSize(150, 20))
        self.comboBox_turco.setMaximumSize(QSize(150, 20))
        self.comboBox_turco.setStyleSheet(u"background-color: None;")

        self.gridLayout_2.addWidget(self.comboBox_turco, 1, 4, 1, 1)

        self.comboBox_sauna = QComboBox(self.frame_opciones_2)
        self.comboBox_sauna.setObjectName(u"comboBox_sauna")
        self.comboBox_sauna.setStyleSheet(u"background-color: None;")

        self.gridLayout_2.addWidget(self.comboBox_sauna, 1, 1, 1, 1)

        self.label_tipoEntrada_2 = QLabel(self.frame_opciones_2)
        self.label_tipoEntrada_2.setObjectName(u"label_tipoEntrada_2")
        self.label_tipoEntrada_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_tipoEntrada_2, 1, 0, 1, 1)

        self.lineedit_otros = QLineEdit(self.frame_opciones_2)
        self.lineedit_otros.setObjectName(u"lineedit_otros")

        self.gridLayout_2.addWidget(self.lineedit_otros, 2, 1, 1, 1)

        self.label_capacidadHabitacion_2 = QLabel(self.frame_opciones_2)
        self.label_capacidadHabitacion_2.setObjectName(u"label_capacidadHabitacion_2")
        self.label_capacidadHabitacion_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_capacidadHabitacion_2, 0, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.label_tipoHabitacion_2 = QLabel(self.frame_opciones_2)
        self.label_tipoHabitacion_2.setObjectName(u"label_tipoHabitacion_2")
        self.label_tipoHabitacion_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_tipoHabitacion_2, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.label_precioHoraAdicional_2 = QLabel(self.frame_opciones_2)
        self.label_precioHoraAdicional_2.setObjectName(u"label_precioHoraAdicional_2")
        self.label_precioHoraAdicional_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_precioHoraAdicional_2, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.comboBox_jacuzzi = QComboBox(self.frame_opciones_2)
        self.comboBox_jacuzzi.setObjectName(u"comboBox_jacuzzi")
        self.comboBox_jacuzzi.setMinimumSize(QSize(150, 20))
        self.comboBox_jacuzzi.setMaximumSize(QSize(150, 20))
        self.comboBox_jacuzzi.setStyleSheet(u"background-color: None;")

        self.gridLayout_2.addWidget(self.comboBox_jacuzzi, 0, 4, 1, 1)

        self.label_estadoHabitacion_2 = QLabel(self.frame_opciones_2)
        self.label_estadoHabitacion_2.setObjectName(u"label_estadoHabitacion_2")
        self.label_estadoHabitacion_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_estadoHabitacion_2, 1, 3, 1, 1)

        self.comboBox_categoriasMH = QComboBox(self.frame_opciones_2)
        self.comboBox_categoriasMH.setObjectName(u"comboBox_categoriasMH")
        self.comboBox_categoriasMH.setStyleSheet(u"background-color: None;")

        self.gridLayout_2.addWidget(self.comboBox_categoriasMH, 0, 1, 1, 1)

        self.pbutton_limpiar_mh = QPushButton(self.ModificarHabitaciones)
        self.pbutton_limpiar_mh.setObjectName(u"pbutton_limpiar_mh")
        self.pbutton_limpiar_mh.setGeometry(QRect(530, 440, 75, 23))
        self.pbutton_limpiar_mh.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.comboBox_numeroHabitacion = QComboBox(self.ModificarHabitaciones)
        self.comboBox_numeroHabitacion.setObjectName(u"comboBox_numeroHabitacion")
        self.comboBox_numeroHabitacion.setGeometry(QRect(30, 250, 111, 22))
        self.comboBox_numeroHabitacion.setStyleSheet(u"background-color: None;")
        self.pbutton_refrescar_2 = QPushButton(self.ModificarHabitaciones)
        self.pbutton_refrescar_2.setObjectName(u"pbutton_refrescar_2")
        self.pbutton_refrescar_2.setGeometry(QRect(530, 250, 71, 23))
        self.pbutton_refrescar_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"")
        self.pbutton_modificar_mh = QPushButton(self.ModificarHabitaciones)
        self.pbutton_modificar_mh.setObjectName(u"pbutton_modificar_mh")
        self.pbutton_modificar_mh.setGeometry(QRect(440, 440, 75, 23))
        self.pbutton_modificar_mh.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.tabWidget.addTab(self.ModificarHabitaciones, "")

        self.retranslateUi(VentanaModificar)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VentanaModificar)
    # setupUi

    def retranslateUi(self, VentanaModificar):
        VentanaModificar.setWindowTitle(QCoreApplication.translate("VentanaModificar", u"Modificar", None))
        self.label_estadoHabitacion.setText(QCoreApplication.translate("VentanaModificar", u"Precio Base", None))
        self.label_capacidadHabitacion.setText(QCoreApplication.translate("VentanaModificar", u"Capacidad ", None))
        self.label_tipoEntrada.setText(QCoreApplication.translate("VentanaModificar", u"Tipo Entrada ", None))
        self.label_tipoHabitacion.setText(QCoreApplication.translate("VentanaModificar", u"Nombre", None))
        self.label_precioHoraAdicional.setText(QCoreApplication.translate("VentanaModificar", u"Precio hora adicional", None))
        self.label_precioPersonaAdicional.setText(QCoreApplication.translate("VentanaModificar", u"Precio persona adicional", None))
        self.label_titulo.setText(QCoreApplication.translate("VentanaModificar", u"Modificar Categorias ", None))
        ___qtablewidgetitem = self.tableCategorias.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaModificar", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableCategorias.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaModificar", u"Capacidad", None));
        ___qtablewidgetitem2 = self.tableCategorias.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaModificar", u"Tipo Entrada", None));
        ___qtablewidgetitem3 = self.tableCategorias.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaModificar", u"Precio base", None));
        ___qtablewidgetitem4 = self.tableCategorias.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaModificar", u"Hora adicional", None));
        ___qtablewidgetitem5 = self.tableCategorias.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VentanaModificar", u"Persona adicional", None));
        self.label.setText(QCoreApplication.translate("VentanaModificar", u"Ingrese los campos que desea cambiar ", None))
        self.pbutton_limpiar.setText(QCoreApplication.translate("VentanaModificar", u"Limpiar", None))
        self.pbutton_modificar.setText(QCoreApplication.translate("VentanaModificar", u"Modificar", None))
        self.pbutton_refrescar.setText(QCoreApplication.translate("VentanaModificar", u"Refrescar", None))
        self.pbutton_volver.setText(QCoreApplication.translate("VentanaModificar", u"Volver", None))
        self.comboBox_categorias.setCurrentText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModificarCategorias), QCoreApplication.translate("VentanaModificar", u"ModificarCategorias", None))
        self.label_titulo_2.setText(QCoreApplication.translate("VentanaModificar", u"Modificar Habitaciones", None))
        ___qtablewidgetitem6 = self.tableHabitaciones.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VentanaModificar", u"Numero", None));
        ___qtablewidgetitem7 = self.tableHabitaciones.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VentanaModificar", u"Categoria", None));
        ___qtablewidgetitem8 = self.tableHabitaciones.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VentanaModificar", u"Estado", None));
        ___qtablewidgetitem9 = self.tableHabitaciones.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VentanaModificar", u"Jacuzzi", None));
        ___qtablewidgetitem10 = self.tableHabitaciones.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VentanaModificar", u"Sauna", None));
        ___qtablewidgetitem11 = self.tableHabitaciones.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("VentanaModificar", u"Turco ", None));
        ___qtablewidgetitem12 = self.tableHabitaciones.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("VentanaModificar", u"Otros", None));
        self.label_2.setText(QCoreApplication.translate("VentanaModificar", u"Ingrese los campos que desea cambiar ", None))
        self.pbutton_volver_mh.setText(QCoreApplication.translate("VentanaModificar", u"Volver", None))
        self.comboBox_turco.setCurrentText("")
        self.comboBox_sauna.setCurrentText("")
        self.label_tipoEntrada_2.setText(QCoreApplication.translate("VentanaModificar", u"Sauna", None))
        self.label_capacidadHabitacion_2.setText(QCoreApplication.translate("VentanaModificar", u"Jacuzzi", None))
        self.label_tipoHabitacion_2.setText(QCoreApplication.translate("VentanaModificar", u"Categoria", None))
        self.label_precioHoraAdicional_2.setText(QCoreApplication.translate("VentanaModificar", u"Otros", None))
        self.comboBox_jacuzzi.setCurrentText("")
        self.label_estadoHabitacion_2.setText(QCoreApplication.translate("VentanaModificar", u"Turco", None))
        self.comboBox_categoriasMH.setCurrentText("")
        self.pbutton_limpiar_mh.setText(QCoreApplication.translate("VentanaModificar", u"Limpiar", None))
        self.comboBox_numeroHabitacion.setCurrentText("")
        self.pbutton_refrescar_2.setText(QCoreApplication.translate("VentanaModificar", u"Refrescar", None))
        self.pbutton_modificar_mh.setText(QCoreApplication.translate("VentanaModificar", u"Modificar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModificarHabitaciones), QCoreApplication.translate("VentanaModificar", u"ModificarHabitaciones", None))
    # retranslateUi

