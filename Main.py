import sys
import json
import config
import Ui_menu
import comunicacion
import Graficos_Estadistic as Graficos
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
        self.dia1 = Day_report([3600000, 11820000, 38700000, 48180000, 71880000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )


        self.showFullScreen() #Adapta a pantalla completa
        #self.arduino = comunicacion.conexion_arduino()

    #Método que abre el Menu
    def setup_menu(self):
        self.ui_menu.setupUi(self) 
        self.ui_menu.config_boton.clicked.connect(self.show_config) #Capta si el boton config fue presionado para ejecutar la funcion show_config
        self.ui_menu.estadistic_boton.clicked.connect(self.show_estadistic) #Capta si el boton estadistic fue presionado para ejecutar la funcion show_estadistic

    #Muestra nuevamente el menu
    def volver(self):
        self.setup_menu() #vinculamos la funcion volver para que muestre el menu principal
        Graficos.plt.close("all")

    #Método que abre Ui_configuracion.py
    def show_config(self):
        self.ui_config.setupUi(self)
        Graficos.plt.close("all")
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

        self.ard_lm = config.organizar_limites(self.limites)

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
        self.lg_lm = str(len(comunicacion.convertir_matriz(self.matriz_datos, "limite")))
        self.lg_hr = str(len(comunicacion.convertir_matriz(self.matriz_datos, "horarios")))

        self.mensaje = f"{comunicacion.miliseg_week()}, {self.lg_lm}, {self.lg_hr}" + ",".join(map(str, self.ard_lm)) + "," + ",".join(map(str, comunicacion.convertir_matriz(self.matriz_datos, "limite"))) + "," + ",".join(map(str, comunicacion.convertir_matriz(self.matriz_datos, "horarios")))

        print(self.mensaje)
        """
        self.arduino.write(comunicacion.miliseg_week())
        self.arduino.write((self.lg_lm))
        self.arduino.write((self.lg_hr))
        for value in comunicacion.convertir_matriz(self.matriz_datos, "limite"):
            self.arduino.write(f"{value}".encode()+b"\n")

        for value in comunicacion.convertir_matriz(self.matriz_datos, "horarios"):
            self.arduino.write(f"{value}".encode()+b"\n")"""
            

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
                                    [5, 4, 2, 3, 2, 7, 3,],
                                    [10, 2, 9, 3, 4, 4, 5,],
                                    [3, 1, 3, 8, 2, 7, 6,]
                                ]
        #Crea los graficos a partir de las clases correspondientes.
        self.grafica = Graficos.Canvas_grafica(['orange','yellow','green','blue', 'purple'], ['Madrugada', 'Mañana', 'Mediodia', 'Tarde','Noche'], [28, 32, 2, 25, 13], "Horarios de Actividad Promedio")
        self.grafica1 = Graficos.Canvas_grafica2(['Sobra', 'Falta', 'Justo'], ['green','orange','aqua'], [20,26,54], [0.05, 0.10, 0.05], "Alimento para Pedir Promedio")
        self.grafica2 = Graficos.Canvas_grafica4(self.matriz_grafico, ["Comida Pedida ", "Comida Programada ", "Comida Habilitada "], ["orange","blue","green"], "Uso del Alimento Diario")
        self.grafica3 = Graficos.Canvas_grafica(['pink','red','orange','brown', 'grey'], ["Horario 1", "Horario 2", "Horario 3", "Horario 4","Horario 5"], [18, 15, 30, 15, 38], "Horarios de Consumo Promedio")

        # Agrega a cada layouts los graficos correspondientes
        self.ui_estadistic.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic.grafica_tres.addWidget(self.grafica2)
        self.ui_estadistic.grafica_cuatro.addWidget(self.grafica3)
    
    #Muestra Ui_estadisticas_2.py
    def show_estadistic_2(self):

        self.ui_estadistic_2.setupUi(self) #Abre la pagina estadisticas_2
        self.parametros_estad2("1","2","3","4","5","6")
        self.ui_estadistic_2.Volver_inicio.clicked.connect(self.volver) #Capta si el boton volver al inicio fue presionado para ejecutar la funcion volver
        self.ui_estadistic_2.Volver_estadistic.clicked.connect(self.show_estadistic) #Capta si el boton volver estadistic fue presionado para ejecutar la funcion show_estadistic
        
        self.lista = self.dia1.Pedido_lim()
        self.lista.pop()
        #Crea los graficos a partir de las clases correspondientes.
        self.grafica = Graficos.Canvas_grafica(['orange','yellow','green','blue', 'purple'], ['Madrugada', 'Mañana', 'Mediodia', 'Tarde','Noche'], self.dia1.zn_horaria(), "Horarios de Actividad")
        self.grafica1 = Graficos.Canvas_grafica2(['Sobra', 'Falta', 'Justo'], ['green','orange','aqua'], self.lista, [0.05, 0.10, 0.05], "Alimento para Pedir")
        self.grafica3 = Graficos.Canvas_grafica4(self.dia1.Disponible(), ["Comida Pedida ", "Comida Programada ", "Comida Habilitada "] ,["orange","blue","green"], "hola")

        #Agrega a los layouts los graficos correspondientes
        self.ui_estadistic_2.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic_2.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic_2.grafica_cuatro.addWidget(self.grafica3)   

    def parametros_estad2(self, hr1, hr2, hr3, hr4, hr5, lm):
        self.ui_estadistic_2.Horario_1.setText(hr1)
        self.ui_estadistic_2.Horario_2.setText(hr2)
        self.ui_estadistic_2.Horario_3.setText(hr3)
        self.ui_estadistic_2.Horario_4.setText(hr4)
        self.ui_estadistic_2.Horario_5.setText(hr5)
        self.ui_estadistic_2.Limite.setText(lm)
        


    
    def Buscar_dia(self):
        self.Fecha = (self.ui_estadistic_2.Fecha.date().toString("yyyy-MM-dd"))
        try:
            self.Fecha
        except:
            pass


