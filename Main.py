import sys
import json
import config
import Ui_menu
import comunicacion
from Graficos import*
import Ui_configuracion
import Ui_estadisticas_1
import Ui_estadisticas_2
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):  # Main window class inherited from QMainWindow
    def __init__(self):  # Constructor
        super().__init__()
        self.ui_menu = Ui_menu.Ui_MainWindow()  #facilita la coneccion con Ui_menu
        self.ui_config = Ui_configuracion.Ui_MainWindow()  #facilita la coneccion con Ui_configuracion
        self.ui_estadistic = Ui_estadisticas_1.Ui_MainWindow() #facilita la coneccion con Ui_estadisticas_1
        self.ui_estadistic_2 = Ui_estadisticas_2.Ui_MainWindow() #facilita la coneccion con Ui_estadisticas_2
        self.setup_menu() #Inicia la pagina Menu

        self.showFullScreen() #Adapta a pantalla completa
        self.arduino = comunicacion.conexion_arduino()

    #Método que abre el Menu
    def setup_menu(self):
        self.ui_menu.setupUi(self) 
        self.ui_menu.config_boton.clicked.connect(self.show_config) #Capta si el boton config fue presionado para ejecutar la funcion show_config
        self.ui_menu.estadistic_boton.clicked.connect(self.show_estadistic) #Capta si el boton estadistic fue presionado para ejecutar la funcion show_estadistic

    #Muestra nuevamente el menu
    def volver(self):
        self.setup_menu() #vinculamos la funcion volver para que muestre el menu principal

    #Método que abre Ui_configuracion.py
    def show_config(self):
        self.ui_config.setupUi(self) 
        self.ui_config.volver_boton.clicked.connect(self.volver) #Capta si el boton volver fue presionado para ejecutar la funcion volver

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

        
        self.matriz_datos = config.organizar_horarios(self.matriz_datos) # Organizar los horarios

        self.general = comunicacion.convertir_matriz(self.matriz_datos)

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

        self.mensaje = f"{comunicacion.miliseg_week()},{5}," + ",".join(map(str, comunicacion.convertir_matriz()))

        # Intentar enviar los datos al Arduino
        try:
            self.arduino.write(f"{self.mensaje}\n".encode())
            print(f"Enviando datos: {self.mensaje}")
        except comunicacion.serial.SerialException as e:
            print(f"Error al intentar enviar datos al Arduino: {e}")

    """# Leer el contador enviado por Arduino
        while True:
            try:
                if self.arduino.in_waiting > 0:
                    mensaje = self.arduino.readline().decode('utf-8').strip()
                    
                    # Si el mensaje contiene el contador
                    if "Contador del sensor:" in mensaje:
                        contador = mensaje.split(":")[1].strip()
                        print(f"Contador del sensor: {contador}")
            except comunicacion.serial.SerialException as e:
                print(f"Error al leer datos del Arduino: {e}")
            
            comunicacion.time.sleep(1)
        self.arduino.close()"""

    #Metodo que obtiene datos de los archivos .json
    def extraer(ruta, indice): 
        with open(ruta, "r", encoding="utf-8") as datos:
            objeto = json.load(datos)  
            dato = objeto.get(indice)  # Obtén el valor asociado a la clave 
        return dato     # Retorna el valor obtenido
    
    #Otorga restricciones y parametros a Ui_configuracion.py
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

    #Muestra Ui_estadisticas_1.py
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
    
    #Muestra Ui_estadisticas_2.py
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
    
    def Buscar_dia(self):
        pass
    

if __name__ == "__main__":  #Verifica si es el main
    app = QApplication(sys.argv)
    window = MainWindow() #Se crea objeto de la clase MainWindow
    window.show()  # Se muestra la ventana

    #Se establecen rutas de acceso a los archivos ".json"
    ruta = "horario.json" 
    ruta2 = "limite.json"

    sys.exit(app.exec_())