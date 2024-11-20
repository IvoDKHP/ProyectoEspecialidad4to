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
        self.ui_menu.config_boton.clicked.connect(self.show_config)

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
            [cg.lm_grl.value(), str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.grl_tm2.time().hour()) +":"+ str(cg.grl_tm2.time().minute()), str(cg.grl_tm3.time().hour()) +":"+ str(cg.grl_tm3.time().minute()),  str(cg.grl_tm4.time().hour()) +":"+ str(cg.grl_tm4.time().minute()), str(cg.grl_tm5.time().hour()) +":"+ str(cg.grl_tm5.time().minute())],
            [cg.lm_lu.value(), str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.lu_tm2.time().hour()) +":"+ str(cg.lu_tm2.time().minute()), str(cg.lu_tm3.time().hour()) +":"+ str(cg.lu_tm3.time().minute()), str(cg.lu_tm4.time().hour()) +":"+ str(cg.lu_tm4.time().minute()), str(cg.lu_tm5.time().hour()) +":"+ str(cg.lu_tm5.time().minute())],
            [cg.lm_mt.value(), str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mt_tm2.time().hour()) +":"+ str(cg.mt_tm2.time().minute()), str(cg.mt_tm3.time().hour()) +":"+ str(cg.mt_tm3.time().minute()), str(cg.mt_tm4.time().hour()) +":"+ str(cg.mt_tm4.time().minute()), str(cg.mt_tm5.time().hour()) +":"+ str(cg.mt_tm5.time().minute())],
            [cg.lm_mc.value(), str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.mc_tm2.time().hour()) +":"+ str(cg.mc_tm2.time().minute()), str(cg.mc_tm3.time().hour()) +":"+ str(cg.mc_tm3.time().minute()), str(cg.mc_tm4.time().hour()) +":"+ str(cg.mc_tm4.time().minute()), str(cg.mc_tm5.time().hour()) +":"+ str(cg.mc_tm5.time().minute())],
            [cg.lm_jv.value(), str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.jv_tm2.time().hour()) +":"+ str(cg.jv_tm2.time().minute()), str(cg.jv_tm3.time().hour()) +":"+ str(cg.jv_tm3.time().minute()), str(cg.jv_tm4.time().hour()) +":"+ str(cg.jv_tm4.time().minute()), str(cg.jv_tm5.time().hour()) +":"+ str(cg.jv_tm5.time().minute())],
            [cg.lm_vn.value(), str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.vn_tm2.time().hour()) +":"+ str(cg.vn_tm2.time().minute()), str(cg.vn_tm3.time().hour()) +":"+ str(cg.vn_tm3.time().minute()), str(cg.vn_tm4.time().hour()) +":"+ str(cg.vn_tm4.time().minute()), str(cg.vn_tm5.time().hour()) +":"+ str(cg.vn_tm5.time().minute())],
            [cg.lm_sb.value(), str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.sb_tm2.time().hour()) +":"+ str(cg.sb_tm2.time().minute()), str(cg.sb_tm3.time().hour()) +":"+ str(cg.sb_tm3.time().minute()), str(cg.sb_tm4.time().hour()) +":"+ str(cg.sb_tm4.time().minute()), str(cg.sb_tm5.time().hour()) +":"+ str(cg.sb_tm5.time().minute())],
            [cg.lm_dg.value(), str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute()), str(cg.dg_tm2.time().hour()) +":"+ str(cg.dg_tm2.time().minute()), str(cg.dg_tm3.time().hour()) +":"+ str(cg.dg_tm3.time().minute()), str(cg.dg_tm4.time().hour()) +":"+ str(cg.dg_tm4.time().minute()), str(cg.dg_tm5.time().hour()) +":"+ str(cg.dg_tm5.time().minute())]
        ]
        
        
        # Imprimir la matriz para verificar
        print("Matriz de datos:", self.matriz_datos)
        #self.ordenar_horarios()
        self.ordenar_horarios()

    def ordenar_horarios(self):
        for fila in 7:
            self.lista = []
            for horario in range(1, 5):
                self.min_ttl = int(self.matriz_datos[fila][horario].split(":")[0]) * 60 + int(self.matriz_datos[fila][horario].split(":")[1])
                if self.min_ttl != 0:
                    self.lista.append(self.min_ttl)
            self.lista.sort()
            for horario in range(1, 5):
                try:
                    self.matriz_datos[fila][horario] = self.lista[horario - 1]
                    self.matriz_datos[fila][horario] = str(self.matriz_datos[fila][horario]//60) + ":" + str(self.matriz_datos[fila][horario]%60)
                except:
                    self.matriz_datos[fila][horario] = 0
            




    def ordenar_horarios(self):
        # Iterar a través de cada fila en la matriz
        for fila in self.matriz_datos:
            # Ignorar la primera columna y obtener solo los horarios (sin el primer valor)
            horarios = fila[1:]
            
            # Separar los horarios válidos de los "00:00"
            self.horarios_validos = [horario for horario in horarios if horario != "00:00"]
            self.horarios_00_00 = [horario for horario in horarios if horario == "00:00"]
            
            # Convertir los horarios válidos a minutos para ordenar
            horarios_en_minutos = []
            for horario in self.horarios_validos:
                horas, minutos = map(int, horario.split(':'))
                total_minutos = horas * 60 + minutos
                horarios_en_minutos.append(total_minutos)
            
            # Ordenar los horarios válidos en minutos de menor a mayor
            horarios_en_minutos.sort()
            
            # Convertir de vuelta a formato HH:MM los horarios ordenados
            horarios_ordenados = []
            for minutos_totales in horarios_en_minutos:
                horas = minutos_totales // 60
                minutos = minutos_totales % 60
                horarios_ordenados.append(f"{horas:02}:{minutos:02}")
            
            # Añadir los valores "00:00" al final de la lista ordenada
            horarios_ordenados.extend(self.horarios_00_00)
            
            # Asignar los horarios ordenados de vuelta en la fila, manteniendo la primera columna intacta
            fila[1:] = horarios_ordenados
        
        for fila in self.matriz_datos:
            if horario == 0:
                fila.append(horario)
        
        # Imprimir la matriz ordenada para verificar
        print("Matriz de datos ordenada:", self.matriz_datos)







if __name__ == "__main__":  # Entry point check
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application loop