# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogoCrearHabitacionesGDSmFw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogoCrearHabitaciones(object):
    def setupUi(self, DialogoCrearHabitaciones):
        if not DialogoCrearHabitaciones.objectName():
            DialogoCrearHabitaciones.setObjectName(u"DialogoCrearHabitaciones")
        DialogoCrearHabitaciones.resize(608, 356)
        DialogoCrearHabitaciones.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.buttonBox = QDialogButtonBox(DialogoCrearHabitaciones)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(300, 320, 301, 32))
        self.buttonBox.setStyleSheet(u"background-color: None;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_titulo = QLabel(DialogoCrearHabitaciones)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(93, 13, 421, 31))
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
        self.frame = QFrame(DialogoCrearHabitaciones)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 60, 521, 201))
        self.frame.setStyleSheet(u"background-color: None;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineedit_tipoEntrada = QLineEdit(self.frame)
        self.lineedit_tipoEntrada.setObjectName(u"lineedit_tipoEntrada")

        self.gridLayout.addWidget(self.lineedit_tipoEntrada, 1, 4, 1, 1)

        self.label_numHabitacion = QLabel(self.frame)
        self.label_numHabitacion.setObjectName(u"label_numHabitacion")
        self.label_numHabitacion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_numHabitacion, 0, 0, 1, 1)

        self.label_tipoEntrada = QLabel(self.frame)
        self.label_tipoEntrada.setObjectName(u"label_tipoEntrada")
        self.label_tipoEntrada.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.label_tipoEntrada, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.lineedit_capacidad = QLineEdit(self.frame)
        self.lineedit_capacidad.setObjectName(u"lineedit_capacidad")

        self.gridLayout.addWidget(self.lineedit_capacidad, 1, 1, 1, 1)

        self.lineedit_numHabitacion = QLineEdit(self.frame)
        self.lineedit_numHabitacion.setObjectName(u"lineedit_numHabitacion")

        self.gridLayout.addWidget(self.lineedit_numHabitacion, 0, 1, 1, 1)

        self.label_tipo = QLabel(self.frame)
        self.label_tipo.setObjectName(u"label_tipo")
        self.label_tipo.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_tipo, 0, 3, 1, 1)

        self.label_capacidad = QLabel(self.frame)
        self.label_capacidad.setObjectName(u"label_capacidad")
        self.label_capacidad.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_capacidad, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lineedit_tipo = QLineEdit(self.frame)
        self.lineedit_tipo.setObjectName(u"lineedit_tipo")

        self.gridLayout.addWidget(self.lineedit_tipo, 0, 4, 1, 1)

        self.label_estado = QLabel(self.frame)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.label_estado, 2, 0, 1, 1)

        self.lineedit_estado = QLineEdit(self.frame)
        self.lineedit_estado.setObjectName(u"lineedit_estado")

        self.gridLayout.addWidget(self.lineedit_estado, 2, 1, 1, 1)


        self.retranslateUi(DialogoCrearHabitaciones)
        self.buttonBox.accepted.connect(DialogoCrearHabitaciones.accept)
        self.buttonBox.rejected.connect(DialogoCrearHabitaciones.reject)

        QMetaObject.connectSlotsByName(DialogoCrearHabitaciones)
    # setupUi

    def retranslateUi(self, DialogoCrearHabitaciones):
        DialogoCrearHabitaciones.setWindowTitle(QCoreApplication.translate("DialogoCrearHabitaciones", u"Agregar Habitaciones", None))
        self.label_titulo.setText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Agregar Habitacion ", None))
        self.lineedit_tipoEntrada.setPlaceholderText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Obligatorio*", None))
        self.label_numHabitacion.setText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Numero Habitacion     ", None))
        self.label_tipoEntrada.setText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Tipo Entrada", None))
        self.lineedit_capacidad.setPlaceholderText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Obligatorio*", None))
        self.lineedit_numHabitacion.setPlaceholderText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Obligatorio*", None))
        self.label_tipo.setText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Tipo Habitacion   ", None))
        self.label_capacidad.setText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Capacidad Habitacion", None))
        self.lineedit_tipo.setPlaceholderText(QCoreApplication.translate("DialogoCrearHabitaciones", u"Obligatorio*", None))
        self.label_estado.setText(QCoreApplication.translate("DialogoCrearHabitaciones", u" Estado Habitacion ", None))
        self.lineedit_estado.setPlaceholderText("")
    # retranslateUi

