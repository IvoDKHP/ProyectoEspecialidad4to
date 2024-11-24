import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

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

        #Asignar datos de longitud y latitud xd
        self.x  = matriz[0]
        self.y1 = matriz[1]
        self.y2 = matriz[2]
        self.y3 = matriz[3]
        self.y = np.vstack([self.y1, self.y2, self.y3]) #formar "y" matriz a partir de las listas y1, y2 e y3
        self.labels = [dato[0], dato[1], dato[2]] #Agregar etiquetas a cada variable
        self.color = color #Identificar colores asignados

        #Aplicar graficos con datos ingresados
        self.ax.stackplot(self.x, self.y1, self.y2, self.y3, labels=self.labels,colors=self.color) 
        self.ax.legend(loc='upper left')
        self.ax.stackplot(self.x, self.y)
        self.fig.suptitle(info,size=9) #Agrega subtitulo al grafico
