# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipalhrCEki.ui'
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
        VentanaPrincipal.resize(596, 337)
        self.pushButton_salir = QPushButton(VentanaPrincipal)
        self.pushButton_salir.setObjectName(u"pushButton_salir")
        self.pushButton_salir.setGeometry(QRect(270, 230, 75, 44))
        self.pushButton_salir.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 87 24pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 170, 170);\n"
"	font: 87 24pt \"Arial\";\n"
"\n"
"}")
        self.label = QLabel(VentanaPrincipal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 0, 497, 115))
        self.label.setStyleSheet(u"font: 75 28pt \\\"Script MT Bold\\\";\\n")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.retranslateUi(VentanaPrincipal)
        self.pushButton_salir.clicked.connect(VentanaPrincipal.close)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Menu Principal", None))
        self.pushButton_salir.setText(QCoreApplication.translate("VentanaPrincipal", u"Salir", None))
        self.label.setText(QCoreApplication.translate("VentanaPrincipal", u"<html><head/><body><p><span style=\" font-size:72pt; font-weight:600;\">cooming soon</span></p></body></html>", None))
    # retranslateUi

