import serial
import time
from datetime import datetime

# Configura el puerto serie
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 por tu puerto
time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice

# Obtener la hora actual en milisegundos desde el inicio del día
hora_actual = datetime.now()
milisegundos_actuales = (hora_actual.hour * 3600000) + (hora_actual.minute * 60000) + (hora_actual.second * 1000) + (hora_actual.microsecond // 1000)

# Establecer la hora objetivo en milisegundos (ejemplo: 15:30:00)
hora_objetivo = 15
minuto_objetivo = 30
segundo_objetivo = 0
milisegundos_objetivo = (hora_objetivo * 3600000) + (minuto_objetivo * 60000) + (segundo_objetivo * 1000)

# Establecer el número máximo de activaciones del motor
max_activaciones = 10  # Número máximo de veces que el motor puede girar

# Crear un mensaje con los tres valores
mensaje = f"{milisegundos_actuales},{milisegundos_objetivo},{max_activaciones}"

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