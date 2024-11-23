//funcion millis que es el reloj global
unsigned long inicio_millis = 0;  // Tiempo inicial sincronizado
unsigned long tiempo_objetivo = 0;  // Tiempo objetivo en milisegundos (establecido por ti)
unsigned long tiempo_espera = 3600000; // tiempo de espera para volver activar el sensor
unsigned long tiempo_restringuido = 900000; // tiempo de inactividad de los sensores

// Pines del HC-SR04
const int trigPin = 10;   // Pin Trig del sensor
const int echoPin = 9;    // Pin Echo del sensor

// Pines del motor y el parlante
const int motorPin = 13;  // Pin del motor
const int parlante = 6;   // Pin del parlante

// Umbral de distancia en centímetros
const int distanciaUmbral = 20;

// Variables de control
bool enEspera = false;    // Controla el tiempo de espera después de encender el motor
int contador_sensor = 0;  // contador de activaciones del sensor 

void setup() {
  // Configuración de pines
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  pinMode(parlante, OUTPUT);
  digitalWrite(motorPin, LOW);
  // Inicia comunicación serie
  Serial.begin(9600);
    while (!Serial) {
      ; // Espera a que el puerto serie esté disponible
  }

  // Leer el tiempo inicial desde el puerto serie
  while (Serial.available() == 0) {
    // Espera hasta que haya datos disponibles
  }

  String mensaje = Serial.readStringUntil('\n');  // Leer hasta el salto de línea
  inicio_millis = mensaje.toInt();  // Convertir el tiempo inicial a entero

  // Establece la hora objetivo (por ejemplo, 15:30:00 en milisegundos desde el día)
  int hora_objetivo = 21;
  int minuto_objetivo = 0;
  int segundo_objetivo = 0;
  tiempo_objetivo = (hora_objetivo * 3600000) + (minuto_objetivo * 60000) + (segundo_objetivo * 1000); 
}

void loop() {
  // Calcula el tiempo actual en milisegundos desde el inicio del día
  unsigned long tiempo_actual = millis() + inicio_millis;

  if (tiempo_actual < tiempo_objetivo - tiempo_restringuido || tiempo_actual >= tiempo_objetivo + tiempo_espera) {
    if (!enEspera) {
      // Enviar un pulso desde el pin Trig
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10); 
      digitalWrite(trigPin, LOW);

      // Leer el tiempo del pulso reflejado en el pin Echo
      long duracion = pulseIn(echoPin, HIGH);

      // Calcular la distancia en centímetros
      int distancia = duracion * 0.034 / 2;

      if (distancia > 0 && distancia <= distanciaUmbral) {
        // Se detecta un objeto dentro del rango
        Serial.println("Objeto detectado: Motor encendido.");
        digitalWrite(motorPin, LOW); // Encender el motor
        noTone(parlante);           // Apagar el parlante
        delay(1000);                // Mantener el motor encendido 1 segundo
        digitalWrite(motorPin, HIGH); // Apagar el motor
        contador_sensor += 1;  // Incrementar el contador de activaciones

        // Enviar el contador al monitor serie
        Serial.print("Contador del sensor: ");
        Serial.println(contador_sensor);

        // Entrar en estado de espera
        enEspera = true;
        Serial.println("Esperando 5 segundos para permitir otra señal.");
        delay(5000); // Tiempo de espera
        enEspera = false;
      } else {
        // No se detecta un objeto dentro del rango
        Serial.println("No se detecta objeto: Sonando parlante.");
        digitalWrite(motorPin, HIGH); // Asegurar que el motor esté apagado
        tone(parlante, 1000);         // Sonar el parlante (1000 Hz)
        delay(500);                   // Sonar durante 500 ms
        noTone(parlante);             // Apagar el parlante
        delay(500);                   // Pausa de 500 ms
      }
    } else {
      // Si está en espera, no realiza detecciones
      delay(100);
    }
  } else {
    // Apaga el motor y asegura que esté apagado
    Serial.println("Tiempo límite alcanzado: Motor apagado.");
    digitalWrite(motorPin, HIGH); // Asegura que el motor esté apagado
    noTone(parlante);            // Apaga el parlante (por si está activo)
    enEspera = true;             // Evita que vuelva a activarse
  }
}