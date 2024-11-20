import sys
import json

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
        self.ui_menu.pushButton.clicked.connect(self.parametros_cf)

    def show_config(self):
        # Set up the configuration interface and show it
        self.ui_config.setupUi(self)
        self.ui_config.volver_boton.clicked.connect(self.volver)
        self.matriz_datos = MainWindow.extraer_dato(ruta)
    
    def parametros_cf(self):
        self.lm = [self.ui_config.lm_grl, self.ui_config.lm_lu, self.ui_config.lm_mt, self.ui_config.lm_mc, self.ui_config.lm_jv, self.ui_config.lm_vn, self.ui_config.lm_sb, self.ui_config.lm_dg]
        for day in self.lm:
            day.clear()  
            if day.value() == -1:
                day.setSpecialValueText("--")
            day.setMinimum(-1)
            day.setMaximum(10)
            day.setValue(-1)
        
        self.tm =   [
                        [self.ui_config.grl_tm1, self.ui_config.grl_tm2, self.ui_config.grl_tm3, self.ui_config.grl_tm4, self.ui_config.grl_tm5],   #horarios generales
                        [self.ui_config.lu_tm1, self.ui_config.lu_tm2, self.ui_config.lu_tm3, self.ui_config.lu_tm4, self.ui_config.lu_tm5],        #horarios lunes
                        [self.ui_config.mt_tm1, self.ui_config.mt_tm2, self.ui_config.mt_tm3, self.ui_config.mt_tm4, self.ui_config.mt_tm5],        #horarios martes
                        [self.ui_config.mc_tm1, self.ui_config.mc_tm2, self.ui_config.mc_tm3, self.ui_config.mc_tm4, self.ui_config.mc_tm5],        #horarios miercoles
                        [self.ui_config.jv_tm1, self.ui_config.jv_tm2, self.ui_config.jv_tm3, self.ui_config.jv_tm4, self.ui_config.jv_tm5],        #horarios jueves
                        [self.ui_config.vn_tm1, self.ui_config.vn_tm2, self.ui_config.vn_tm3, self.ui_config.vn_tm4, self.ui_config.vn_tm5],        #horarios viernes
                        [self.ui_config.sb_tm1, self.ui_config.sb_tm2, self.ui_config.sb_tm3, self.ui_config.sb_tm4, self.ui_config.sb_tm5],        #horarios sabado
                        [self.ui_config.dg_tm1, self.ui_config.dg_tm2, self.ui_config.dg_tm3, self.ui_config.dg_tm4, self.ui_config.dg_tm5]         #horarios domingo
                    ]
        
        for dia in self.tm:  # `self.tm` es la lista de listas con los widgets de horarios
            for horario in dia:
                horario.clear()  # Limpiamos cualquier texto anterior

                # Verificamos si el horario actual es "0:0"
                if horario.time().toString("H:m") == "0:0":
                    # Si el valor es "0:0", mostramos un texto especial
                    horario.setSpecialValueText("--:--:--")
                else:
                    # Configuramos el rango de tiempo permitido
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
                                [cg.lm_grl.value(), cg.grl_tm1.time(), cg.grl_tm2.time(), cg.grl_tm3.time(), cg.grl_tm4.time(), cg.grl_tm5.time()],
                                [cg.lm_lu.value(), cg.lu_tm1.time(), cg.lu_tm2.time(), cg.lu_tm3.time(), cg.lu_tm4.time(), cg.lu_tm5.time()],
                                [cg.lm_mt.value(), cg.mt_tm1.time(), cg.mt_tm2.time(), cg.mt_tm3.time(), cg.mt_tm4.time(), cg.mt_tm5.time()],
                                [cg.lm_mc.value(), cg.mc_tm1.time(), cg.mc_tm2.time(), cg.mc_tm3.time(), cg.mc_tm4.time(), cg.mc_tm5.time()],
                                [cg.lm_jv.value(), cg.jv_tm1.time(), cg.jv_tm2.time(), cg.jv_tm3.time(), cg.jv_tm4.time(), cg.jv_tm5.time()],
                                [cg.lm_vn.value(), cg.vn_tm1.time(), cg.vn_tm2.time(), cg.vn_tm3.time(), cg.vn_tm4.time(), cg.vn_tm5.time()],
                                [cg.lm_sb.value(), cg.sb_tm1.time(), cg.sb_tm2.time(), cg.sb_tm3.time(), cg.sb_tm4.time(), cg.sb_tm5.time()],
                                [cg.lm_dg.value(), cg.dg_tm1.time(), cg.dg_tm2.time(), cg.dg_tm3.time(), cg.dg_tm4.time(), cg.dg_tm5.time()]
                            ]


        
        # Imprimir la matriz para verificar
        print("Matriz de datos:", self.matriz_datos)

        self.datos = {
            "matriz":self.matriz_datos
        }

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)  # `ensure_ascii=False` para caracteres especiales
    
        print("Datos guardados en " , ruta)
        
        MainWindow.extraer_dato(ruta)

    def extraer_dato(ruta):
        with open(ruta, "r", encoding="utf-8") as dato:
            objeto = json.load(dato)  # Carga el JSON como un diccionario
            matriz = objeto.get("matriz")  # Obtén el valor asociado a la clave "matriz"
        print(matriz)
        return matriz

if __name__ == "__main__":  # Entry point check
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    ruta = "data.json"
    sys.exit(app.exec_())  # Start the application loop
    
