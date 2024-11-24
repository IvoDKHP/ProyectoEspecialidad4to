import sys
import json
import serial
from datetime import datetime
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import Ui_menu
import Ui_configuracion
import Ui_estadisticas_1
import Ui_estadisticas_2

class MainWindow(QMainWindow):  # Main window class inherited from QMainWindow
    def __init__(self):  # Constructor
        super().__init__()
        self.ui_menu = Ui_menu.Ui_MainWindow()  #facilita la coneccion con Ui_menu
        self.ui_config = Ui_configuracion.Ui_MainWindow()  #facilita la coneccion con Ui_configuracion
        self.ui_estadistic = Ui_estadisticas_1.Ui_MainWindow() #facilita la coneccion con Ui_estadisticas_1
        self.ui_estadistic_2 = Ui_estadisticas_2.Ui_MainWindow() #facilita la coneccion con Ui_estadisticas_2
        self.setup_menu() #Inicia la pagina Menu

        self.showFullScreen() #Adapta a pantalla completa

    
    def setup_menu(self):
        self.ui_menu.setupUi(self) #Funcion que abre el Menu

        self.ui_menu.config_boton.clicked.connect(self.show_config) #Capta si el boton config fue presionado para ejecutar la funcion show_config
        self.ui_menu.estadistic_boton.clicked.connect(self.show_estadistic) #Capta si el boton estadistic fue presionado para ejecutar la funcion show_estadistic
 
    def show_config(self):
        self.ui_config.setupUi(self) #Funcion que abre configuracion

        self.ui_config.volver_boton.clicked.connect(self.volver) #Capta si el boton volver fue presionado para ejecutar la funcion volver


    def parametros_cf(self):
        self.matriz_datos = MainWindow.extraer(ruta, "matriz") #Actualiza la Matriz para mostrar los dotos del horario.json
        self.limites = MainWindow.extraer(ruta2, "limite") #Actualiza la Lista para mostrar los dotos del limites.json
        self.lm =   [   self.ui_config.lm_grl,
                        self.ui_config.lm_lu, 
                        self.ui_config.lm_mt, 
                        self.ui_config.lm_mc, 
                        self.ui_config.lm_jv, 
                        self.ui_config.lm_vn, 
                        self.ui_config.lm_sb, 
                        self.ui_config.lm_dg
                    ]#lista que tiene los inputs para modificar
        
        for day_idx, day in enumerate(self.lm):  # Usamos enumerate para obtener el índice del input actual (day_idx) y el valor del input actual = day
            day.clear() #limpiamos el input actual = day
            day.setMinimum(-1) #asignamos minimo
            day.setMaximum(10) #asignamos maximo
            self.valor = self.limites[day_idx] #Asigna nombre al dato actual de la lista self.limites
            day.setValue(self.valor) #Muestra el valor antes asignado
            if self.valor == -1:
                day.setSpecialValueText("ilimitado") #si el valor es -1 se le pone el texto "ilimitado"
                    
        self.tm =   [
                        [self.ui_config.grl_tm1, self.ui_config.grl_tm2, self.ui_config.grl_tm3, self.ui_config.grl_tm4, self.ui_config.grl_tm5],   #horarios generales
                        [self.ui_config.lu_tm1, self.ui_config.lu_tm2, self.ui_config.lu_tm3, self.ui_config.lu_tm4, self.ui_config.lu_tm5],        #horarios lunes
                        [self.ui_config.mt_tm1, self.ui_config.mt_tm2, self.ui_config.mt_tm3, self.ui_config.mt_tm4, self.ui_config.mt_tm5],        #horarios martes
                        [self.ui_config.mc_tm1, self.ui_config.mc_tm2, self.ui_config.mc_tm3, self.ui_config.mc_tm4, self.ui_config.mc_tm5],        #horarios miercoles
                        [self.ui_config.jv_tm1, self.ui_config.jv_tm2, self.ui_config.jv_tm3, self.ui_config.jv_tm4, self.ui_config.jv_tm5],        #horarios jueves
                        [self.ui_config.vn_tm1, self.ui_config.vn_tm2, self.ui_config.vn_tm3, self.ui_config.vn_tm4, self.ui_config.vn_tm5],        #horarios viernes
                        [self.ui_config.sb_tm1, self.ui_config.sb_tm2, self.ui_config.sb_tm3, self.ui_config.sb_tm4, self.ui_config.sb_tm5],        #horarios sabado
                        [self.ui_config.dg_tm1, self.ui_config.dg_tm2, self.ui_config.dg_tm3, self.ui_config.dg_tm4, self.ui_config.dg_tm5]         #horarios domingo
                    ] #Matriz que guarda los inputs de horarios por dias
        
        for dia_idx, dia in enumerate(self.tm):   # Usamos enumerate para obtener el índice de la lista actual (dia_idx) y el valor de la lista actual = dia
            for hora_idx, hora in enumerate(dia): # Usamos enumerate para obtener el índice del horario actual (hora_idx) y el valor del horario actual = hora
                hora.clear()  #limpiamos el input actual = day
                hora.setTimeRange(QtCore.QTime(0, 0, 0), QtCore.QTime(23, 59, 59)) #asignamos limites de horario
                self.valor = self.matriz_datos[dia_idx][hora_idx] #Sacamos el valor de horario  de la matriz de datos
                if self.valor == "0:0": #Comparamos si es 0:0 para asignar el texto "--:--"
                    hora.setSpecialValueText("--:--") 
                else:
                    hora.setTime(QtCore.QTime(int(self.valor.split(":")[0]), int(self.valor.split(":")[1]))) #Mostramos en el input el valor guardado en matriz_datos 
        
    def volver(self):
        self.setup_menu() #vinculamos la funcion volver para que muestre el menu principal

    def show_estadistic(self):
        self.ui_estadistic.setupUi(self) #Abre la pagina estadisticas_1
        self.ui_estadistic.boton_volver.clicked.connect(self.volver) #Capta si el boton volver fue presionado para ejecutar la funcion volver
        self.ui_estadistic.boton_mas_estadisticas.clicked.connect(self.show_estadistic_2) #Capta si el boton volver fue presionado para ejecutar la funcion volver

        self.matriz_grafico =   [
                                    [1, 2, 3, 4, 5, 6, 7], 
                                    [1, 0, 1, 3, 2, 4, 3,],
                                    [0, 2, 2, 3, 4, 6, 5,],
                                    [3, 1, 3, 4, 2, 7, 6,]
                                ]
        #Crea los graficos a partir de las clases correspondientes.
        self.grafica = Canvas_grafica(['orange','yellow','green','blue', 'purple'], ['Madrugada', 'Mañana', 'Mediodia', 'Tarde','Noche'], [10, 15, 20, 25, 30], "Horarios de Actividad Promedio")
        self.grafica1 = Canvas_grafica2(['Sobra', 'Falta', 'Justo'], ['green','orange','aqua'], [20,26,54], [0.05, 0.10, 0.05], "Alimento para Pedir Promedio")
        self.grafica2 = Canvas_grafica4(self.matriz_grafico, ["Comida Pedida ", "Comida Programada ", "Comida Habilitada "], ["orange","blue","green"], "Uso del Alimento Diario")
        self.grafica3 = Canvas_grafica(['pink','red','orange','brown', 'grey'], ["Horario 1", "Horario 2", "Horario 3", "Horario 4","Horario 5"], [10, 15, 20, 25, 30], "Horarios de Consumo Promedio")

        # Agrega a cada layouts los graficos correspondientes
        self.ui_estadistic.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic.grafica_tres.addWidget(self.grafica2)
        self.ui_estadistic.grafica_cuatro.addWidget(self.grafica3)
    
    def Buscar_dia(self):
        pass

    def show_estadistic_2(self):
        self.ui_estadistic_2.setupUi(self) #Abre la pagina estadisticas_2
        self.ui_estadistic_2.Volver_inicio.clicked.connect(self.volver) #Capta si el boton volver al inicio fue presionado para ejecutar la funcion volver
        self.ui_estadistic_2.Volver_estadistic.clicked.connect(self.show_estadistic) #Capta si el boton volver estadistic fue presionado para ejecutar la funcion show_estadistic
        
        self.matriz_grafico_2 =   [
                                    [1, 2, 3, 4, 5, 6, 7], 
                                    [1, 0, 1, 3, 2, 4, 3,],
                                    [0, 2, 2, 3, 4, 6, 5,],
                                    [3, 1, 3, 4, 2, 7, 6,]
                                ]
        
        #Crea los graficos a partir de las clases correspondientes.
        self.grafica = Canvas_grafica(['orange','yellow','green','blue', 'purple'], ['Madrugada', 'Mañana', 'Mediodia', 'Tarde','Noche'], [10, 15, 20, 25, 30], "Horarios de Actividad")
        self.grafica1 = Canvas_grafica2(['Sobra', 'Falta', 'Justo'], ['green','orange','aqua'], [20,26,54], [0.05, 0.10, 0.05], "Alimento para Pedir")
        self.grafica3 = Canvas_grafica4(self.matriz_grafico_2, ["Comida Pedida ", "Comida Programada ", "Comida Habilitada "] ,["orange","blue","green"], "hola")

        #Agrega a los layouts los graficos correspondientes
        self.ui_estadistic_2.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic_2.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic_2.grafica_cuatro.addWidget(self.grafica3)    

    def organizar_horarios(self, matriz):
        self.nueva_matriz = [] # Creamos la matriz que vamos a utilizar para devolver los datos ordenados 
        for fila in matriz: 
            self.horarios_validos = [] # Creamos la lista de horarios x dia    
            for horario in fila:
                if horario != "0:0": # Filtrar los horarios válidos (diferentes de "0:0") y convertirlos a minutos
                    horas, minutos = map(int, horario.split(":"))
                    minutos_totales = horas * 60 + minutos #Obtiene los minutos correspondientes al horario
                    self.horarios_validos.append((horario, minutos_totales)) #Agregamos la tupla a la lista de horarios validos 
            
            for i in range(len(self.horarios_validos) - 1): #Ordenar los horarios válidos por minutos
                for j in range(len(self.horarios_validos) - 1 - i): #Generar numero de pasadas necesarias para acomodar
                    #Si el valor de la derecha es mayor que el izquierdo se intercambian
                    if self.horarios_validos[j][1] > self.horarios_validos[j + 1][1]:
                        self.horarios_validos[j], self.horarios_validos[j + 1] = self.horarios_validos[j + 1], self.horarios_validos[j] 

            self.fila_ordenada = [] #Se crea la lista de horarios ordenados del dia
            for horario, minutos in self.horarios_validos:
                self.fila_ordenada.append(horario) #Agregar los horarios de forma ordenada a la lista

            self.fila_ordenada += ["0:0"] * (len(fila) - len(self.fila_ordenada)) #Añade los "0:0" al final de la lista (compara cuantos son los faltantes)

            self.nueva_matriz.append(self.fila_ordenada) #Agrega la lista ordenada a la nueva matriz

        return self.nueva_matriz  # Devolver la nueva matriz ya ordenada

    def enviar_dato(self):
        cg = self.ui_config # Crea un enlace de facil acceso 
        self.limites = [cg.lm_grl.value(), cg.lm_lu.value(), cg.lm_mt.value(), cg.lm_mc.value(), cg.lm_jv.value(), cg.lm_vn.value(), cg.lm_sb.value(), cg.lm_dg.value()]

        self.matriz_datos = [
                                [ str(cg.grl_tm1.time().hour()) + ":" + str(cg.grl_tm1.time().minute()), str(cg.grl_tm2.time().hour()) + ":" + str(cg.grl_tm2.time().minute()), str(cg.grl_tm3.time().hour()) + ":" + str(cg.grl_tm3.time().minute()), str(cg.grl_tm4.time().hour()) + ":" + str(cg.grl_tm4.time().minute()), str(cg.grl_tm5.time().hour()) + ":" + str(cg.grl_tm5.time().minute())],
                                [ str(cg.lu_tm1.time().hour()) + ":" + str(cg.lu_tm1.time().minute()), str(cg.lu_tm2.time().hour()) + ":" + str(cg.lu_tm2.time().minute()), str(cg.lu_tm3.time().hour()) + ":" + str(cg.lu_tm3.time().minute()), str(cg.lu_tm4.time().hour()) + ":" + str(cg.lu_tm4.time().minute()), str(cg.lu_tm5.time().hour()) + ":" + str(cg.lu_tm5.time().minute())],
                                [ str(cg.mt_tm1.time().hour()) + ":" + str(cg.mt_tm1.time().minute()), str(cg.mt_tm2.time().hour()) + ":" + str(cg.mt_tm2.time().minute()), str(cg.mt_tm3.time().hour()) + ":" + str(cg.mt_tm3.time().minute()), str(cg.mt_tm4.time().hour()) + ":" + str(cg.mt_tm4.time().minute()), str(cg.mt_tm5.time().hour()) + ":" + str(cg.mt_tm5.time().minute())],
                                [ str(cg.mc_tm1.time().hour()) + ":" + str(cg.mc_tm1.time().minute()), str(cg.mc_tm2.time().hour()) + ":" + str(cg.mc_tm2.time().minute()), str(cg.mc_tm3.time().hour()) + ":" + str(cg.mc_tm3.time().minute()), str(cg.mc_tm4.time().hour()) + ":" + str(cg.mc_tm4.time().minute()), str(cg.mc_tm5.time().hour()) + ":" + str(cg.mc_tm5.time().minute())],
                                [ str(cg.jv_tm1.time().hour()) + ":" + str(cg.jv_tm1.time().minute()), str(cg.jv_tm2.time().hour()) + ":" + str(cg.jv_tm2.time().minute()), str(cg.jv_tm3.time().hour()) + ":" + str(cg.jv_tm3.time().minute()), str(cg.jv_tm4.time().hour()) + ":" + str(cg.jv_tm4.time().minute()), str(cg.jv_tm5.time().hour()) + ":" + str(cg.jv_tm5.time().minute())],
                                [ str(cg.vn_tm1.time().hour()) + ":" + str(cg.vn_tm1.time().minute()), str(cg.vn_tm2.time().hour()) + ":" + str(cg.vn_tm2.time().minute()), str(cg.vn_tm3.time().hour()) + ":" + str(cg.vn_tm3.time().minute()), str(cg.vn_tm4.time().hour()) + ":" + str(cg.vn_tm4.time().minute()), str(cg.vn_tm5.time().hour()) + ":" + str(cg.vn_tm5.time().minute())],
                                [ str(cg.sb_tm1.time().hour()) + ":" + str(cg.sb_tm1.time().minute()), str(cg.sb_tm2.time().hour()) + ":" + str(cg.sb_tm2.time().minute()), str(cg.sb_tm3.time().hour()) + ":" + str(cg.sb_tm3.time().minute()), str(cg.sb_tm4.time().hour()) + ":" + str(cg.sb_tm4.time().minute()), str(cg.sb_tm5.time().hour()) + ":" + str(cg.sb_tm5.time().minute())],
                                [ str(cg.dg_tm1.time().hour()) + ":" + str(cg.dg_tm1.time().minute()), str(cg.dg_tm2.time().hour()) + ":" + str(cg.dg_tm2.time().minute()), str(cg.dg_tm3.time().hour()) + ":" + str(cg.dg_tm3.time().minute()), str(cg.dg_tm4.time().hour()) + ":" + str(cg.dg_tm4.time().minute()), str(cg.dg_tm5.time().hour()) + ":" + str(cg.dg_tm5.time().minute())]
                            ] # Matriz que guarda los datos de horarios en formato str

        
        self.matriz_datos = self.organizar_horarios(self.matriz_datos) # Organizar los horarios

        
        print("Matriz de datos:", self.matriz_datos) # Imprimir la matriz para verificar

        self.datos = {
            "matriz":self.matriz_datos
        } #Crea diccionario de la matriz
        self.limit = {
            "limite":self.limites
        } #Crea diccionario del limite

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False) #Ingresar diccionario de la matriz al horario.json
            
        with open(ruta2, "w", encoding="utf-8") as archivo:
            json.dump(self.limit, archivo, indent=4, ensure_ascii=False)  #Ingresar diccionario del limite al limite.json

        print(f"Datos guardados en {ruta} y {ruta2}") #Muestra los archivos donde se guarda los diccionarios

    def extraer( ruta, indice): #Metodo que obtiene 
        with open(ruta, "r", encoding="utf-8") as datos:
            objeto = json.load(datos)  
            dato = objeto.get(indice)  # Obtén el valor asociado a la clave 
        return dato     # Retorna el valor obtenido
    
    class Dato_diario():
        pass
        
