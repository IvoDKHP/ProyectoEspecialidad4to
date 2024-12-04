import sys
import json
import time
import config
import Ui_menu
import comunicacion
import comunicacion_1
import Graficos
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
        self.dia1 = Day_report([3600000, 11820000, 32300000, 48660000, 70080000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        self.dia2 = Day_report([3900000, 13320000, 11100000, 42080000, 65980000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        self.dia3 = Day_report([4200000, 15320000, 32700000, 41080000, 57980000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        self.dia4 = Day_report([5000000, 16820000, 9400000, 48010000, 71710000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        self.dia5 = Day_report([5700000, 16720000, 129700000, 10180000, 30880000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        self.dia6 = Day_report([7000000, 11820000, 40000000, 42780000, 71880000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        self.dia7 = Day_report([7800000, 18420000, 43200000, 12180000, 71880000, 83520000], 10, [3630000, 9800000, 3890000, 1840000, 71800000, 83520000], 6 )
        
        self.arduino = comunicacion.conexion_arduino()

        self.showFullScreen() #Adapta a pantalla completa
        

    #Método que abre el Menu
    def setup_menu(self):
        self.ui_menu.setupUi(self) 
        self.ui_menu.config_boton.clicked.connect(self.show_config) #Capta si el boton config fue presionado para ejecutar la funcion show_config
        self.ui_menu.estadistic_boton.clicked.connect(self.show_estadistic) #Capta si el boton estadistic fue presionado para ejecutar la funcion show_estadistic
        self.ui_menu.salir_boton.clicked.connect(self.cerrar_app)
    #Muestra nuevamente el menu

    def cerrar_app(self):
        QApplication.quit()
    def volver(self):
        self.setup_menu() #vinculamos la funcion volver para que muestre el menu principal
        Graficos.plt.close("all")

    #Método que abre Ui_configuracion.py
    def show_config(self):
        self.ui_config.setupUi(self)
        Graficos.plt.close("all")
        self.matriz_datos = MainWindow.extraer(ruta, "matriz") #Actualiza la Matriz para mostrar los dotos del horario.json
        self.limites = MainWindow.extraer(ruta2, "limite") #Actualiza la Lista para mostrar los dotos del limites.json
        self.ui_config.volver_boton.clicked.connect(self.volver) #Capta si el boton volver fue presionado para ejecutar la funcion volver

    def enviar_dato(self):
        #self.arduino = comunicacion.conexion_arduino()
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

        #self.ard_lm = config.organizar_limites(self.limites)

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
        self.lista_pa = comunicacion.convertir_matriz(self.matriz_datos, "limite")
        print(comunicacion.convertir_matriz(self.matriz_datos, "limite"))
        self.lista_hr = comunicacion.convertir_matriz(self.matriz_datos, "horarios")
        print(comunicacion.convertir_matriz(self.matriz_datos, "horarios"))
        self.lista_lm = comunicacion.convertir_limites(self.limites)
        print(comunicacion.convertir_limites(self.limites))

        self.lg_lm = len(comunicacion.convertir_matriz(self.matriz_datos, "limite"))
        self.lg_hr = len(comunicacion.convertir_matriz(self.matriz_datos, "horarios"))

        ################################################################

        try:
            # Envía el número al Arduino
            self.mensaje = f"{comunicacion.miliseg_week()}\n"
            self.arduino.write(self.mensaje.encode())  # Convierte el mensaje a bytes y envía
            print(f"Tiempo enviado: {comunicacion.miliseg_week()}")
            # Espera a recibir la confirmación del Arduino

            self.mensaje = f"{self.lg_lm}\n"
            self.arduino.write(self.mensaje.encode())  # Convierte el mensaje a bytes y envía
            print(f"largo de on-off enviado: {self.lg_lm}")

            self.mensaje = f"{self.lg_hr}\n"
            self.arduino.write(self.mensaje.encode())  # Convierte el mensaje a bytes y envía
            print(f"largo de horarios: {self.lg_hr}")

            mensaje_dato = f"{0}\n"
            self.arduino.write(mensaje_dato.encode())
            print("Lista 1 activada...")
            time.sleep(0.05)
            print(self.lista_pa)
            for dato in self.lista_pa:
                mensaje_dato = f"{dato}\n"
                self.arduino.write(mensaje_dato.encode())
                print(f"Dato enviado: {dato}")
                time.sleep(0.05)

            mensaje_dato = f"{0}\n"
            self.arduino.write(mensaje_dato.encode())
            print("Lista 2 activada...")
            time.sleep(0.05)

            print(self.lista_hr)
            for dato in self.lista_hr:
                mensaje_dato = f"{dato}\n"
                self.arduino.write(mensaje_dato.encode())
                print(f"Dato enviado: {dato}")
                time.sleep(0.05)

            mensaje_dato = f"{0}\n"
            self.arduino.write(mensaje_dato.encode())
            print("Lista 3 activada...")
            time.sleep(0.05)
            for dato in self.lista_lm:
                mensaje_dato = f"{dato}\n"
                self.arduino.write(mensaje_dato.encode())
                print(f"Dato enviado: {dato}")
                time.sleep(0.05)

            """while True:
                time.sleep(0.1)  # Pausa de 100 ms para evitar consumir demasiados recursos
                if self.arduino.in_waiting > 0:  # Comprueba si hay datos en el búfer
                    respuesta = self.arduino.readline().decode().strip()  # Lee, decodifica y limpia el mensaje
                    print(f"Respuesta del Arduino: {respuesta}")
                else: 
                    self.arduino.close()
                    break"""


        except KeyboardInterrupt:
            print("Interrumpido por el usuario.")

        ############################################################
        
            

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
        self.matriz_prom1 = [comunicacion_1.reports[-1].Disponible()[2], 
                             comunicacion_1.reports[-2].Disponible()[2], 
                             comunicacion_1.reports[-3].Disponible()[2], 
                             comunicacion_1.reports[-4].Disponible()[2], 
                             comunicacion_1.reports[-5].Disponible()[2], 
                             comunicacion_1.reports[-6].Disponible()[2], 
                             comunicacion_1.reports[-7].Disponible()[2]]
        
        self.matriz_prom2 = [comunicacion_1.reports[-1].Disponible()[3], 
                             comunicacion_1.reports[-2].Disponible()[3], 
                             comunicacion_1.reports[-3].Disponible()[3], 
                             comunicacion_1.reports[-4].Disponible()[3], 
                             comunicacion_1.reports[-5].Disponible()[3], 
                             comunicacion_1.reports[-6].Disponible()[3], 
                             comunicacion_1.reports[-7].Disponible()[3]]
        
        self.mtz_prom =    [comunicacion_1.reports[-1].zn_horaria(), 
                             comunicacion_1.reports[-2].zn_horaria(), 
                             comunicacion_1.reports[-3].zn_horaria(), 
                             comunicacion_1.reports[-4].zn_horaria(), 
                             comunicacion_1.reports[-5].zn_horaria(), 
                             comunicacion_1.reports[-6].zn_horaria(), 
                             comunicacion_1.reports[-7].zn_horaria()]
        
        self.mtz_porcent =  [comunicacion_1.reports[-1].calcular_porcentajes(), 
                             comunicacion_1.reports[-2].calcular_porcentajes(), 
                             comunicacion_1.reports[-3].calcular_porcentajes(), 
                             comunicacion_1.reports[-4].calcular_porcentajes(), 
                             comunicacion_1.reports[-5].calcular_porcentajes(), 
                             comunicacion_1.reports[-6].calcular_porcentajes(), 
                             comunicacion_1.reports[-7].calcular_porcentajes()]


        self.matriz_grafico =   [
                                    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                                    [0,0,0,0,1,2,2,3,4, 6, 8, 8,10, 9, 7, 6, 4, 4, 6, 6, 8,10, 8, 4],
                                    comunicacion_1.promedio_indice(self.matriz_prom1),
                                    comunicacion_1.promedio_indice(self.matriz_prom2)
                                ]
        self.list_datos = [1,2,10,4,5]
        
        #Crea los graficos a partir de las clases correspondientes.
        self.grafica = Graficos.Canvas_grafica(['orange','yellow','green','blue', 'purple'], ['Madrugada', 'Mañana', 'Mediodia', 'Tarde','Noche'], comunicacion_1.promedio_indice(self.mtz_prom), "Horarios de Actividad Promedio")
        self.grafica1 = Graficos.Canvas_grafica2(['Sobra', 'Falta', 'Justo'], ['green','orange','aqua'], comunicacion_1.promedio_indice(self.mtz_porcent), [0.05, 0.10, 0.05], "Alimento para Pedir Promedio")
        self.grafica2 = Graficos.Canvas_grafica4(self.matriz_grafico, ["Comida estimada ", "Comida Pedida ", "Comida Habilitada "], ["orange","blue","green"], "Uso del Alimento Diario")
        self.grafica3 = Graficos.Canvas_grafica(['pink','red','orange','brown', 'grey'], ["Horario 1", "Horario 2", "Horario 3", "Horario 4","Horario 5"], self.list_datos, "Horarios de Consumo Promedio")

        # Agrega a cada layouts los graficos correspondientes
        self.ui_estadistic.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic.grafica_tres.addWidget(self.grafica2)
        self.ui_estadistic.grafica_cuatro.addWidget(self.grafica3)
    
    #Muestra Ui_estadisticas_2.py
    def show_estadistic_2(self):

        self.ui_estadistic_2.setupUi(self) #Abre la pagina estadisticas_2
        self.parametros_estad2(comunicacion_1.reports[1].pedido,"6")
        self.ui_estadistic_2.Volver_inicio.clicked.connect(self.volver) #Capta si el boton volver al inicio fue presionado para ejecutar la funcion volver
        self.ui_estadistic_2.Volver_estadistic.clicked.connect(self.show_estadistic) #Capta si el boton volver estadistic fue presionado para ejecutar la funcion show_estadistic
        #Crea los graficos a partir de las clases correspondientes.
        self.grafica = Graficos.Canvas_grafica(['orange','yellow','green','blue', 'purple'], ['Madrugada', 'Mañana', 'Mediodia', 'Tarde','Noche'], comunicacion_1.reports[1].zn_horaria(), "Horarios de Actividad")
        self.grafica1 = Graficos.Canvas_grafica2(['Sobra', 'Falta', 'Justo'], ['green','orange','aqua'], comunicacion_1.reports[1].calcular_porcentajes(), [0.05, 0.10, 0.05], "Alimento para Pedir")
        self.grafica3 = Graficos.Canvas_grafica4(comunicacion_1.reports[1].Disponible(), ["Comida estimada ", "Comida Pedida ", "Comida Habilitada "] ,["orange","blue","green","red"], "hola")

        #Agrega a los layouts los graficos correspondientes
        self.ui_estadistic_2.grafica_uno.addWidget(self.grafica)
        self.ui_estadistic_2.grafica_dos.addWidget(self.grafica1)
        self.ui_estadistic_2.grafica_cuatro.addWidget(self.grafica3)   

    def parametros_estad2(self, lista, lm):
        self.lista_hrs = lista
        self.ui_estadistic_2.Horario_1.setText(lista[0])
        self.ui_estadistic_2.Horario_2.setText(lista[1])
        self.ui_estadistic_2.Horario_3.setText(lista[2])
        self.ui_estadistic_2.Horario_4.setText(lista[3])
        self.ui_estadistic_2.Horario_5.setText(lista[4])
        self.ui_estadistic_2.Limite.setText(lm)

    
    def Buscar_dia(self):
        self.fecha_str = 0
        self.reportes = comunicacion_1.reports
        self.fecha_str = (self.ui_estadistic_2.Fecha.date().toString("yyyy-MM-dd"))
        try:
            print(self.fecha_str)
        except:
            pass

        fecha = datetime.strptime(self.fecha_str, "%d-%m-%Y")
        # Buscar en la lista de reportes
        for reporte in self.reportes:
            if reporte.date.date() == fecha.date():
                return reporte
        # Si no se encuentra, devolver None o un mensaje de error
        return None
        


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
