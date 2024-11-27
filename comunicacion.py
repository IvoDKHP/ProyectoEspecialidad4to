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
    return total_segundos * 1000 # Convertir a milisegundos

def convertir_matriz(matriz, type):
    lista = []
    mtz = matriz
    general = matriz[0]
    for hora_grl in general:
        miliseg = convertir_a_millis(hora_grl)
        for dias in range(7):
            if hora_grl != '0:0':
                lista.append(miliseg + dias * 86400000)
        
    del mtz[0]
    for dia in mtz:
        for horario in dia:
            miliseg = convertir_a_millis(horario)
            if horario != '0:0':
                plus_millis = (mtz.index(dia) * 86400000)
                lista.append(miliseg + plus_millis)

    if type == "limite":
        new_list_2 = []
        for xd in lista:
            new_list_2.append([(xd - 900000), (xd + 3600000)])

        
        #ordenamiento de la lista
        for i in range(len(new_list_2) - 1): #Ordenar los horarios válidos por minutos
            for j in range(len(new_list_2) - 1 - i): #Generar numero de pasadas necesarias para acomodar
                #Si el valor de la derecha es mayor que el izquierdo se intercambian
                if new_list_2[j][1] > new_list_2[j + 1][1]:
                    new_list_2[j], new_list_2[j + 1] = new_list_2[j + 1], new_list_2[j]
        print(new_list_2)
        new_list = []
        t = 0
        a = 0

        while a < len(lista) - 1 - t:
            if new_list_2[a + 1][0] < new_list_2[a][1]:  # Checar si hay intersección
                new_interval = [new_list_2[a][0], new_list_2[a + 1][1]]
                del new_list_2[a + 1]  # Eliminar segundo intervalo
                new_list_2[a] = new_interval  # Actualizar primer intervalo
                t += 1  # Ajustar longitud lógica
            else:
                # Si no hay intersección, avanzar al siguiente intervalo
                new_list.append(new_list_2[a])
                a += 1
        # Añadir el último elemento no procesado
        if a < len(new_list_2):
            new_list.append(new_list_2[a])

        new_list_2 = []
        for x in new_list:
            new_list_2.append(x[0] )
            new_list_2.append(x[1])
        new_list_2 = list(set(new_list_2))
        new_list_2.sort()

        return new_list_2

    if len(lista) > 1:
        lista = list(set(lista))
        lista.sort()
    return lista
    


# Obtener la hora actual en milisegundos desde el inicio de la semana
def miliseg_week():
    hora_actual = datetime.now()
    miliseg = hora_actual.hour * 3600000 + hora_actual.minute * 60000 + hora_actual.second * 1000 + hora_actual.microsecond // 1000 + hora_actual.weekday() * 86400000
    return miliseg
