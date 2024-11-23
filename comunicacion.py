import serial
import time
from datetime import datetime

# Configura el puerto serie
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 por tu puerto
time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice

# Obtener la hora actual en milisegundos desde el inicio del día
hora_actual = datetime.now()
milisegundos_actuales = (hora_actual.hour * 3600000) + (hora_actual.minute * 60000) + (hora_actual.second * 1000) + (hora_actual.microsecond // 1000)

# Definir la hora objetivo en milisegundos (ejemplo: 21:00:00)
hora_objetivo = (3 * 3600000) + ( 54* 60000) + (0 * 1000)  # Cambiar según la necesidad

# Formatear y enviar el mensaje (hora_actual,hora_objetivo)
mensaje = f"{milisegundos_actuales},{hora_objetivo}\n"
arduino.write(mensaje.encode())
print(f"Enviando datos al Arduino: {mensaje}")

# Leer el contador desde el Arduino
while True:
    if arduino.in_waiting > 0:
        # Leer la línea enviada por el Arduino
        respuesta = arduino.readline().decode('utf-8').strip()
        
        try:
            # Convertir la respuesta en entero (contador del sensor)
            contador = int(respuesta)
            print(f"Contador del sensor: {contador}")
        except ValueError:
            print(f"Mensaje del arduino: {respuesta}")

    time.sleep(1)  # Pequeño retraso para evitar saturación del puerto

arduino.close()