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
from Ui_estadisticas import*

class MainWindow(QMainWindow):  # Main window class inherited from QMainWindow
    def __init__(self):  # Constructor
        super().__init__()
        self.ui_menu = Ui_menu.Ui_MainWindow()  # Main menu UI
        self.ui_config = Ui_configuracion.Ui_MainWindow()  # Configuration UI
        self.ui_estadistic = Ui_MainWindow()
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

    """def extraer_dato(ruta):
        with open(ruta, "r", encoding="utf-8") as dato:
            objeto = json.load(dato)  # Carga el JSON como un diccionario
            matriz = objeto.get("matriz")  # Obtén el valor asociado a la clave "matriz"
        print(matriz)
        return matriz"""
    
    def extraer_dato(ruta):
        with open(ruta, "r", encoding="utf-8") as dato:
            objeto = json.load(dato)  # Carga el JSON como un diccionario
            matriz = objeto.get("matriz")  # Obtén el valor asociado a la clave "matriz"
        print(matriz)
        return matriz
    
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
    ruta = "data.json"
    sys.exit(app.exec_())  # Start the application loop
    
