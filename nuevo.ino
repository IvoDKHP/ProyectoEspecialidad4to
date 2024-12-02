unsigned long customMillis = 0; // Variable global para almacenar el valor inicial
unsigned long tiempoLimite = 0; // Variable para almacenar el tiempo recibido + 15 segundos
unsigned long offsetMillis = 0; // Diferencia entre millis() del Arduino y customMillis

const int motorPin1 = 13;
const int motorPin2 = 12;

void setup() {
  Serial.begin(9600);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    // Leer el dato numérico como cadena
    String input = Serial.readStringUntil('\n');
    input.trim(); // Eliminar caracteres extra

    // Intentar convertir el dato recibido a un número
    unsigned long recibido = input.toInt();
    if (recibido > 0) {
      customMillis = recibido;     // Establecer como valor inicial
      offsetMillis = millis();     // Capturar el valor actual de millis() en Arduino
      tiempoLimite = customMillis + 15000; // Sumar 15 segundos al valor recibido
    } else {
      Serial.println("Error: El valor recibido no es válido.");
    }
  }

  // Simular el paso del tiempo basado en customMillis
  unsigned long tiempoActual = customMillis + (millis() - offsetMillis);
  Serial.print("Horario actual (millis sincronizados): ");
  Serial.println(tiempoActual);

  // Verificar si el tiempo actual es mayor o igual al tiempo límite
  if (tiempoActual >= tiempoLimite && tiempoLimite != 0) {
    // Enciende el pin motorPin1 y apaga el pin motorPin2
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    Serial.println("Motor encendido");

    delay(5000); // Espera 5 segundos

    // Apaga ambos pines
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    Serial.println("Motor apagado");

    // Reinicia el tiempo límite para evitar reactivaciones innecesarias
    tiempoLimite = 0;
  }

  delay(1000); // Pausa para evitar saturar el monitor serie
}