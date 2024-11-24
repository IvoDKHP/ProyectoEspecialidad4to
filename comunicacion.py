import serial
import time
from datetime import datetime

# Configura el puerto serie
def conexion_arduino():
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 por tu puerto
    time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice
    return arduino

# Función para convertir hora:minuto a milisegundos
def convertir_a_millis(hora_minuto):
    horas, minutos = map(int, hora_minuto.split(":"))  # Separar y convertir a enteros
    total_segundos = horas * 3600 + minutos * 60  # Calcular el total de segundos
    return total_segundos * 1000  # Convertir a milisegundos

def convertir_matriz(matriz):
    lista_horarios = []
    for dia in matriz:
        for horario in dia:
            if horario != "0:0":
                miliseg = convertir_a_millis(horario)
                if dia == matriz[0]:
                    for hora_grl in range(7):
                        lista_horarios.append(miliseg + hora_grl * 86400000)
                else:
                    plus_millis = (matriz.index(dia) - 1) * 86400000
                    lista_horarios.append(miliseg + plus_millis)
    return lista_horarios

# Obtener la hora actual en milisegundos desde el inicio de la semana
def miliseg_week():
    hora_actual = datetime.now()
    miliseg = hora_actual.hour * 3600000 + hora_actual.minute * 60000 + hora_actual.second * 1000 + hora_actual.microsecond // 1000 + hora_actual.weekday() * 86400000
    return miliseg
