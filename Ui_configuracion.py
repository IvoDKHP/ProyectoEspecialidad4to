from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.volver_boton = QtWidgets.QPushButton(self.centralwidget)
        self.volver_boton.setGeometry(QtCore.QRect(0, 5, 71, 30))
        self.volver_boton.setObjectName("volver_boton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 37, 841, 199))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.SemanaLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.SemanaLayout.setContentsMargins(0, 0, 0, 0)
        self.SemanaLayout.setObjectName("SemanaLayout")
        self.GeneralLayout = QtWidgets.QVBoxLayout()
        self.GeneralLayout.setObjectName("GeneralLayout")
        self.cartel_general = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_general.setObjectName("cartel_general")
        self.GeneralLayout.addWidget(self.cartel_general)
        self.lm_grl = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_grl.setObjectName("lm_grl")
        self.GeneralLayout.addWidget(self.lm_grl)
        self.grl_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.grl_tm1.setObjectName("grl_tm1")
        self.GeneralLayout.addWidget(self.grl_tm1)
        self.grl_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.grl_tm2.setObjectName("grl_tm2")
        self.GeneralLayout.addWidget(self.grl_tm2)
        self.grl_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.grl_tm3.setObjectName("grl_tm3")
        self.GeneralLayout.addWidget(self.grl_tm3)
        self.grl_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.grl_tm4.setObjectName("grl_tm4")
        self.GeneralLayout.addWidget(self.grl_tm4)
        self.grl_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.grl_tm5.setObjectName("grl_tm5")
        self.GeneralLayout.addWidget(self.grl_tm5)
        self.SemanaLayout.addLayout(self.GeneralLayout)
        self.LunesLayout = QtWidgets.QVBoxLayout()
        self.LunesLayout.setObjectName("LunesLayout")
        self.cartel_lunes = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_lunes.setObjectName("cartel_lunes")
        self.LunesLayout.addWidget(self.cartel_lunes)
        self.lm_lu = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_lu.setObjectName("lm_lu")
        self.LunesLayout.addWidget(self.lm_lu)
        self.lu_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.lu_tm1.setObjectName("lu_tm1")
        self.LunesLayout.addWidget(self.lu_tm1)
        self.lu_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.lu_tm2.setObjectName("lu_tm2")
        self.LunesLayout.addWidget(self.lu_tm2)
        self.lu_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.lu_tm3.setObjectName("lu_tm3")
        self.LunesLayout.addWidget(self.lu_tm3)
        self.lu_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.lu_tm4.setObjectName("lu_tm4")
        self.LunesLayout.addWidget(self.lu_tm4)
        self.lu_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.lu_tm5.setObjectName("lu_tm5")
        self.LunesLayout.addWidget(self.lu_tm5)
        self.SemanaLayout.addLayout(self.LunesLayout)
        self.MartesLayout = QtWidgets.QVBoxLayout()
        self.MartesLayout.setObjectName("MartesLayout")
        self.cartel_martes = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_martes.setObjectName("cartel_martes")
        self.MartesLayout.addWidget(self.cartel_martes)
        self.lm_mt = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_mt.setObjectName("lm_mt")
        self.MartesLayout.addWidget(self.lm_mt)
        self.mt_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mt_tm1.setObjectName("mt_tm1")
        self.MartesLayout.addWidget(self.mt_tm1)
        self.mt_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mt_tm2.setObjectName("mt_tm2")
        self.MartesLayout.addWidget(self.mt_tm2)
        self.mt_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mt_tm3.setObjectName("mt_tm3")
        self.MartesLayout.addWidget(self.mt_tm3)
        self.mt_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mt_tm4.setObjectName("mt_tm4")
        self.MartesLayout.addWidget(self.mt_tm4)
        self.mt_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mt_tm5.setObjectName("mt_tm5")
        self.MartesLayout.addWidget(self.mt_tm5)
        self.SemanaLayout.addLayout(self.MartesLayout)
        self.MiercolesLayout = QtWidgets.QVBoxLayout()
        self.MiercolesLayout.setObjectName("MiercolesLayout")
        self.cartel_miercoles = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_miercoles.setObjectName("cartel_miercoles")
        self.MiercolesLayout.addWidget(self.cartel_miercoles)
        self.lm_mc = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_mc.setObjectName("lm_mc")
        self.MiercolesLayout.addWidget(self.lm_mc)
        self.mc_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mc_tm1.setObjectName("mc_tm1")
        self.MiercolesLayout.addWidget(self.mc_tm1)
        self.mc_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mc_tm2.setObjectName("mc_tm2")
        self.MiercolesLayout.addWidget(self.mc_tm2)
        self.mc_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mc_tm3.setObjectName("mc_tm3")
        self.MiercolesLayout.addWidget(self.mc_tm3)
        self.mc_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mc_tm4.setObjectName("mc_tm4")
        self.MiercolesLayout.addWidget(self.mc_tm4)
        self.mc_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.mc_tm5.setObjectName("mc_tm5")
        self.MiercolesLayout.addWidget(self.mc_tm5)
        self.SemanaLayout.addLayout(self.MiercolesLayout)
        self.JuevesLayout = QtWidgets.QVBoxLayout()
        self.JuevesLayout.setObjectName("JuevesLayout")
        self.cartel_jueves = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_jueves.setObjectName("cartel_jueves")
        self.JuevesLayout.addWidget(self.cartel_jueves)
        self.lm_jv = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_jv.setObjectName("lm_jv")
        self.JuevesLayout.addWidget(self.lm_jv)
        self.jv_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.jv_tm1.setObjectName("jv_tm1")
        self.JuevesLayout.addWidget(self.jv_tm1)
        self.jv_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.jv_tm2.setObjectName("jv_tm2")
        self.JuevesLayout.addWidget(self.jv_tm2)
        self.jv_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.jv_tm3.setObjectName("jv_tm3")
        self.JuevesLayout.addWidget(self.jv_tm3)
        self.jv_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.jv_tm4.setObjectName("jv_tm4")
        self.JuevesLayout.addWidget(self.jv_tm4)
        self.jv_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.jv_tm5.setObjectName("jv_tm5")
        self.JuevesLayout.addWidget(self.jv_tm5)
        self.SemanaLayout.addLayout(self.JuevesLayout)
        self.ViernesLayout = QtWidgets.QVBoxLayout()
        self.ViernesLayout.setObjectName("ViernesLayout")
        self.cartel_viernes = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_viernes.setObjectName("cartel_viernes")
        self.ViernesLayout.addWidget(self.cartel_viernes)
        self.lm_vn = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_vn.setObjectName("lm_vn")
        self.ViernesLayout.addWidget(self.lm_vn)
        self.vn_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.vn_tm1.setObjectName("vn_tm1")
        self.ViernesLayout.addWidget(self.vn_tm1)
        self.vn_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.vn_tm2.setObjectName("vn_tm2")
        self.ViernesLayout.addWidget(self.vn_tm2)
        self.vn_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.vn_tm3.setObjectName("vn_tm3")
        self.ViernesLayout.addWidget(self.vn_tm3)
        self.vn_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.vn_tm4.setObjectName("vn_tm4")
        self.ViernesLayout.addWidget(self.vn_tm4)
        self.vn_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.vn_tm5.setObjectName("vn_tm5")
        self.ViernesLayout.addWidget(self.vn_tm5)
        self.SemanaLayout.addLayout(self.ViernesLayout)
        self.SabadoLayout = QtWidgets.QVBoxLayout()
        self.SabadoLayout.setObjectName("SabadoLayout")
        self.cartel_sabado = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_sabado.setObjectName("cartel_sabado")
        self.SabadoLayout.addWidget(self.cartel_sabado)
        self.lm_sb = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_sb.setObjectName("lm_sb")
        self.SabadoLayout.addWidget(self.lm_sb)
        self.sb_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.sb_tm1.setObjectName("sb_tm1")
        self.SabadoLayout.addWidget(self.sb_tm1)
        self.sb_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.sb_tm2.setObjectName("sb_tm2")
        self.SabadoLayout.addWidget(self.sb_tm2)
        self.sb_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.sb_tm3.setObjectName("sb_tm3")
        self.SabadoLayout.addWidget(self.sb_tm3)
        self.sb_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.sb_tm4.setObjectName("sb_tm4")
        self.SabadoLayout.addWidget(self.sb_tm4)
        self.sb_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.sb_tm5.setObjectName("sb_tm5")
        self.SabadoLayout.addWidget(self.sb_tm5)
        self.SemanaLayout.addLayout(self.SabadoLayout)
        self.DomingoLayout = QtWidgets.QVBoxLayout()
        self.DomingoLayout.setObjectName("DomingoLayout")
        self.cartel_domingo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cartel_domingo.setObjectName("cartel_domingo")
        self.DomingoLayout.addWidget(self.cartel_domingo)
        self.lm_dg = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.lm_dg.setObjectName("lm_dg")
        self.DomingoLayout.addWidget(self.lm_dg)
        self.dg_tm1 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.dg_tm1.setObjectName("dg_tm1")
        self.DomingoLayout.addWidget(self.dg_tm1)
        self.dg_tm2 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.dg_tm2.setObjectName("dg_tm2")
        self.DomingoLayout.addWidget(self.dg_tm2)
        self.dg_tm3 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.dg_tm3.setObjectName("dg_tm3")
        self.DomingoLayout.addWidget(self.dg_tm3)
        self.dg_tm4 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.dg_tm4.setObjectName("dg_tm4")
        self.DomingoLayout.addWidget(self.dg_tm4)
        self.dg_tm5 = QtWidgets.QTimeEdit(self.horizontalLayoutWidget)
        self.dg_tm5.setObjectName("dg_tm5")
        self.DomingoLayout.addWidget(self.dg_tm5)
        self.SemanaLayout.addLayout(self.DomingoLayout)
        self.enviar_boton = QtWidgets.QPushButton(self.centralwidget)
        self.enviar_boton.setGeometry(QtCore.QRect(750, 238, 91, 30))
        self.enviar_boton.setObjectName("enviar_boton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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