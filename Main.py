import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

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
        self.ui_config.volver_boton.clicked.connect(self.show_menu)

    def show_menu(self):
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
