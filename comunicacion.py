import serial
import time
from datetime import datetime

# Configura el puerto serie
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Cambia COM3 por tu puerto
time.sleep(2)  # Espera 2 segundos para que Arduino se estabilice

# Obtener la hora actual en milisegundos desde el inicio del día
hora_actual = datetime.now()
milisegundos_actuales = (hora_actual.hour * 3600000) + (hora_actual.minute * 60000) + (hora_actual.second * 1000) + (hora_actual.microsecond // 1000)

# Envía los milisegundos actuales al Arduino
arduino.write(f"{milisegundos_actuales}\n".encode())
print(f"Enviando milisegundos actuales: {milisegundos_actuales}")

# Leer el contador enviado por Arduino
while True:
    if arduino.in_waiting > 0:
        mensaje = arduino.readline().decode('utf-8').strip()
        
        # Si el mensaje contiene el contador
        if "Contador del sensor:" in mensaje:
            contador = mensaje.split(":")[1].strip()
            print(f"Contador del sensor: {contador}")
    
    time.sleep(1)

arduino.close()
