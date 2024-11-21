import sys
import json
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

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

    def setup_menu(self):
        # Set up the main menu interface
        self.ui_menu.setupUi(self)
        # Connect button to configuration window function
        self.ui_menu.config_boton.clicked.connect(self.show_config)
        self.ui_menu.estadistic_boton.clicked.connect(self.show_estadistic)
 
    def show_config(self):
        # Set up the configuration interface and show it
        self.ui_config.setupUi(self)

        MainWindow.parametros_cf
        self.ui_config.volver_boton.clicked.connect(self.volver)
        self.matriz_datos = MainWindow.extraer_dato(ruta)
    
    def parametros_cf(self):
        self.limites = MainWindow.extraer_limite(ruta2)
        self.lm = [self.ui_config.lm_grl, self.ui_config.lm_lu, self.ui_config.lm_mt, self.ui_config.lm_mc, self.ui_config.lm_jv, self.ui_config.lm_vn, self.ui_config.lm_sb, self.ui_config.lm_dg]
        for day_idx, day_widget in enumerate(self.lm):  # Usamos enumerate para obtener el índice y el widget
            day_widget.clear()
            day_widget.setMinimum(-1)
            day_widget.setMaximum(10)
            self.valor = self.limites[day_idx]
            day_widget.setValue(self.valor)
            if self.valor == -1:
                day_widget.setSpecialValueText("ilimitado")
                    
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
        self.matriz_datos = MainWindow.extraer_dato(ruta)
        for dia_idx, dia_widget in enumerate(self.tm):  # `self.tm` es la lista de listas con los widgets de horarios
            for hora_idx, hora_widget in enumerate(dia_widget):
                hora_widget.clear()  # Limpiamos cualquier texto anterior
                hora_widget.setTimeRange(QtCore.QTime(0, 0, 0), QtCore.QTime(23, 59, 59))
                # Verificamos si el horario actual es "0:0"
                self.valor = self.matriz_datos[dia_idx][hora_idx]
                if self.valor == "0:0":
                    # Si el valor es "0:0", mostramos un texto especial
                    hora_widget.setSpecialValueText("--:--")
                else:
                    # Configuramos el rango de tiempo permitido
                    hora_widget.setTime(QtCore.QTime(int(self.valor.split(":")[0]), int(self.valor.split(":")[1])))
        
    def volver(self):
        # Return to the main menu
        self.setup_menu()

    def show_estadistic(self):
        # Return to the main menu
        self.ui_estadistic.setupUi(self)
        """self.ui_estadistic.volver_boton.clicked.connect(self.volver)""" 

        self.grafica = Canvas_grafica()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()

        self.ui_estadistic.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic.grafica_tres.addWidget(self.grafica2)
        self.ui_estadistic.grafica_cuatro.addWidget(self.grafica3)

    def enviar_dato(self):
        # Obtener el valor del QSpinBox y añadirlo a la matriz
        cg = self.ui_config 
        self.limites = [cg.lm_grl.value(), cg.lm_lu.value(), cg.lm_mt.value(), cg.lm_mc.value(), cg.lm_jv.value(), cg.lm_vn.value(), cg.lm_sb.value(), cg.lm_dg.value()]

        self.matriz_datos = [
                                [ str(cg.grl_tm1.time().hour()) +":"+ str(cg.grl_tm1.time().minute()), str(cg.grl_tm2.time().hour()) +":"+ str(cg.grl_tm2.time().minute()), str(cg.grl_tm3.time().hour()) +":"+ str(cg.grl_tm3.time().minute()), str(cg.grl_tm4.time().hour()) +":"+ str(cg.grl_tm4.time().minute()), str(cg.grl_tm5.time().hour()) +":"+ str(cg.grl_tm5.time().minute()),],
                                [ str(cg.lu_tm1.time().hour()) +":"+ str(cg.lu_tm1.time().minute()), str(cg.lu_tm2.time().hour()) +":"+ str(cg.lu_tm2.time().minute()),str(cg.lu_tm3.time().hour()) +":"+ str(cg.lu_tm3.time().minute()), str(cg.lu_tm4.time().hour()) +":"+ str(cg.lu_tm4.time().minute()), str(cg.lu_tm5.time().hour()) +":"+ str(cg.lu_tm5.time().minute())],
                                [ str(cg.mt_tm1.time().hour()) +":"+ str(cg.mt_tm1.time().minute()), str(cg.mt_tm2.time().hour()) +":"+ str(cg.mt_tm2.time().minute()), str(cg.mt_tm3.time().hour()) +":"+ str(cg.mt_tm3.time().minute()), str(cg.mt_tm4.time().hour()) +":"+ str(cg.mt_tm4.time().minute()),str(cg.mt_tm5.time().hour()) +":"+ str(cg.mt_tm5.time().minute())],
                                [ str(cg.mc_tm1.time().hour()) +":"+ str(cg.mc_tm1.time().minute()), str(cg.mc_tm2.time().hour()) +":"+ str(cg.mc_tm2.time().minute()), str(cg.mc_tm3.time().hour()) +":"+ str(cg.mc_tm3.time().minute()), str(cg.mc_tm4.time().hour()) +":"+ str(cg.mc_tm4.time().minute()), str(cg.mc_tm5.time().hour()) +":"+ str(cg.mc_tm5.time().minute())],
                                [ str(cg.jv_tm1.time().hour()) +":"+ str(cg.jv_tm1.time().minute()), str(cg.jv_tm2.time().hour()) +":"+ str(cg.jv_tm2.time().minute()), str(cg.jv_tm3.time().hour()) +":"+ str(cg.jv_tm3.time().minute()), str(cg.jv_tm4.time().hour()) +":"+ str(cg.jv_tm4.time().minute()), str(cg.jv_tm5.time().hour()) +":"+ str(cg.jv_tm5.time().minute())],
                                [ str(cg.vn_tm1.time().hour()) +":"+ str(cg.vn_tm1.time().minute()), str(cg.vn_tm2.time().hour()) +":"+ str(cg.vn_tm2.time().minute()), str(cg.vn_tm3.time().hour()) +":"+ str(cg.vn_tm3.time().minute()), str(cg.vn_tm4.time().hour()) +":"+ str(cg.vn_tm4.time().minute()), str(cg.vn_tm5.time().hour()) +":"+ str(cg.vn_tm5.time().minute()),],
                                [ str(cg.sb_tm1.time().hour()) +":"+ str(cg.sb_tm1.time().minute()), str(cg.sb_tm2.time().hour()) +":"+ str(cg.sb_tm2.time().minute()), str(cg.sb_tm3.time().hour()) +":"+ str(cg.sb_tm3.time().minute()), str(cg.sb_tm4.time().hour()) +":"+ str(cg.sb_tm4.time().minute()), str(cg.sb_tm5.time().hour()) +":"+ str(cg.sb_tm5.time().minute()),],
                                [ str(cg.dg_tm1.time().hour()) +":"+ str(cg.dg_tm1.time().minute()), str(cg.dg_tm2.time().hour()) +":"+ str(cg.dg_tm2.time().minute()), str(cg.dg_tm3.time().hour()) +":"+ str(cg.dg_tm3.time().minute()), str(cg.dg_tm4.time().hour()) +":"+ str(cg.dg_tm4.time().minute()), str(cg.dg_tm5.time().hour()) +":"+ str(cg.dg_tm5.time().minute())]
                            ]

        # Imprimir la matriz para verificar
        print("Matriz de datos:", self.matriz_datos)

        self.datos = {
            "matriz":self.matriz_datos
        }
        self.limit = {
            "limite":self.limites
        }

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)
            
        with open(ruta2, "w", encoding="utf-8") as archivo:
            json.dump(self.limit, archivo, indent=4, ensure_ascii=False)  # `ensure_ascii=False` para caracteres especiales
    
        print(f"Datos guardados en {ruta} y {ruta2}")
        MainWindow.extraer_dato(ruta)

    def extraer_dato(ruta):
        with open(ruta, "r", encoding="utf-8") as dato:
            objeto = json.load(dato)  # Carga el JSON como un diccionario
            matriz = objeto.get("matriz")  # Obtén el valor asociado a la clave "matriz"
        return matriz
    
    def extraer_limite(ruta2):
        with open(ruta2, "r", encoding="utf-8") as dato:
            objeto = json.load(dato)  # Carga el JSON como un diccionario
            limite = objeto.get("limite")  # Obtén el valor asociado a la clave "matriz"
        return limite
    
    class Dato_diario():
        pass
        