class Canvas_grafica(FigureCanvas):
    def __init__(self, colores, nombres, tamaño, info, parent=None):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), sharey=True, facecolor='white') 
        super().__init__(self.fig) 

        #Pasa parametros a las variables
        self.colores = colores 
        self.nombres = nombres
        self.tamaño = tamaño

        self.fig.suptitle(info,size=9) #Coloca un titulo sobre el grafico
        self.ax.bar(self.nombres, self.tamaño, color = self.colores) #Aplica los datos dados al grafico


class Canvas_grafica2(FigureCanvas):
    def __init__(self, nombres, colores, tamaño, explotar, info, parent=None):     
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig) 

        #Pasa parametros a las variables
        self.nombres = nombres
        self.colores = colores
        self.tamaño = tamaño
        self.explotar = explotar 

        plt.title(info, color='black', size=9, family="DejaVu Sans") #Coloca un titulo sobre el grafico


        self.ax.pie(self.tamaño, #Aplica % de cada parte
                    explode = self.explotar, #coloca una distancia de sobresalido de las piezas del grafico
                    labels = self.nombres, #Proporciona nombre a cada porcion
                    colors = self.colores, #Proporciona color 
                    autopct = '%1.0f%%', pctdistance = 0.6,
                    shadow=True, startangle=90, radius = 0.8, #Sombra, radio, etc.
                    labeldistance=1.1)  #Distancia del texto respecto la porcion
        self.ax.axis('equal')

class Canvas_grafica4(FigureCanvas):
    def __init__(self, matriz, dato, color, info, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig) 

        self.x  = matriz[0]
        self.y1 = matriz[1]
        self.y2 = matriz[2]
        self.y3 = matriz[3]

        self.y = np.vstack([self.y1, self.y2, self.y3])

        self.labels = [dato[0], dato[1], dato[2]]
        self.color = color

        self.ax.stackplot(self.x, self.y1, self.y2, self.y3, labels=self.labels,colors=self.color)
        self.ax.legend(loc='upper left')
        self.ax.stackplot(self.x, self.y)
        self.fig.suptitle(info,size=9)


if __name__ == "__main__":  # Entry point check
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    ruta = "horario.json"
    ruta2 = "limite.json"
    sys.exit(app.exec_())  # Start the application loop
    
    