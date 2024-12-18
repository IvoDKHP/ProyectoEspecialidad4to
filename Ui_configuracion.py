# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuracion.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1268, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Fondo = QtWidgets.QFrame(self.centralwidget)
        self.Fondo.setStyleSheet("QFrame {\n"
"    background-image: url(../Graficos/2.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-color: transparent;\n"
"}")
        self.Fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Fondo.setObjectName("Fondo")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Fondo)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.Volver_frame = QtWidgets.QFrame(self.Fondo)
        self.Volver_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Volver_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Volver_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Volver_frame.setObjectName("Volver_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Volver_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Volver = QtWidgets.QFrame(self.Volver_frame)
        self.Volver.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Volver.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Volver.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Volver.setObjectName("Volver")
        self.volver_boton = QtWidgets.QPushButton(self.Volver)
        self.volver_boton.setGeometry(QtCore.QRect(0, 3, 280, 40))
        self.volver_boton.setStyleSheet("QPushButton {\n"
"    background-color: blue;  /* Cambia \'green\' al color que prefieras */\n"
"    color: white;  /* Cambia \'white\' al color del texto que prefieras */\n"
"border rad\n"
"}\n"
"QPushButton { border-radius: 15px; /* Ajusta el valor para hacer el botón más o menos redondeado / background-color: #3498db; / Color de fondo del botón / color: white; / Color del texto del botón / border: 12px solid #2980b9; / Borde del botón */ }")
        self.volver_boton.setObjectName("volver_boton")
        self.horizontalLayout_2.addWidget(self.Volver)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 12)
        self.horizontalLayout_2.setStretch(1, 25)
        self.horizontalLayout_2.setStretch(2, 75)
        self.verticalLayout_10.addWidget(self.Volver_frame)
        self.Semana_frame = QtWidgets.QFrame(self.Fondo)
        self.Semana_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Semana_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Semana_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Semana_frame.setObjectName("Semana_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Semana_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.General_frame = QtWidgets.QFrame(self.Semana_frame)
        self.General_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.General_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.General_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.General_frame.setObjectName("General_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.General_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cartel_general = QtWidgets.QLabel(self.General_frame)
        self.cartel_general.setStyleSheet("")
        self.cartel_general.setObjectName("cartel_general")
        self.verticalLayout_2.addWidget(self.cartel_general)
        self.Horarios_general = QtWidgets.QFrame(self.General_frame)
        self.Horarios_general.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_general.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_general.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_general.setObjectName("Horarios_general")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Horarios_general)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lm_grl = QtWidgets.QSpinBox(self.Horarios_general)
        self.lm_grl.setStyleSheet("")
        self.lm_grl.setObjectName("lm_grl")
        self.verticalLayout.addWidget(self.lm_grl)
        self.grl_tm1 = QtWidgets.QTimeEdit(self.Horarios_general)
        self.grl_tm1.setStyleSheet("")
        self.grl_tm1.setObjectName("grl_tm1")
        self.verticalLayout.addWidget(self.grl_tm1)
        self.grl_tm2 = QtWidgets.QTimeEdit(self.Horarios_general)
        self.grl_tm2.setObjectName("grl_tm2")
        self.verticalLayout.addWidget(self.grl_tm2)
        self.grl_tm3 = QtWidgets.QTimeEdit(self.Horarios_general)
        self.grl_tm3.setObjectName("grl_tm3")
        self.verticalLayout.addWidget(self.grl_tm3)
        self.grl_tm4 = QtWidgets.QTimeEdit(self.Horarios_general)
        self.grl_tm4.setObjectName("grl_tm4")
        self.verticalLayout.addWidget(self.grl_tm4)
        self.grl_tm5 = QtWidgets.QTimeEdit(self.Horarios_general)
        self.grl_tm5.setObjectName("grl_tm5")
        self.verticalLayout.addWidget(self.grl_tm5)
        self.verticalLayout_2.addWidget(self.Horarios_general)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.General_frame)
        self.Lunes_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Lunes_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Lunes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Lunes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Lunes_frame.setObjectName("Lunes_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Lunes_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cartel_lunes = QtWidgets.QLabel(self.Lunes_frame)
        self.cartel_lunes.setObjectName("cartel_lunes")
        self.verticalLayout_3.addWidget(self.cartel_lunes)
        self.Horarios_lunes = QtWidgets.QFrame(self.Lunes_frame)
        self.Horarios_lunes.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_lunes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_lunes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_lunes.setObjectName("Horarios_lunes")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Horarios_lunes)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lm_lu = QtWidgets.QSpinBox(self.Horarios_lunes)
        self.lm_lu.setObjectName("lm_lu")
        self.verticalLayout_11.addWidget(self.lm_lu)
        self.lu_tm1 = QtWidgets.QTimeEdit(self.Horarios_lunes)
        self.lu_tm1.setObjectName("lu_tm1")
        self.verticalLayout_11.addWidget(self.lu_tm1)
        self.lu_tm2 = QtWidgets.QTimeEdit(self.Horarios_lunes)
        self.lu_tm2.setObjectName("lu_tm2")
        self.verticalLayout_11.addWidget(self.lu_tm2)
        self.lu_tm3 = QtWidgets.QTimeEdit(self.Horarios_lunes)
        self.lu_tm3.setObjectName("lu_tm3")
        self.verticalLayout_11.addWidget(self.lu_tm3)
        self.lu_tm4 = QtWidgets.QTimeEdit(self.Horarios_lunes)
        self.lu_tm4.setObjectName("lu_tm4")
        self.verticalLayout_11.addWidget(self.lu_tm4)
        self.lu_tm5 = QtWidgets.QTimeEdit(self.Horarios_lunes)
        self.lu_tm5.setObjectName("lu_tm5")
        self.verticalLayout_11.addWidget(self.lu_tm5)
        self.verticalLayout_3.addWidget(self.Horarios_lunes)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Lunes_frame)
        self.Martes_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Martes_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Martes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Martes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Martes_frame.setObjectName("Martes_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Martes_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cartel_martes = QtWidgets.QLabel(self.Martes_frame)
        self.cartel_martes.setObjectName("cartel_martes")
        self.verticalLayout_4.addWidget(self.cartel_martes)
        self.Horarios_martes = QtWidgets.QFrame(self.Martes_frame)
        self.Horarios_martes.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_martes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_martes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_martes.setObjectName("Horarios_martes")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Horarios_martes)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lm_mt = QtWidgets.QSpinBox(self.Horarios_martes)
        self.lm_mt.setObjectName("lm_mt")
        self.verticalLayout_12.addWidget(self.lm_mt)
        self.mt_tm1 = QtWidgets.QTimeEdit(self.Horarios_martes)
        self.mt_tm1.setObjectName("mt_tm1")
        self.verticalLayout_12.addWidget(self.mt_tm1)
        self.mt_tm2 = QtWidgets.QTimeEdit(self.Horarios_martes)
        self.mt_tm2.setObjectName("mt_tm2")
        self.verticalLayout_12.addWidget(self.mt_tm2)
        self.mt_tm3 = QtWidgets.QTimeEdit(self.Horarios_martes)
        self.mt_tm3.setObjectName("mt_tm3")
        self.verticalLayout_12.addWidget(self.mt_tm3)
        self.mt_tm4 = QtWidgets.QTimeEdit(self.Horarios_martes)
        self.mt_tm4.setObjectName("mt_tm4")
        self.verticalLayout_12.addWidget(self.mt_tm4)
        self.mt_tm5 = QtWidgets.QTimeEdit(self.Horarios_martes)
        self.mt_tm5.setObjectName("mt_tm5")
        self.verticalLayout_12.addWidget(self.mt_tm5)
        self.verticalLayout_4.addWidget(self.Horarios_martes)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Martes_frame)
        self.Miercoles_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Miercoles_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Miercoles_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Miercoles_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Miercoles_frame.setObjectName("Miercoles_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Miercoles_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cartel_miercoles = QtWidgets.QLabel(self.Miercoles_frame)
        self.cartel_miercoles.setObjectName("cartel_miercoles")
        self.verticalLayout_5.addWidget(self.cartel_miercoles)
        self.Horarios_miercoles = QtWidgets.QFrame(self.Miercoles_frame)
        self.Horarios_miercoles.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_miercoles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_miercoles.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_miercoles.setObjectName("Horarios_miercoles")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Horarios_miercoles)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lm_mc = QtWidgets.QSpinBox(self.Horarios_miercoles)
        self.lm_mc.setObjectName("lm_mc")
        self.verticalLayout_13.addWidget(self.lm_mc)
        self.mc_tm1 = QtWidgets.QTimeEdit(self.Horarios_miercoles)
        self.mc_tm1.setObjectName("mc_tm1")
        self.verticalLayout_13.addWidget(self.mc_tm1)
        self.mc_tm2 = QtWidgets.QTimeEdit(self.Horarios_miercoles)
        self.mc_tm2.setObjectName("mc_tm2")
        self.verticalLayout_13.addWidget(self.mc_tm2)
        self.mc_tm3 = QtWidgets.QTimeEdit(self.Horarios_miercoles)
        self.mc_tm3.setObjectName("mc_tm3")
        self.verticalLayout_13.addWidget(self.mc_tm3)
        self.mc_tm4 = QtWidgets.QTimeEdit(self.Horarios_miercoles)
        self.mc_tm4.setObjectName("mc_tm4")
        self.verticalLayout_13.addWidget(self.mc_tm4)
        self.mc_tm5 = QtWidgets.QTimeEdit(self.Horarios_miercoles)
        self.mc_tm5.setObjectName("mc_tm5")
        self.verticalLayout_13.addWidget(self.mc_tm5)
        self.verticalLayout_5.addWidget(self.Horarios_miercoles)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Miercoles_frame)
        self.Jueves_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Jueves_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Jueves_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Jueves_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Jueves_frame.setObjectName("Jueves_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Jueves_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cartel_jueves = QtWidgets.QLabel(self.Jueves_frame)
        self.cartel_jueves.setObjectName("cartel_jueves")
        self.verticalLayout_6.addWidget(self.cartel_jueves)
        self.Horarios_jueves = QtWidgets.QFrame(self.Jueves_frame)
        self.Horarios_jueves.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_jueves.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_jueves.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_jueves.setObjectName("Horarios_jueves")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Horarios_jueves)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lm_jv = QtWidgets.QSpinBox(self.Horarios_jueves)
        self.lm_jv.setObjectName("lm_jv")
        self.verticalLayout_14.addWidget(self.lm_jv)
        self.jv_tm1 = QtWidgets.QTimeEdit(self.Horarios_jueves)
        self.jv_tm1.setObjectName("jv_tm1")
        self.verticalLayout_14.addWidget(self.jv_tm1)
        self.jv_tm2 = QtWidgets.QTimeEdit(self.Horarios_jueves)
        self.jv_tm2.setObjectName("jv_tm2")
        self.verticalLayout_14.addWidget(self.jv_tm2)
        self.jv_tm3 = QtWidgets.QTimeEdit(self.Horarios_jueves)
        self.jv_tm3.setObjectName("jv_tm3")
        self.verticalLayout_14.addWidget(self.jv_tm3)
        self.jv_tm4 = QtWidgets.QTimeEdit(self.Horarios_jueves)
        self.jv_tm4.setObjectName("jv_tm4")
        self.verticalLayout_14.addWidget(self.jv_tm4)
        self.jv_tm5 = QtWidgets.QTimeEdit(self.Horarios_jueves)
        self.jv_tm5.setObjectName("jv_tm5")
        self.verticalLayout_14.addWidget(self.jv_tm5)
        self.verticalLayout_6.addWidget(self.Horarios_jueves)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Jueves_frame)
        self.Viernes_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Viernes_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Viernes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Viernes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Viernes_frame.setObjectName("Viernes_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Viernes_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cartel_viernes = QtWidgets.QLabel(self.Viernes_frame)
        self.cartel_viernes.setObjectName("cartel_viernes")
        self.verticalLayout_7.addWidget(self.cartel_viernes)
        self.Horarios_viernes = QtWidgets.QFrame(self.Viernes_frame)
        self.Horarios_viernes.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_viernes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_viernes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_viernes.setObjectName("Horarios_viernes")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.Horarios_viernes)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lm_vn = QtWidgets.QSpinBox(self.Horarios_viernes)
        self.lm_vn.setObjectName("lm_vn")
        self.verticalLayout_15.addWidget(self.lm_vn)
        self.vn_tm1 = QtWidgets.QTimeEdit(self.Horarios_viernes)
        self.vn_tm1.setObjectName("vn_tm1")
        self.verticalLayout_15.addWidget(self.vn_tm1)
        self.vn_tm2 = QtWidgets.QTimeEdit(self.Horarios_viernes)
        self.vn_tm2.setObjectName("vn_tm2")
        self.verticalLayout_15.addWidget(self.vn_tm2)
        self.vn_tm3 = QtWidgets.QTimeEdit(self.Horarios_viernes)
        self.vn_tm3.setObjectName("vn_tm3")
        self.verticalLayout_15.addWidget(self.vn_tm3)
        self.vn_tm4 = QtWidgets.QTimeEdit(self.Horarios_viernes)
        self.vn_tm4.setObjectName("vn_tm4")
        self.verticalLayout_15.addWidget(self.vn_tm4)
        self.vn_tm5 = QtWidgets.QTimeEdit(self.Horarios_viernes)
        self.vn_tm5.setObjectName("vn_tm5")
        self.verticalLayout_15.addWidget(self.vn_tm5)
        self.verticalLayout_7.addWidget(self.Horarios_viernes)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Viernes_frame)
        self.Sabado_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Sabado_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Sabado_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Sabado_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Sabado_frame.setObjectName("Sabado_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Sabado_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cartel_sabado = QtWidgets.QLabel(self.Sabado_frame)
        self.cartel_sabado.setObjectName("cartel_sabado")
        self.verticalLayout_8.addWidget(self.cartel_sabado)
        self.Horario_sabado = QtWidgets.QFrame(self.Sabado_frame)
        self.Horario_sabado.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horario_sabado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horario_sabado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horario_sabado.setObjectName("Horario_sabado")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.Horario_sabado)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lm_sb = QtWidgets.QSpinBox(self.Horario_sabado)
        self.lm_sb.setObjectName("lm_sb")
        self.verticalLayout_16.addWidget(self.lm_sb)
        self.sb_tm1 = QtWidgets.QTimeEdit(self.Horario_sabado)
        self.sb_tm1.setObjectName("sb_tm1")
        self.verticalLayout_16.addWidget(self.sb_tm1)
        self.sb_tm2 = QtWidgets.QTimeEdit(self.Horario_sabado)
        self.sb_tm2.setObjectName("sb_tm2")
        self.verticalLayout_16.addWidget(self.sb_tm2)
        self.sb_tm3 = QtWidgets.QTimeEdit(self.Horario_sabado)
        self.sb_tm3.setObjectName("sb_tm3")
        self.verticalLayout_16.addWidget(self.sb_tm3)
        self.sb_tm4 = QtWidgets.QTimeEdit(self.Horario_sabado)
        self.sb_tm4.setObjectName("sb_tm4")
        self.verticalLayout_16.addWidget(self.sb_tm4)
        self.sb_tm5 = QtWidgets.QTimeEdit(self.Horario_sabado)
        self.sb_tm5.setObjectName("sb_tm5")
        self.verticalLayout_16.addWidget(self.sb_tm5)
        self.verticalLayout_8.addWidget(self.Horario_sabado)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Sabado_frame)
        self.Domingo_frame = QtWidgets.QFrame(self.Semana_frame)
        self.Domingo_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Domingo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Domingo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Domingo_frame.setObjectName("Domingo_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Domingo_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cartel_domingo = QtWidgets.QLabel(self.Domingo_frame)
        self.cartel_domingo.setObjectName("cartel_domingo")
        self.verticalLayout_9.addWidget(self.cartel_domingo)
        self.Horarios_domingo = QtWidgets.QFrame(self.Domingo_frame)
        self.Horarios_domingo.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Horarios_domingo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Horarios_domingo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Horarios_domingo.setObjectName("Horarios_domingo")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.Horarios_domingo)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lm_dg = QtWidgets.QSpinBox(self.Horarios_domingo)
        self.lm_dg.setObjectName("lm_dg")
        self.verticalLayout_17.addWidget(self.lm_dg)
        self.dg_tm1 = QtWidgets.QTimeEdit(self.Horarios_domingo)
        self.dg_tm1.setObjectName("dg_tm1")
        self.verticalLayout_17.addWidget(self.dg_tm1)
        self.dg_tm2 = QtWidgets.QTimeEdit(self.Horarios_domingo)
        self.dg_tm2.setObjectName("dg_tm2")
        self.verticalLayout_17.addWidget(self.dg_tm2)
        self.dg_tm3 = QtWidgets.QTimeEdit(self.Horarios_domingo)
        self.dg_tm3.setObjectName("dg_tm3")
        self.verticalLayout_17.addWidget(self.dg_tm3)
        self.dg_tm4 = QtWidgets.QTimeEdit(self.Horarios_domingo)
        self.dg_tm4.setObjectName("dg_tm4")
        self.verticalLayout_17.addWidget(self.dg_tm4)
        self.dg_tm5 = QtWidgets.QTimeEdit(self.Horarios_domingo)
        self.dg_tm5.setObjectName("dg_tm5")
        self.verticalLayout_17.addWidget(self.dg_tm5)
        self.verticalLayout_9.addWidget(self.Horarios_domingo)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.Domingo_frame)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout.setStretch(0, 25)
        self.horizontalLayout.setStretch(1, 50)
        self.horizontalLayout.setStretch(2, 50)
        self.horizontalLayout.setStretch(3, 50)
        self.horizontalLayout.setStretch(4, 50)
        self.horizontalLayout.setStretch(5, 50)
        self.horizontalLayout.setStretch(6, 50)
        self.horizontalLayout.setStretch(7, 50)
        self.horizontalLayout.setStretch(8, 50)
        self.horizontalLayout.setStretch(9, 25)
        self.verticalLayout_10.addWidget(self.Semana_frame)
        self.Enviar_frame = QtWidgets.QFrame(self.Fondo)
        self.Enviar_frame.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Enviar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Enviar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Enviar_frame.setObjectName("Enviar_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Enviar_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.Enviar = QtWidgets.QFrame(self.Enviar_frame)
        self.Enviar.setStyleSheet("QFrame {\n"
"    background: transparent;\n"
"}")
        self.Enviar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Enviar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Enviar.setObjectName("Enviar")
        self.enviar_boton = QtWidgets.QPushButton(self.Enviar)
        self.enviar_boton.setGeometry(QtCore.QRect(0, 4, 290, 40))
        self.enviar_boton.setStyleSheet("QPushButton {\n"
"    background-color: blue;  /* Cambia \'green\' al color que prefieras */\n"
"    color: white;  /* Cambia \'white\' al color del texto que prefieras */\n"
"border rad\n"
"}\n"
"QPushButton { border-radius: 15px; /* Ajusta el valor para hacer el botón más o menos redondeado / background-color: #3498db; / Color de fondo del botón / color: white; / Color del texto del botón / border: 12px solid #2980b9; / Borde del botón */ }")
        self.enviar_boton.setObjectName("enviar_boton")
        self.horizontalLayout_4.addWidget(self.Enviar)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_4.setStretch(0, 75)
        self.horizontalLayout_4.setStretch(1, 25)
        self.horizontalLayout_4.setStretch(2, 6)
        self.verticalLayout_10.addWidget(self.Enviar_frame)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem7)
        self.verticalLayout_10.setStretch(0, 15)
        self.verticalLayout_10.setStretch(1, 15)
        self.verticalLayout_10.setStretch(2, 70)
        self.verticalLayout_10.setStretch(3, 15)
        self.verticalLayout_10.setStretch(4, 25)
        self.horizontalLayout_3.addWidget(self.Fondo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.volver_boton.clicked.connect(MainWindow.volver) # type: ignore
        self.enviar_boton.clicked.connect(MainWindow.enviar_dato) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.parametros_cf()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.volver_boton.setText(_translate("MainWindow", "Volver"))
        self.cartel_general.setText(_translate("MainWindow", "General"))
        self.cartel_lunes.setText(_translate("MainWindow", "Lunes"))
        self.cartel_martes.setText(_translate("MainWindow", "Martes"))
        self.cartel_miercoles.setText(_translate("MainWindow", "Miercoles"))
        self.cartel_jueves.setText(_translate("MainWindow", "Jueves"))
        self.cartel_viernes.setText(_translate("MainWindow", "Viernes"))
        self.cartel_sabado.setText(_translate("MainWindow", "Sabado"))
        self.cartel_domingo.setText(_translate("MainWindow", "Domingo"))
        self.enviar_boton.setText(_translate("MainWindow", "Enviar"))