class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        nombres = ['15', '25', '30', '35','40']
        colores = ['red','red','red','red', 'red']
        tamaño = [10, 15, 20, 25, 30]

        self.ax.bar(nombres, tamaño, color = colores)
        self.fig.suptitle('Grafica de Barras',size=9)


class Canvas_grafica2(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        nombres = ['Fresa', 'Piña', 'Lima', 'Uva']
        colores = ['blue','yellow','aqua','fuchsia']
        tamaño = [20, 26, 30, 24]
        explotar = [0.05, 0.05, 0.05, 0.05] 

        plt.title("Cantidad de Frutas Disponibles", color='black', size=9, family="DejaVu Sans")


        self.ax.pie(tamaño, explode = explotar, labels = nombres, 
            colors = colores,
                autopct = '%1.0f%%', pctdistance = 0.6,
                shadow=True, startangle=90, radius = 0.8, 
                labeldistance=1.1)  
        self.ax.axis('equal')


class Canvas_grafica3(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        self.fig.suptitle('Grafica de Datos',size=9)
        np.random.seed(20)
        y = np.random.randn(150).cumsum()

        self.ax = plt.axes()
        plt.plot(y, color='magenta')


class Canvas_grafica4(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        x = [1, 2, 3, 4, 5,6,7]
        y1 = [1, 0, 1, 3, 2,4,3]
        y2 = [0, 2, 2, 3, 4,6,5]
        y3 = [3, 1, 3, 4, 2,7,6]

        y = np.vstack([y1, y2, y3])

        labels = ["Y1 ", "Y2", "Y3"]
        color = ["orange","blue","green"]

        self.ax.stackplot(x, y1, y2, y3, labels=labels,colors=color)
        self.ax.legend(loc='upper left')
        self.ax.stackplot(x, y)
        self.fig.suptitle('Grafica Stackplot',size=9)


if __name__ == "__main__":  # Entry point check
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    ruta = "horario.json"
    ruta2 = "limite.json"
    sys.exit(app.exec_())  # Start the application loop
    
    