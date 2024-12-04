import serial
import time
from datetime import datetime

# Configura el puerto serie
def conexion_arduino():
    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate= "9600", timeout=1)  # Cambia COM3 por tu puerto
    time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice
    #arduino.write("CONECTADO")
    return arduino

# Función para convertir hora:minuto a milisegundos
def convertir_a_millis(hora_minuto):
    horas, minutos = map(int, hora_minuto.split(":"))  # Separar y convertir a enteros
    total_minutos = horas * 60 + minutos  # Calcular el total de minutos
    return total_minutos # Enviar minutos

def convertir_matriz(matriz, type):
    lista = []
    mtz = [row[:] for row in matriz]
    general = matriz[0]
    for hora_grl in general:
        mins = convertir_a_millis(hora_grl)
        for dias in range(7):
            if hora_grl != '0:0':
                lista.append(mins + dias * 1440)
        
    del mtz[0]
    for dia_idx, dia in enumerate(mtz):
        for horario in dia:
            mins = convertir_a_millis(horario)
            if horario != '0:0':
                plus_mins = (dia_idx * 1440)
                lista.append(mins + plus_mins)

    if type == "limite":
        new_list_2 = []
        for xd in lista:
            new_list_2.append([(xd - 15), (xd + 60)])

        
        #ordenamiento de la lista
        for i in range(len(new_list_2) - 1): #Ordenar los horarios válidos por minutos
            for j in range(len(new_list_2) - 1 - i): #Generar numero de pasadas necesarias para acomodar
                #Si el valor de la derecha es mayor que el izquierdo se intercambian
                if new_list_2[j][1] > new_list_2[j + 1][1]:
                    new_list_2[j], new_list_2[j + 1] = new_list_2[j + 1], new_list_2[j]
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
    
def convertir_limites(lista_lm):
    # Verificamos si el primer valor es -1
    if lista_lm[0] == -1:
        lista_lm = [-1] * len(lista_lm)  # Establecemos todos los valores a -1
    else:
        # Sumamos el primer valor a todos los valores de la lista,
        # pero no modificamos los valores que ya son -1
        lista_lm = [x + lista_lm[0] if x != -1 else -1 for x in lista_lm]
    
    # Eliminamos el primer elemento
    del lista_lm[0]
    
    # Reemplazamos los valores 0 por -2, sin afectar los -1
    lista_lm = [-2 if x == 0 else x for x in lista_lm]
    
    return lista_lm

def generate_day_string():
    # Obtener la fecha y hora actual
    current_date = datetime.now()
    
    # Formatear la fecha en el formato deseado (por ejemplo, "2024-12-01")
    date_string = current_date.strftime("%Y-%m-%d")
    
    # Crear el string con la fecha actual
    return date_string


# Obtener la hora actual en milisegundos desde el inicio de la semana
def miliseg_week():
    hora_actual = datetime.now()
    miliseg = hora_actual.hour * 3600000 + hora_actual.minute * 60000 + hora_actual.second * 1000 + hora_actual.microsecond // 1000 + hora_actual.weekday() * 86400000
    return miliseg

"""matriz = [  ['0:0', '0:0', '0:0', '0:0', '0:0'],
            ['1:0', '2:0', '0:0', '0:0', '0:0'], 
            ['2:0', '0:0', '0:0', '0:0', '0:0'], 
            ['1:0', '0:0', '0:0', '0:0', '0:0'], 
            ['1:0', '0:0', '0:0', '0:0', '0:0'], 
            ['1:0', '0:0', '0:0', '0:0', '0:0'], 
            ['0:0', '0:0', '0:0', '0:0', '0:0'], 
            ['0:0', '0:0', '0:0', '0:0', '0:0']]
print(convertir_matriz(matriz, "hora"))
print(convertir_matriz(matriz, "limite"))

lista = [-1, 1, 2, 3, -1, 5, 6, 7]

print(convertir_limites(lista))"""