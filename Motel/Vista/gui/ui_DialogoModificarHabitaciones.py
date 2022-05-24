# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogoModificarHabitacioneshBVmin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogoModificarHabitaciones(object):
    def setupUi(self, DialogoModificarHabitaciones):
        if not DialogoModificarHabitaciones.objectName():
            DialogoModificarHabitaciones.setObjectName(u"DialogoModificarHabitaciones")
        DialogoModificarHabitaciones.resize(625, 507)
        DialogoModificarHabitaciones.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.horizontalLayout = QHBoxLayout(DialogoModificarHabitaciones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(DialogoModificarHabitaciones)
        self.tabWidget.setObjectName(u"tabWidget")
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

        self.lineedit_capacidadHabitacion = QLineEdit(self.frame_opciones)
        self.lineedit_capacidadHabitacion.setObjectName(u"lineedit_capacidadHabitacion")

        self.gridLayout.addWidget(self.lineedit_capacidadHabitacion, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lineedit_categoria = QLineEdit(self.frame_opciones)
        self.lineedit_categoria.setObjectName(u"lineedit_categoria")

        self.gridLayout.addWidget(self.lineedit_categoria, 0, 1, 1, 1)

        self.lineedit_estadoHabitacion = QLineEdit(self.frame_opciones)
        self.lineedit_estadoHabitacion.setObjectName(u"lineedit_estadoHabitacion")

        self.gridLayout.addWidget(self.lineedit_estadoHabitacion, 1, 4, 1, 1)

        self.label_tipoHabitacion = QLabel(self.frame_opciones)
        self.label_tipoHabitacion.setObjectName(u"label_tipoHabitacion")
        self.label_tipoHabitacion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_tipoHabitacion, 0, 0, 1, 1)

        self.label_tipoEntrada_2 = QLabel(self.frame_opciones)
        self.label_tipoEntrada_2.setObjectName(u"label_tipoEntrada_2")
        self.label_tipoEntrada_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_tipoEntrada_2, 2, 0, 1, 1)

        self.lineedit_tipoEntrada_2 = QLineEdit(self.frame_opciones)
        self.lineedit_tipoEntrada_2.setObjectName(u"lineedit_tipoEntrada_2")

        self.gridLayout.addWidget(self.lineedit_tipoEntrada_2, 2, 1, 1, 1)

        self.label_tipoEntrada_3 = QLabel(self.frame_opciones)
        self.label_tipoEntrada_3.setObjectName(u"label_tipoEntrada_3")
        self.label_tipoEntrada_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_tipoEntrada_3, 2, 3, 1, 1)

        self.lineedit_tipoEntrada_3 = QLineEdit(self.frame_opciones)
        self.lineedit_tipoEntrada_3.setObjectName(u"lineedit_tipoEntrada_3")

        self.gridLayout.addWidget(self.lineedit_tipoEntrada_3, 2, 4, 1, 1)

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
        self.lineedit_numeroHabitacion = QLineEdit(self.ModificarCategorias)
        self.lineedit_numeroHabitacion.setObjectName(u"lineedit_numeroHabitacion")
        self.lineedit_numeroHabitacion.setGeometry(QRect(20, 250, 113, 20))
        self.lineedit_numeroHabitacion.setStyleSheet(u"background-color: None;\n"
"border: 2px solid;\n"
"border-color: rgb(0, 0, 0);")
        self.buttonBox = QDialogButtonBox(self.ModificarCategorias)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 430, 301, 32))
        self.buttonBox.setStyleSheet(u"background-color: None;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tableHabitaciones = QTableWidget(self.ModificarCategorias)
        if (self.tableHabitaciones.columnCount() < 4):
            self.tableHabitaciones.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableHabitaciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableHabitaciones.setObjectName(u"tableHabitaciones")
        self.tableHabitaciones.setGeometry(QRect(80, 40, 451, 201))
        self.tableHabitaciones.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.ModificarCategorias)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 270, 251, 51))
        self.label.setStyleSheet(u"background-color: None;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"color:rgb(130, 130, 130)")
        self.label.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.ModificarCategorias, "")
        self.ModificarHabitaciones = QWidget()
        self.ModificarHabitaciones.setObjectName(u"ModificarHabitaciones")
        self.tabWidget.addTab(self.ModificarHabitaciones, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(DialogoModificarHabitaciones)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogoModificarHabitaciones)
    # setupUi

    def retranslateUi(self, DialogoModificarHabitaciones):
        DialogoModificarHabitaciones.setWindowTitle(QCoreApplication.translate("DialogoModificarHabitaciones", u"Modificar Habitaciones", None))
        self.label_estadoHabitacion.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Precio Base", None))
        self.label_capacidadHabitacion.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Capacidad ", None))
        self.label_tipoEntrada.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Tipo Entrada ", None))
        self.label_tipoHabitacion.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Nombre", None))
        self.label_tipoEntrada_2.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Tipo Entrada ", None))
        self.label_tipoEntrada_3.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Tipo Entrada ", None))
        self.label_titulo.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Modificar Categorias ", None))
        self.lineedit_numeroHabitacion.setPlaceholderText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Nombre Categoria", None))
        ___qtablewidgetitem = self.tableHabitaciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Numero", None));
        ___qtablewidgetitem1 = self.tableHabitaciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Categoria", None));
        ___qtablewidgetitem2 = self.tableHabitaciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Capacidad", None));
        ___qtablewidgetitem3 = self.tableHabitaciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Precio", None));
        self.label.setText(QCoreApplication.translate("DialogoModificarHabitaciones", u"Ingrese los campos que desea cambiar ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModificarCategorias), QCoreApplication.translate("DialogoModificarHabitaciones", u"ModificarCategorias", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ModificarHabitaciones), QCoreApplication.translate("DialogoModificarHabitaciones", u"ModificarHabitaciones", None))
    # retranslateUi

