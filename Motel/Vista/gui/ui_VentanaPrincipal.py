# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPrincipalqpWxCP.ui'
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
        VentanaPrincipal.setMaximumSize(QSize(624, 359))
        VentanaPrincipal.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));")
        self.frame = QFrame(VentanaPrincipal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 10, 461, 81))
        self.frame.setToolTipDuration(-1)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pbutton_entradas = QPushButton(self.frame)
        self.pbutton_entradas.setObjectName(u"pbutton_entradas")
        self.pbutton_entradas.setMinimumSize(QSize(121, 61))
        self.pbutton_entradas.setMaximumSize(QSize(121, 61))
        self.pbutton_entradas.setStyleSheet(u"border-radius: 10px;\n"
"\n"
"background-color: rgb(255,255,255);")
        icon = QIcon()
        icon.addFile(u"imgs/entradas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbutton_entradas.setIcon(icon)
        self.pbutton_entradas.setIconSize(QSize(112, 86))

        self.horizontalLayout.addWidget(self.pbutton_entradas)

        self.pbutton_configurar = QPushButton(self.frame)
        self.pbutton_configurar.setObjectName(u"pbutton_configurar")
        self.pbutton_configurar.setMinimumSize(QSize(121, 61))
        self.pbutton_configurar.setMaximumSize(QSize(121, 61))
        self.pbutton_configurar.setStyleSheet(u"border-radius: 10px;\n"
"\n"
"background-color: rgb(255,255,255);\n"
"background-image: u\"imgs/configurar.png\"")
        icon1 = QIcon()
        icon1.addFile(u"imgs/configurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbutton_configurar.setIcon(icon1)
        self.pbutton_configurar.setIconSize(QSize(112, 86))

        self.horizontalLayout.addWidget(self.pbutton_configurar)

        self.pbutton_reservas = QPushButton(self.frame)
        self.pbutton_reservas.setObjectName(u"pbutton_reservas")
        self.pbutton_reservas.setMinimumSize(QSize(121, 61))
        self.pbutton_reservas.setMaximumSize(QSize(121, 61))
        self.pbutton_reservas.setStyleSheet(u"border-radius: 10px;\n"
"border: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(0, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u"imgs/reservas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbutton_reservas.setIcon(icon2)
        self.pbutton_reservas.setIconSize(QSize(112, 86))

        self.horizontalLayout.addWidget(self.pbutton_reservas)

        self.frame_2 = QFrame(VentanaPrincipal)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 90, 101, 231))
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0%);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Menu Principal", None))
    # retranslateUi

