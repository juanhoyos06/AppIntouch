# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaDeInicioSnyJey.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaDeInicio(object):
    def setupUi(self, VentanaDeInicio):
        if not VentanaDeInicio.objectName():
            VentanaDeInicio.setObjectName(u"VentanaDeInicio")
        VentanaDeInicio.resize(333, 419)
        VentanaDeInicio.setMaximumSize(QSize(333, 419))
        VentanaDeInicio.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(VentanaDeInicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 351, 421))
        self.frame.setMaximumSize(QSize(351, 421))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.491633, y1:0.125, x2:0.499, y2:0.988636, stop:0.193634 rgba(13, 0, 0, 255), stop:1 rgba(255, 0, 15, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.492, y1:0.0572727, x2:0.499, y2:0.988636, stop:0.471591 rgba(0, 0, 0, 255), stop:1 rgba(255, 0, 15, 255));\n"
"\n"
"border: 1px solid #000")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_usuario = QLabel(self.frame)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setEnabled(False)
        self.label_usuario.setGeometry(QRect(130, 160, 71, 21))
        self.label_usuario.setMaximumSize(QSize(71, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_usuario.setFont(font)
        self.label_usuario.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"selection-color: rgb(255, 255, 255);")
        self.label_contrasenia = QLabel(self.frame)
        self.label_contrasenia.setObjectName(u"label_contrasenia")
        self.label_contrasenia.setEnabled(False)
        self.label_contrasenia.setGeometry(QRect(120, 250, 101, 21))
        self.label_contrasenia.setMaximumSize(QSize(101, 21))
        self.label_contrasenia.setFont(font)
        self.label_contrasenia.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"border-color: rgba(0, 0, 0,0%);")
        self.pbutton_salir = QPushButton(self.frame)
        self.pbutton_salir.setObjectName(u"pbutton_salir")
        self.pbutton_salir.setEnabled(True)
        self.pbutton_salir.setGeometry(QRect(90, 340, 75, 23))
        self.pbutton_salir.setStyleSheet(u"QPushButton{\n"
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
        self.pbutton_ingresar = QPushButton(self.frame)
        self.pbutton_ingresar.setObjectName(u"pbutton_ingresar")
        self.pbutton_ingresar.setGeometry(QRect(170, 340, 81, 23))
        self.pbutton_ingresar.setStyleSheet(u"QPushButton{\n"
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
        self.lineedit_usuario = QLineEdit(self.frame)
        self.lineedit_usuario.setObjectName(u"lineedit_usuario")
        self.lineedit_usuario.setGeometry(QRect(90, 190, 161, 31))
        self.lineedit_usuario.setMaximumSize(QSize(161, 31))
        self.lineedit_usuario.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.lineedit_usuario.setAlignment(Qt.AlignCenter)
        self.lineedit_contrasenia = QLineEdit(self.frame)
        self.lineedit_contrasenia.setObjectName(u"lineedit_contrasenia")
        self.lineedit_contrasenia.setGeometry(QRect(90, 280, 161, 31))
        self.lineedit_contrasenia.setMaximumSize(QSize(161, 31))
        self.lineedit_contrasenia.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.lineedit_contrasenia.setEchoMode(QLineEdit.Password)
        self.lineedit_contrasenia.setAlignment(Qt.AlignCenter)
        self.label_InTouch = QLabel(self.frame)
        self.label_InTouch.setObjectName(u"label_InTouch")
        self.label_InTouch.setGeometry(QRect(50, 30, 221, 91))
        self.label_InTouch.setMaximumSize(QSize(221, 151))
        self.label_InTouch.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"font: 75 28pt \"Script MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_InTouch.setScaledContents(True)
        self.label_Software = QLabel(self.frame)
        self.label_Software.setObjectName(u"label_Software")
        self.label_Software.setGeometry(QRect(180, 100, 71, 20))
        self.label_Software.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);\n"
"border: None;")
        VentanaDeInicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaDeInicio)
        self.pbutton_salir.clicked.connect(VentanaDeInicio.close)

        QMetaObject.connectSlotsByName(VentanaDeInicio)
    # setupUi

    def retranslateUi(self, VentanaDeInicio):
        VentanaDeInicio.setWindowTitle(QCoreApplication.translate("VentanaDeInicio", u"Login-In Touch", None))
        self.label_usuario.setText(QCoreApplication.translate("VentanaDeInicio", u"<html><head/><body><p><span style=\" color:#ffffff;\">Usuario</span></p></body></html>", None))
        self.label_contrasenia.setText(QCoreApplication.translate("VentanaDeInicio", u"<html><head/><body><p><span style=\" color:#ffffff;\">Contrase\u00f1a</span></p></body></html>", None))
        self.pbutton_salir.setText(QCoreApplication.translate("VentanaDeInicio", u"Salir", None))
        self.pbutton_ingresar.setText(QCoreApplication.translate("VentanaDeInicio", u"Ingresar", None))
        self.lineedit_usuario.setPlaceholderText(QCoreApplication.translate("VentanaDeInicio", u"Obligatorio*", None))
        self.lineedit_contrasenia.setPlaceholderText(QCoreApplication.translate("VentanaDeInicio", u"Obligatorio*", None))
        self.label_InTouch.setText(QCoreApplication.translate("VentanaDeInicio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">In Touch</span></p></body></html>", None))
        self.label_Software.setText(QCoreApplication.translate("VentanaDeInicio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Software</span></p></body></html>", None))
    # retranslateUi

