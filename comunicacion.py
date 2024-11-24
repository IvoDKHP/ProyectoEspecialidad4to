import serial
import time
from datetime import datetime

# Configura el puerto serie
def conexion_arduino():
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 por tu puerto
    time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice
    return arduino
# Crear la matriz general con valores "hh:mm"
general = [
    "14:12",  # Primer valor
    "0:0",  # Segundo valor
    "0:0",  # Tercer valor
    "0:0",  # Cuarto valor
    "0:0"   # Quinto valor
]


class Dato_diario():
    pass
        

# Función para convertir hora:minuto a milisegundos
def convertir_a_millis(hora_minuto):
    horas, minutos = map(int, hora_minuto.split(":"))  # Separar y convertir a enteros
    total_segundos = horas * 3600 + minutos * 60  # Calcular el total de segundos
    return total_segundos * 1000  # Convertir a milisegundos

arduino = conexion_arduino()

# Convertir toda la matriz general y asignar valores a variables individuales
general_millis = [convertir_a_millis(valor) for valor in general]

# Obtener la hora actual en milisegundos desde el inicio del día
hora_actual = datetime.now()
milisegundos_actuales = (hora_actual.hour * 3600000) + (hora_actual.minute * 60000) + (hora_actual.second * 1000) + (hora_actual.microsecond // 1000)

# Establecer el número máximo de activaciones del motor
max_activaciones = 5  # Número máximo de veces que el motor puede girar

# Crear un mensaje con los valores
mensaje = f"{milisegundos_actuales},{max_activaciones}," + ",".join(map(str, general_millis))

# Intentar enviar los datos al Arduino
try:
    arduino.write(f"{mensaje}\n".encode())
    print(f"Enviando datos: {mensaje}")
except serial.SerialException as e:
    print(f"Error al intentar enviar datos al Arduino: {e}")

# Leer el contador enviado por Arduino
while True:
    try:
        if arduino.in_waiting > 0:
            mensaje = arduino.readline().decode('utf-8').strip()
            
            # Si el mensaje contiene el contador
            if "Contador del sensor:" in mensaje:
                contador = mensaje.split(":")[1].strip()
                print(f"Contador del sensor: {contador}")
    except serial.SerialException as e:
        print(f"Error al leer datos del Arduino: {e}")
    
    time.sleep(1)

arduino.close()