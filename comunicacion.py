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

def convertir_matriz(matriz, type):
    lista = []
    mtz = matriz
    """for horario in mtz:
        for dia_tm in horario:
            if dia_tm != "0:0":
                miliseg = convertir_a_millis(dia_tm)
                if dia_tm == mtz[0]:
                    for hora_grl in range(8):
                        lista.append(miliseg + hora_grl * 86400000)

                else:
                    plus_millis = (horario.index(dia_tm), mtz.index(horario))
                    print(plus_millis)
                    lista.append(miliseg )"""

    
    dia = []
    while len(dia) < len(mtz):
        horario = []
        while len(horario) < len(dia):
            if mtz[len(dia)][len(horario)] != "0:0":
                miliseg = convertir_a_millis(mtz[len(dia)][len(horario)])
                if len(dia) == 0:
                    for hora_grl in range(8):
                        lista.append(miliseg + hora_grl * 86400000)
                        print(hora_grl)
                        horario.append(0)
                    dia.append(0)
                
                else:
                    plus_millis = (len(dia) -1) * 86400000
                    print(plus_millis)
                    lista.append(miliseg)
                    horario.append(0)



    if type == "limite":
        new_list_2 = []
        for xd in lista:
            new_list_2.append([(xd - 900000), (xd + 3600000)])

        new_list = []
        t = 0
        a = 0
        for i in range(len(new_list_2) - 1): #Ordenar los horarios válidos por minutos
            for j in range(len(new_list_2) - 1 - i): #Generar numero de pasadas necesarias para acomodar
                #Si el valor de la derecha es mayor que el izquierdo se intercambian
                if new_list_2[j][1] > new_list_2[j + 1][1]:
                    new_list_2[j], new_list_2[j + 1] = new_list_2[j + 1], new_list_2[j]
        
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

        return new_list_2

    if len(lista) > 1:
        lista.sort()
        lista = list(set(lista))
    return lista
    


# Obtener la hora actual en milisegundos desde el inicio de la semana
def miliseg_week():
    hora_actual = datetime.now()
    miliseg = hora_actual.hour * 3600000 + hora_actual.minute * 60000 + hora_actual.second * 1000 + hora_actual.microsecond // 1000 + hora_actual.weekday() * 86400000
    return miliseg

matriz = [  ['0:0', '0:0', '0:0', '0:0', '0:0'],
            ['1:0', '2:0', '0:0', '0:0', '0:0'], 
            ['2:0', '0:0', '0:0', '0:0', '0:0'], 
            ['1:0', '0:0', '0:0', '0:0', '0:0'], 
            ['1:0', '0:0', '0:0', '0:0', '0:0'], 
            ['1:0', '0:0', '0:0', '0:0', '0:0'], 
            ['0:0', '0:0', '0:0', '0:0', '0:0'], 
            ['0:0', '0:0', '0:0', '0:0', '0:0']]
print(convertir_matriz(matriz, "horarios"))