class Day_report():
    def __init__(self, horarios, limite, pedido, cantidad):
        self.horarios = horarios
        self.limite = limite
        self.pedido = pedido
        self.cantidad = cantidad
        
    def zn_horaria(self):
        self.zn_hora = [0,0,0,0,0]
        for i in self.pedido:
            if i%86400000 < 18000000:
                self.zn_hora[0] += 1
            elif i%86400000 < 36000000:
                self.zn_hora[1] += 1
            elif i%86400000 < 50400000:
                self.zn_hora[2] += 1
            elif i%86400000 < 68400000:
                self.zn_hora[3] += 1
            else:
                self.zn_hora[4] += 1
        return self.zn_hora
        
    def Pedido_lim(self):
        self.falta = 0
        self.justo = 0
        self.sobra = 0
        self.div = self.cantidad / self.limite
        if self.div > 1:
            self.falta = self.cantidad*100/self.limite
            self.justo = 100 - self.falta 
            self.x = -1
        elif self.div < 1:
            self.sobra = self.cantidad*100/self.limite
            self.justo = 100 - self.sobra
            self.x = 1
        else:
            self.justo = 100
            self.x = 0
        self.porcent = [self.justo, self.falta, self.sobra, self.x]
        return self.porcent

    def Disponible(self):
        self.habilitado = []
        for i in range(7):
            self.habilitado.append(self.limite + len(self.horarios))
        self.utilizado = []
        if self.limite - self.cantidad > 0:
            for i in range(7):
                if self.cantidad > sum(self.utilizado) and i != 7:
                    self.utilizado.append(1)
                elif i == 7:
                    self.utilizado.append(self.cantidad - sum(self.utilizado))
        elif self.limite - self.cantidad < 0:
            for i in range(7):
                if self.limite > sum(self.utilizado) and i != 7:
                    self.utilizado.append(1)
                elif i == 7:
                    self.utilizado.append(self.limite - sum(self.utilizado))
        else:
            for i in range(7):
                if self.limite > sum(self.utilizado) and i != 7:
                    self.utilizado.append(1)
                elif i == 7:
                    self.utilizado.append(self.limite - sum(self.utilizado))
        
        self.utilizado.append(self.limite - self.cantidad)
        self.necesitado = []
        self.necesitado = self.zn_horaria()
        self.necesitado.append(0)
        self.necesitado.append(0)
        self.matriz = [ [1,2,3,4,5,6,7],
                        self.utilizado,
                        self.necesitado,
                        self.habilitado ]
        return self.matriz

if __name__ == "__main__":  #Verifica si es el main
    app = QApplication(sys.argv)
    window = MainWindow() #Se crea objeto de la clase MainWindow
    window.show()  # Se muestra la ventana

    #Se establecen rutas de acceso a los archivos ".json"
    ruta = "horario.json" 
    ruta2 = "limite.json"

    sys.exit(app.exec_())
