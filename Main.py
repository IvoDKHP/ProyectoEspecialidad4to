import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import Ui_menu
import Ui_configuracion
import Ui_estadisticas

class MainWindow(QMainWindow):  # Main window class inherited from QMainWindow
    def __init__(self):  # Constructor
        super().__init__()
        self.ui_menu = Ui_menu.Ui_MainWindow()  # Main menu UI
        self.ui_config = Ui_configuracion.Ui_MainWindow()  # Configuration UI
        self.ui_estadistic = Ui_estadisticas.Ui_MainWindow()
        self.setup_menu()
        self.matriz_datos = []

    def setup_menu(self):
        # Set up the main menu interface
        self.ui_menu.setupUi(self)
        # Connect button to configuration window function
        self.ui_menu.pushButton.clicked.connect(self.show_config)

    def show_config(self):
        # Set up the configuration interface and show it
        self.ui_config.setupUi(self)
        self.ui_config.volver_boton.clicked.connect(self.volver)
    
    def parametros_cf(self):
        self.lm = [self.ui_config.lm_grl, self.ui_config.lm_lu, self.ui_config.lm_mt, self.ui_config.lm_mc, self.ui_config.lm_jv, self.ui_config.lm_vn, self.ui_config.lm_sb, self.ui_config.lm_dg]
        for day in self.lm:
            day.clear()  
            day.setSpecialValueText("--")
            day.setMinimum(-1)
            day.setMaximum(10)
            day.setValue(-1)
        
        self.tm =   [
                        [self.ui_config.grl_tm1, self.ui_config.grl_tm2, self.ui_config.grl_tm3, self.ui_config.grl_tm4, self.ui_config.grl_tm5],
                        [self.ui_config.lu_tm1, self.ui_config.lu_tm2, self.ui_config.lu_tm3, self.ui_config.lu_tm4, self.ui_config.lu_tm5],
                        [self.ui_config.mt_tm1, self.ui_config.mt_tm2, self.ui_config.mt_tm3, self.ui_config.mt_tm4, self.ui_config.mt_tm5],
                        [self.ui_config.mc_tm1, self.ui_config.mc_tm2, self.ui_config.mc_tm3, self.ui_config.mc_tm4, self.ui_config.mc_tm5],
                        [self.ui_config.jv_tm1, self.ui_config.jv_tm2, self.ui_config.jv_tm3, self.ui_config.jv_tm4, self.ui_config.jv_tm5],
                        [self.ui_config.vn_tm1, self.ui_config.vn_tm2, self.ui_config.vn_tm3, self.ui_config.vn_tm4, self.ui_config.vn_tm5],
                        [self.ui_config.sb_tm1, self.ui_config.sb_tm2, self.ui_config.sb_tm3, self.ui_config.sb_tm4, self.ui_config.sb_tm5],
                        [self.ui_config.dg_tm1, self.ui_config.dg_tm2, self.ui_config.dg_tm3, self.ui_config.dg_tm4, self.ui_config.dg_tm5]
                    ]
        
        for dia in self.tm:
            for horario in dia:
                horario.clear()  
                horario.setSpecialValueText("--:--:--")  
                horario.setTimeRange(QtCore.QTime(0, 0, 0), QtCore.QTime(23, 59, 59))  
                horario.setTime(QtCore.QTime())  
        
    def volver(self):
        # Return to the main menu
        self.setup_menu()

    def show_estadistic(self):
        # Return to the main menu
        self.ui_estadistic.setupUi(self)
        self.ui_estadistic.volver_boton.clicked.connect(self.show_menu)  

    def enviar_dato(self):
        # Obtener el valor del QSpinBox y añadirlo a la matriz
        cg = self.ui_config 
        self.matriz_datos = [
                            [cg.lm_grl.value(), cg.lm_lu.value(), cg.lm_mt.value(), cg.lm_mc.value(), cg.lm_jv.value(), cg.lm_vn.value(), cg.lm_sb.value(), cg.lm_dg.value()], 
                            [str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute())], 
                            [str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute())],
                            [str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute())],
                            [str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute())],
                            [str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute())]
                            ] # dateTime()
        
        # Imprimir la matriz para verificar
        print("Matriz de datos:", self.matriz_datos)

if __name__ == "__main__":  # Entry point check
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application loop
