# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaConfiguraciondFPxWH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaConfiguracion(object):
    def setupUi(self, VentanaConfiguracion):
        if not VentanaConfiguracion.objectName():
            VentanaConfiguracion.setObjectName(u"VentanaConfiguracion")
        VentanaConfiguracion.resize(624, 359)
        VentanaConfiguracion.setMinimumSize(QSize(624, 359))
        VentanaConfiguracion.setMaximumSize(QSize(624, 359))
        VentanaConfiguracion.setLayoutDirection(Qt.RightToLeft)
        VentanaConfiguracion.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:1, angle:195, stop:0.676136 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.horizontalLayout = QHBoxLayout(VentanaConfiguracion)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(VentanaConfiguracion)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(624, 359))
        self.frame_3.setMaximumSize(QSize(624, 359))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 624, 359))
        self.tabWidget.setMinimumSize(QSize(624, 359))
        self.tabWidget.setMaximumSize(QSize(624, 359))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.Definir_categorias = QWidget()
        self.Definir_categorias.setObjectName(u"Definir_categorias")
        self.verticalLayout = QVBoxLayout(self.Definir_categorias)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.Definir_categorias)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:None;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_precioAdiconal = QLabel(self.frame)
        self.label_precioAdiconal.setObjectName(u"label_precioAdiconal")
        self.label_precioAdiconal.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.label_precioAdiconal, 2, 0, 1, 1)

        self.label_capacidad = QLabel(self.frame)
        self.label_capacidad.setObjectName(u"label_capacidad")
        self.label_capacidad.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.label_capacidad, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.label_precioPersona = QLabel(self.frame)
        self.label_precioPersona.setObjectName(u"label_precioPersona")
        self.label_precioPersona.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.label_precioPersona, 2, 4, 1, 1)

        self.lineedit_nombreCategoria = QLineEdit(self.frame)
        self.lineedit_nombreCategoria.setObjectName(u"lineedit_nombreCategoria")
        self.lineedit_nombreCategoria.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_nombreCategoria, 0, 1, 1, 2)

        self.label_tipoEntrada = QLabel(self.frame)
        self.label_tipoEntrada.setObjectName(u"label_tipoEntrada")
        self.label_tipoEntrada.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.label_tipoEntrada, 1, 0, 1, 1)

        self.lineedit_capacidad = QLineEdit(self.frame)
        self.lineedit_capacidad.setObjectName(u"lineedit_capacidad")
        self.lineedit_capacidad.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_capacidad, 0, 5, 1, 1)

        self.lineedit_precioBase = QLineEdit(self.frame)
        self.lineedit_precioBase.setObjectName(u"lineedit_precioBase")
        self.lineedit_precioBase.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_precioBase, 1, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.label_nombreCategoria = QLabel(self.frame)
        self.label_nombreCategoria.setObjectName(u"label_nombreCategoria")
        self.label_nombreCategoria.setStyleSheet(u"background-color: None;")
        self.label_nombreCategoria.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.label_nombreCategoria, 0, 0, 1, 1)

        self.label_precioBase = QLabel(self.frame)
        self.label_precioBase.setObjectName(u"label_precioBase")
        self.label_precioBase.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.label_precioBase, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.lineedit_precioAdicional = QLineEdit(self.frame)
        self.lineedit_precioAdicional.setObjectName(u"lineedit_precioAdicional")
        self.lineedit_precioAdicional.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_precioAdicional, 2, 1, 1, 2)

        self.lineedit_tipoEntrada = QLineEdit(self.frame)
        self.lineedit_tipoEntrada.setObjectName(u"lineedit_tipoEntrada")
        self.lineedit_tipoEntrada.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_tipoEntrada, 1, 1, 1, 2)

        self.lineedit_personaAdicional = QLineEdit(self.frame)
        self.lineedit_personaAdicional.setObjectName(u"lineedit_personaAdicional")
        self.lineedit_personaAdicional.setStyleSheet(u"background-color: None;")

        self.gridLayout.addWidget(self.lineedit_personaAdicional, 2, 5, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.Definir_categorias)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color:None;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_volver_DC = QPushButton(self.frame_2)
        self.pushButton_volver_DC.setObjectName(u"pushButton_volver_DC")
        self.pushButton_volver_DC.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_volver_DC)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButton_aceptar = QPushButton(self.frame_2)
        self.pushButton_aceptar.setObjectName(u"pushButton_aceptar")
        self.pushButton_aceptar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_aceptar)

        self.pushButton_limpiar_categoria = QPushButton(self.frame_2)
        self.pushButton_limpiar_categoria.setObjectName(u"pushButton_limpiar_categoria")
        self.pushButton_limpiar_categoria.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_limpiar_categoria)


        self.verticalLayout.addWidget(self.frame_2)

        self.tabWidget.addTab(self.Definir_categorias, "")
        self.Agregar_habitacion = QWidget()
        self.Agregar_habitacion.setObjectName(u"Agregar_habitacion")
        self.verticalLayout_2 = QVBoxLayout(self.Agregar_habitacion)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_titulo = QLabel(self.Agregar_habitacion)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setMinimumSize(QSize(624, 31))
        self.label_titulo.setMaximumSize(QSize(624, 31))
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

        self.verticalLayout_2.addWidget(self.label_titulo)

        self.frame_4 = QFrame(self.Agregar_habitacion)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: None;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_turcoAgregarH = QLabel(self.frame_4)
        self.label_turcoAgregarH.setObjectName(u"label_turcoAgregarH")

        self.gridLayout_2.addWidget(self.label_turcoAgregarH, 4, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(49, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 4, 3, 1, 1)

        self.label_jacuzziAgregarH = QLabel(self.frame_4)
        self.label_jacuzziAgregarH.setObjectName(u"label_jacuzziAgregarH")
        self.label_jacuzziAgregarH.setStyleSheet(u"background-color: None;")

        self.gridLayout_2.addWidget(self.label_jacuzziAgregarH, 3, 0, 1, 2)

        self.comboBox_jacuzzi = QComboBox(self.frame_4)
        self.comboBox_jacuzzi.setObjectName(u"comboBox_jacuzzi")

        self.gridLayout_2.addWidget(self.comboBox_jacuzzi, 3, 2, 1, 1)

        self.label_numHabitacion = QLabel(self.frame_4)
        self.label_numHabitacion.setObjectName(u"label_numHabitacion")
        self.label_numHabitacion.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_numHabitacion, 0, 0, 1, 2)

        self.comboBox_turco = QComboBox(self.frame_4)
        self.comboBox_turco.setObjectName(u"comboBox_turco")

        self.gridLayout_2.addWidget(self.comboBox_turco, 4, 2, 1, 1)

        self.comboBox_estado = QComboBox(self.frame_4)
        self.comboBox_estado.setObjectName(u"comboBox_estado")

        self.gridLayout_2.addWidget(self.comboBox_estado, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(49, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 3, 3, 1, 1)

        self.label_serviciosAdicionales_2 = QLabel(self.frame_4)
        self.label_serviciosAdicionales_2.setObjectName(u"label_serviciosAdicionales_2")
        self.label_serviciosAdicionales_2.setMinimumSize(QSize(0, 20))
        self.label_serviciosAdicionales_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_serviciosAdicionales_2, 2, 0, 1, 2)

        self.comboBox_categorias = QComboBox(self.frame_4)
        self.comboBox_categorias.setObjectName(u"comboBox_categorias")
        self.comboBox_categorias.setMinimumSize(QSize(133, 20))
        self.comboBox_categorias.setMaximumSize(QSize(133, 20))

        self.gridLayout_2.addWidget(self.comboBox_categorias, 0, 8, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 5, 1, 2)

        self.label_estado = QLabel(self.frame_4)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_2.addWidget(self.label_estado, 1, 0, 1, 1)

        self.label_categoria = QLabel(self.frame_4)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_categoria, 0, 7, 1, 1)

        self.label_saunaAgregarH = QLabel(self.frame_4)
        self.label_saunaAgregarH.setObjectName(u"label_saunaAgregarH")

        self.gridLayout_2.addWidget(self.label_saunaAgregarH, 3, 7, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 7, 1, 1)

        self.comboBox_sauna = QComboBox(self.frame_4)
        self.comboBox_sauna.setObjectName(u"comboBox_sauna")

        self.gridLayout_2.addWidget(self.comboBox_sauna, 3, 8, 1, 1)

        self.lineedit_otros = QLineEdit(self.frame_4)
        self.lineedit_otros.setObjectName(u"lineedit_otros")

        self.gridLayout_2.addWidget(self.lineedit_otros, 4, 8, 1, 1)

        self.lineedit_numHabitacion = QLineEdit(self.frame_4)
        self.lineedit_numHabitacion.setObjectName(u"lineedit_numHabitacion")

        self.gridLayout_2.addWidget(self.lineedit_numHabitacion, 0, 2, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Agregar_habitacion)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(600, 50))
        self.frame_5.setMaximumSize(QSize(600, 50))
        self.frame_5.setStyleSheet(u"background-color: None;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_volver_AH = QPushButton(self.frame_5)
        self.pushButton_volver_AH.setObjectName(u"pushButton_volver_AH")
        self.pushButton_volver_AH.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.pushButton_volver_AH)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.pushButton_aceptarHab = QPushButton(self.frame_5)
        self.pushButton_aceptarHab.setObjectName(u"pushButton_aceptarHab")
        self.pushButton_aceptarHab.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.pushButton_aceptarHab)

        self.pushButton_limpiarHab = QPushButton(self.frame_5)
        self.pushButton_limpiarHab.setObjectName(u"pushButton_limpiarHab")
        self.pushButton_limpiarHab.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.pushButton_limpiarHab)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.tabWidget.addTab(self.Agregar_habitacion, "")

        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(VentanaConfiguracion)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VentanaConfiguracion)
    # setupUi

    def retranslateUi(self, VentanaConfiguracion):
        VentanaConfiguracion.setWindowTitle(QCoreApplication.translate("VentanaConfiguracion", u"Configuracion", None))
        self.label_precioAdiconal.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Precio Hora Adicional</span></p></body></html>", None))
        self.label_capacidad.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Capacidad</span></p></body></html>", None))
        self.label_precioPersona.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Precio Persona Adicional</span></p></body></html>", None))
        self.label_tipoEntrada.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Tipo Entrada</span></p></body></html>", None))
        self.label_nombreCategoria.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Nombre Categoria </span></p></body></html>", None))
        self.label_precioBase.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Precio Base</span></p></body></html>", None))
        self.pushButton_volver_DC.setText(QCoreApplication.translate("VentanaConfiguracion", u"Volver", None))
        self.pushButton_aceptar.setText(QCoreApplication.translate("VentanaConfiguracion", u"Aceptar ", None))
        self.pushButton_limpiar_categoria.setText(QCoreApplication.translate("VentanaConfiguracion", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Definir_categorias), QCoreApplication.translate("VentanaConfiguracion", u"Definir categorias, precios y servicios", None))
        self.label_titulo.setText(QCoreApplication.translate("VentanaConfiguracion", u"Agregar Habitacion ", None))
        self.label_turcoAgregarH.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">\u00bfTurco?</span></p></body></html>", None))
        self.label_jacuzziAgregarH.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">\u00bfJacuzzi?</span></p></body></html>", None))
        self.label_numHabitacion.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Numero Habitacion    </span></p></body></html>", None))
        self.label_serviciosAdicionales_2.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Servicios adicionales:</span></p></body></html>", None))
        self.label_estado.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Estado</span></p></body></html>", None))
        self.label_categoria.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Categoria   </span></p></body></html>", None))
        self.label_saunaAgregarH.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">\u00bfSauna?</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Otros</span></p></body></html>", None))
        self.lineedit_numHabitacion.setPlaceholderText(QCoreApplication.translate("VentanaConfiguracion", u"Obligatorio*", None))
        self.pushButton_volver_AH.setText(QCoreApplication.translate("VentanaConfiguracion", u"Volver", None))
        self.pushButton_aceptarHab.setText(QCoreApplication.translate("VentanaConfiguracion", u"Aceptar", None))
        self.pushButton_limpiarHab.setText(QCoreApplication.translate("VentanaConfiguracion", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Agregar_habitacion), QCoreApplication.translate("VentanaConfiguracion", u"Agregar habitacion", None))
    # retranslateUi

