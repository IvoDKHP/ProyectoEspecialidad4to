"""import sys
import json
import time
import config
import Ui_menu"""
import datetime
import comunicacion
import Ui_configuracion
import Ui_estadisticas_1
import Ui_estadisticas_2

from datetime import datetime, timedelta

# Definición de la clase Day_report
class Day_report:
    def __init__(self, date: datetime, horarios, limite, pedido, cantidad):
        self.date = date          # Fecha del reporte
        self.horarios = horarios  # Lista de horarios
        self.limite = limite      # Valor entero para límite
        self.pedido = pedido      # Lista de pedidos
        self.cantidad = cantidad  # Valor entero para cantidad
        self.report = f"Reporte para {date.strftime('%A, %B %d, %Y')}"

    def zn_horaria(self):

        self.zn_hora = [0,0,0,0,0]
        for i in self.pedido:
            a = comunicacion.convertir_a_millis(i)
            if a%1440 < 200:
                self.zn_hora[0] += 1
            elif a%1440 < 400:
                self.zn_hora[1] += 1
            elif a%1440 < 840:
                self.zn_hora[2] += 1
            elif a%1440 < 1140:
                self.zn_hora[3] += 1
            else:
                self.zn_hora[4] += 1
        return self.zn_hora

    def calcular_porcentajes(self):
        # Validar para evitar divisiones por cero
        veces_habilitadas = self.limite
        veces_pedidas = self.cantidad
        if veces_habilitadas == 0:
            return {"error": "Las veces habilitadas no pueden ser 0."}

        # Inicializamos las variables
        porcentaje_sobra = 0
        porcentaje_falta = 0
        porcentaje_justo = 0

        # Determinar si hay sobra, falta o acierto
        if veces_pedidas < veces_habilitadas:
            # Hay sobra, necesitamos porciones faltantes
            porciones_faltantes = veces_habilitadas - veces_pedidas
            porcentaje_sobra = (porciones_faltantes / veces_habilitadas) * 100
            porcentaje_falta = 0  # No hay falta si hay sobra
        elif veces_pedidas > veces_habilitadas:
            # Hay falta, necesitamos porciones sobrantes
            porciones_sobrantes = veces_pedidas - veces_habilitadas
            porcentaje_falta = (porciones_sobrantes / veces_habilitadas) * 100
            porcentaje_sobra = 0  # No hay sobra si hay falta
        else:
            # No hay sobra ni falta, todo fue justo
            porcentaje_sobra = 0
            porcentaje_falta = 0
            porcentaje_justo = 100

        # Porcentaje de acierto (lo que no es ni sobra ni falta)
        porcentaje_justo = 100 - (porcentaje_sobra + porcentaje_falta)

        return  [
                round(porcentaje_sobra, 2),
                round(porcentaje_falta, 2),
                round(porcentaje_justo, 2)
                ]
    def Disponible(self):
        self.habilitado = []
        for i in range(24):
            self.habilitado.append(self.limite)
        self.lista_horarios = self.pedido
        # Inicializar lista de 24 elementos en 0
        self.necesitado = [0] * 24

        # Asignar valores según la posición en la lista de horarios
        for idx, horario in enumerate(self.lista_horarios, start=1):
            if 0 <= comunicacion.convertir_a_millis(horario) // 60 < 24:  # Validar que el horario esté en el rango válido
                # Aquí sumamos la ración correspondiente a la posición en 'necesitado'
                # Suponiendo que la "ración" que se debe agregar es el valor del índice (idx) o algún valor asociado:
                self.necesitado[(comunicacion.convertir_a_millis(horario) // 60)] += idx

        self.matriz = [ [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                        [0,0,0,0,1,2,2,3,4, 6, 8, 8,10, 9, 7, 6, 4, 4, 6, 6, 8,10, 8, 4],
                        self.necesitado,
                        self.habilitado ]
        return self.matriz
    
    def __str__(self):
        horarios_str = ', '.join(self.horarios)  # Convertir lista de horarios a string
        pedido_str = ', '.join(self.pedido)      # Convertir lista de pedidos a string
        return (f"{self.report}\n"
                f"Horarios: {horarios_str}, Límite: {self.limite}, "
                f"Pedido(s): {pedido_str}, Cantidad: {self.cantidad}")


# Función para crear los reportes con fecha y datos adicionales
def create_day_reports(start_date: str, num_days: int, data_matrix):
    # Convertir la fecha de inicio de formato string a datetime
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")  # Usamos datetime.strptime()
    
    # Lista para almacenar los objetos Day_report
    reports = []
    
    # Crear un objeto Day_report para cada día
    for i in range(num_days):
        # Calcular la fecha de cada día
        day = start_date_obj + timedelta(days=i)
        
        # Obtener los datos de la matriz para el día actual
        horarios, limite, pedido, cantidad = data_matrix[i]
        
        # Crear un objeto Day_report con la fecha y los datos de la matriz
        day_report = Day_report(day, horarios, limite, pedido, cantidad)
        reports.append(day_report)  # Añadir el reporte a la lista
    
    return reports

def sectorizar_lista(horarios):
    matriz = []  # Matriz para almacenar las sublistas
    sublista = []  # Sublista temporal para almacenar valores consecutivos

    for i in range(len(horarios)):
        # Si la sublista está vacía o el valor actual es mayor o igual al anterior, lo agregamos a la sublista
        if not sublista or horarios[i] >= horarios[i - 1]:
            sublista.append(horarios[i])
        else:
            # Si el valor actual es menor al anterior, finalizamos la sublista actual y comenzamos una nueva
            matriz.append(sublista)
            sublista = [horarios[i]]  # Comenzamos una nueva sublista

    # Añadir la última sublista si no está vacía
    if sublista:
        matriz.append(sublista)

    return matriz

def convertir_a_horario(ms):
    horas, minutos = divmod(ms // 60000, 60)
    return f"{horas:02}:{minutos:02}"

def construir_data_matrix(matriz_hr, matriz_pd, limite, cantidad):
    data_matrix = []
    for i in range(len(matriz_hr)):
        # Convertir horarios y pedidos a formato de tiempo
        horarios_str = [convertir_a_horario(h) for h in matriz_hr[i]]
        pedidos_str = [convertir_a_horario(p) for p in matriz_pd[i]]

        # Construir el grupo con los datos correspondientes
        grupo = [horarios_str, limite[i], pedidos_str, cantidad[i]]
        data_matrix.append(grupo)

    return data_matrix

def transformar_a_minutos_totales(lista_horarios):
    """
    Transforma una lista de horarios en formato "HH:MM" a una lista con los minutos totales desde el inicio del día.
    
    Args:
        lista_horarios (list): Lista de horarios como cadenas en formato "HH:MM".
        
    Returns:
        list: Lista de números enteros representando los minutos totales.
    """
    minutos_totales = []
    for horario in lista_horarios:
        horas, minutos = map(int, horario.split(":"))  # Divide "HH:MM" y convierte HH y MM en enteros
        total_minutos = horas * 60 + minutos          # Calcula minutos totales
        minutos_totales.append(total_minutos)
    return minutos_totales

def calcular_restos(lista, divisor=86400000):
    return [valor % divisor for valor in lista]

def promedio_indice(matriz):
    
    longitud_maxima = max(len(fila) for fila in matriz)
    
    # Completar las listas más cortas con ceros
    matriz_completada = [
        fila + [0] * (longitud_maxima - len(fila)) for fila in matriz
    ]
    
    num_listas = len(matriz)
    
    # Calculamos el promedio por índice
    promedios = []
    for i in range(longitud_maxima):
        suma = sum(fila[i] for fila in matriz_completada)
        promedios.append(round(suma / num_listas, 2))
    
    return promedios


# Lista original de horarios
"""Horarios = [2700000, 10800000, 92700000, 97200000, 175500000, 183600000, 10800000, 92700000, 97200000, 175500000, 183600000]
long_hr = [3, 2]
limite = [1 ,2]
Pedidos = [92700000, 97200000, 175500000, 1212000, 12222000]
cantidad = [12 ,17]
# Llamada a la función para sectorizar la lista
print(calcular_restos(Horarios))
matriz_hr = sectorizar_lista(Horarios)
matriz_pd = sectorizar_lista(Pedidos)

# Construir la data_matrix
data_matrix = construir_data_matrix(matriz_hr, matriz_pd, limite, cantidad)

# Imprimir la data_matrix
for grupo in data_matrix:
    print(grupo)
"""

data_matrix = [
    [["01:00", "02:00", "03:00"], 10, ["11:00", "12:30", "23:00", "22:30"], 20],
    [["04:00", "05:00", "06:00"], 20, ["12:00", "12:30", "21:00", "22:40", "23:40"],  3],
    [["07:00", "08:00", "09:00"], 15, ["15:00", "12:30", "22:00", "22:30"], 25],
    [["10:00", "11:00", "12:00"], 17, ["14:00", "12:30", "23:00"],          15],
    [["13:00", "14:00", "15:00"], 12, ["13:00", "12:30", "20:00"],          10],
    [["01:00", "02:00", "03:00"], 10, ["01:00", "12:30", "14:00", "22:00"], 20],
    [["04:00", "05:00", "06:00"], 12, ["05:30", "12:30", "15:00", "22:00"], 13],
    [["07:00", "08:00", "09:00"], 15, ["09:30", "12:30", "16:00"],          15]
]

# Crear los reportes a partir de la fecha de inicio y la cantidad de días
reports = create_day_reports(comunicacion.generate_day_string(), len(data_matrix), data_matrix)

"""matriz_prom1 = [    reports[-1].Disponible()[-2], 
                    reports[-2].Disponible()[-2], 
                    reports[-3].Disponible()[-2], 
                    reports[-4].Disponible()[-2], 
                    reports[-5].Disponible()[-2], 
                    reports[-6].Disponible()[-2], 
                    reports[-7].Disponible()[-2]]
        
matriz_prom2 = [    reports[-1].Disponible()[3], 
                    reports[-2].Disponible()[3], 
                    reports[-3].Disponible()[3], 
                    reports[-4].Disponible()[3], 
                    reports[-5].Disponible()[3], 
                    reports[-6].Disponible()[3], 
                    reports[-7].Disponible()[3]]

promedio_indice(matriz_prom1)
promedio_indice(matriz_prom2)

matriz_grafico =   [
                            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                            [0,0,0,0,1,2,2,3,4, 6, 8, 8,10, 9, 7, 6, 4, 4, 6, 6, 8,10, 8, 4],
                            promedio_indice(matriz_prom1),
                            promedio_indice(matriz_prom2)
                        ]

print(matriz_grafico)"""