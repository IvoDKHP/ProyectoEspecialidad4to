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

def convertir_matriz(matriz, type = "horarios"):
    lista = []
    for dia in matriz:
        for horario in dia:
            if horario != "0:0":
                miliseg = convertir_a_millis(horario)
                if dia == matriz[0]:
                    if type == "horarios":
                        for hora_grl in range(7):
                            lista.append(miliseg + hora_grl * 86400000)
                    elif type == "limite":
                        for limit_grl in range(7):
                            limite = [miliseg + limit_grl * 86400000 - 900000 ,miliseg + limit_grl * 86400000 + 3600000]
                            lista.append(limite)
                else:
                    plus_millis = (matriz.index(dia) - 1) * 86400000
                    if type  == "horarios":
                        lista.append(miliseg + plus_millis)
                    elif type == "limite":
                        limite = [miliseg + plus_millis - 900000, miliseg + plus_millis + 3600000]
                        lista.append(limite)

        if type == "limite":
            new_list = []
            t = 0
            a = 0
            for i in range(len(lista) - 1): #Ordenar los horarios válidos por minutos
                for j in range(len(lista) - 1 - i): #Generar numero de pasadas necesarias para acomodar
                    #Si el valor de la derecha es mayor que el izquierdo se intercambian
                    if lista[j][1] > lista[j + 1][1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
            while a < len(lista) - 1 - t:
                if lista[a + 1][0] < lista[a][1]:  # Checar si hay intersección
                    new_interval = [lista[a][0], lista[a + 1][1]]
                    del lista[a + 1]  # Eliminar segundo intervalo
                    lista[a] = new_interval  # Actualizar primer intervalo
                    t += 1  # Ajustar longitud lógica
                else:
                    # Si no hay intersección, avanzar al siguiente intervalo
                    new_list.append(lista[a])
                    a += 1
            # Añadir el último elemento no procesado
            if a < len(lista):
                new_list.append(lista[a])

            lista = []
            for x in new_list:
                lista.append(x[0] )
                lista.append(x[1])
            
            return lista

        elif type == "horarios":
            return lista.sort()
    


# Obtener la hora actual en milisegundos desde el inicio de la semana
def miliseg_week():
    hora_actual = datetime.now()
    miliseg = hora_actual.hour * 3600000 + hora_actual.minute * 60000 + hora_actual.second * 1000 + hora_actual.microsecond // 1000 + hora_actual.weekday() * 86400000
    return miliseg