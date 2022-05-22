# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogoCrearUsuarioanWFhO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogoCrearUsuario(object):
    def setupUi(self, DialogoCrearUsuario):
        if not DialogoCrearUsuario.objectName():
            DialogoCrearUsuario.setObjectName(u"DialogoCrearUsuario")
        DialogoCrearUsuario.resize(542, 286)
        DialogoCrearUsuario.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.buttonBox = QDialogButtonBox(DialogoCrearUsuario)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(230, 240, 301, 32))
        self.buttonBox.setStyleSheet(u"background-color: None;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_titulo = QLabel(DialogoCrearUsuario)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(50, 10, 421, 31))
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
        self.frame = QFrame(DialogoCrearUsuario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 39, 521, 201))
        self.frame.setStyleSheet(u"background-color: None;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.lineedit_cedula = QLineEdit(self.frame)
        self.lineedit_cedula.setObjectName(u"lineedit_cedula")

        self.gridLayout.addWidget(self.lineedit_cedula, 0, 1, 1, 1)

        self.label_nombres = QLabel(self.frame)
        self.label_nombres.setObjectName(u"label_nombres")
        self.label_nombres.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_nombres, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lineedit_contrasenia = QLineEdit(self.frame)
        self.lineedit_contrasenia.setObjectName(u"lineedit_contrasenia")

        self.gridLayout.addWidget(self.lineedit_contrasenia, 1, 4, 1, 1)

        self.label_cedula = QLabel(self.frame)
        self.label_cedula.setObjectName(u"label_cedula")
        self.label_cedula.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_cedula, 0, 0, 1, 1)

        self.label_contrasenia = QLabel(self.frame)
        self.label_contrasenia.setObjectName(u"label_contrasenia")
        self.label_contrasenia.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout.addWidget(self.label_contrasenia, 1, 3, 1, 1)

        self.lineedit_nombres = QLineEdit(self.frame)
        self.lineedit_nombres.setObjectName(u"lineedit_nombres")

        self.gridLayout.addWidget(self.lineedit_nombres, 0, 4, 1, 1)

        self.label_apellidos = QLabel(self.frame)
        self.label_apellidos.setObjectName(u"label_apellidos")
        self.label_apellidos.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_apellidos, 1, 0, 1, 1)

        self.lineedit_apellidos = QLineEdit(self.frame)
        self.lineedit_apellidos.setObjectName(u"lineedit_apellidos")

        self.gridLayout.addWidget(self.lineedit_apellidos, 1, 1, 1, 1)


        self.retranslateUi(DialogoCrearUsuario)
        self.buttonBox.accepted.connect(DialogoCrearUsuario.accept)
        self.buttonBox.rejected.connect(DialogoCrearUsuario.reject)

        QMetaObject.connectSlotsByName(DialogoCrearUsuario)
    # setupUi

    def retranslateUi(self, DialogoCrearUsuario):
        DialogoCrearUsuario.setWindowTitle(QCoreApplication.translate("DialogoCrearUsuario", u"Crear Usuario", None))
        self.label_titulo.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Crear Usuario", None))
        self.lineedit_cedula.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"Obligatorio*", None))
        self.label_nombres.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Nombres      ", None))
        self.lineedit_contrasenia.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"Obligatorio*", None))
        self.label_cedula.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Cedula      ", None))
        self.label_contrasenia.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Contrase\u00f1a", None))
        self.lineedit_nombres.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"Obligatorio*", None))
        self.label_apellidos.setText(QCoreApplication.translate("DialogoCrearUsuario", u"Apellidos", None))
        self.lineedit_apellidos.setPlaceholderText(QCoreApplication.translate("DialogoCrearUsuario", u"Obligatorio*", None))
    # retranslateUi

